#! env/bin/python3

import json
import argparse

import requests

MODEL = "codellama"


def _define_generator(subparsers):
    generator = subparsers.add_parser('generate', help='generating answer or file with a code.')
    generator.add_argument(
        "-p",
        "--prompt",
        dest="prompt",
        required=True,
        help="prompt to be used for ollama model",
    )
    generator.add_argument(
        "-o",
        "--output",
        dest="output",
        help="destination to output file",
        default="",
    )
    generator.set_defaults(func=generate)


def _define_reviewer(subparsers):
    reviewer = subparsers.add_parser('review', help='reviewing code with codellama model.')
    reviewer.add_argument(
        "-p",
        "--prompt",
        dest="prompt",
        required=True,
        help="prompt to be used for ollama model",
    )
    reviewer.add_argument(
        "-c",
        "--code_dest",
        dest="code_dest",
        help="destination to output file",
        default="",
    )
    reviewer.set_defaults(func=review)


def _define_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="possible methods to use:")
    _define_generator(subparsers)
    _define_reviewer(subparsers)
    
    return parser


def _ask_ollama(prompt: str) -> requests.Response:
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }    
    return requests.post("http://localhost:11434/api/generate", json=data)


def _write_output(output_dest: str, lines: list[str]) -> None:
    output = "".join(lines)
    if not output_dest:
        print(output)
        return

    with open(output_dest, "w") as f:
        if "```" in output:
            f.write(output.split("```")[1])
            return

        f.write(output)


def generate(args):
    response = _ask_ollama(args.prompt)

    jsons = response.text.split("\n")
    jsons = [json.loads(j)['response'] for j in jsons if j != ""]

    _write_output(args.output, jsons)


def review(args):
    print("review")


def main(args):
    args.func(args)


if __name__ == '__main__':
    parser = _define_argparser()
    args = parser.parse_args()
    main(args)
