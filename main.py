#! env/bin/python3

import argparse

import controllers


def _define_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="possible methods to use:")
    _define_generator(subparsers)
    _define_reviewer(subparsers)
    _define_asker(subparsers)

    return parser


def _define_generator(subparsers):
    generator = subparsers.add_parser(
        "generate", help="generating answer or file with a code."
    )
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
    generator.set_defaults(func=controllers.generate)


def _define_reviewer(subparsers):
    reviewer = subparsers.add_parser(
        "review", help="reviewing code with codellama model."
    )
    reviewer.add_argument(
        "-p",
        "--prompt",
        dest="prompt",
        required=True,
        help="prompt to be used for ollama model",
    )
    reviewer.add_argument(
        "-f",
        "--file",
        dest="file",
        help="destination to file with code to review",
        default="",
    )
    reviewer.set_defaults(func=controllers.review)


def _define_asker(subparsers):
    asker = subparsers.add_parser("ask", help="ask something codellama model.")
    asker.add_argument(
        "-p",
        "--prompt",
        dest="prompt",
        required=True,
        help="prompt to be used for ollama model",
    )
    asker.set_defaults(func=controllers.ask)


def main(args):
    args.func(args)


if __name__ == "__main__":
    parser = _define_argparser()
    args = parser.parse_args()
    main(args)
