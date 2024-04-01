#! env/bin/python3

import json
import argparse

import requests

MODEL = "codellama"

def _define_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--prompt",
        dest="prompt",
        required=True,
        help="prompt to be used for ollama model",
    )
    
    return parser

def main(args):
    data = {
        "model": "codellama",
        "prompt": args.prompt,
    }    
    response = requests.post("http://localhost:11434/api/generate", json=data)
    jsons = response.text.split("\n")
    jsons = [json.loads(j) for j in jsons if j != ""]
    print(jsons)

if __name__ == '__main__':
    parser = _define_argparser()
    args = parser.parse_args()
    main(args)
