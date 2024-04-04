import os
import json

import requests


MODEL = "codellama"


def generate(args):
    response = _ask_ollama(args.prompt)
    response_lines = _process_ollama_response(response)
    _write_output(args.output, response_lines)


def review(args):
    if not os.path.exists(args.file):
        raise ValueError("provided file with code should exist to review")

    with open(args.file) as f:
        code = "\n".join(f.readlines())

    response = _ask_ollama("\n".join((args.prompt, code)))
    response_lines = _process_ollama_response(response)

    _write_output("", response_lines)


def ask(args):
    response = _ask_ollama(args.prompt)
    response_lines = _process_ollama_response(response)

    _write_output("", response_lines)


def _ask_ollama(prompt: str) -> requests.Response:
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post("http://localhost:11434/api/generate", json=data)
    if response.status_code != 200:
        raise Exception("codellama responsed with error: %s", response.text)
    return response


def _process_ollama_response(response: requests.Response) -> list[str]:
    jsons = response.text.split("\n")
    return [json.loads(j)["response"] for j in jsons if j != ""]


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
