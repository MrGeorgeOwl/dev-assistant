import json

import requests

MODEL = "codellama"

def main():
    data = {
        "model": "codellama",
        "prompt": "Write me a function that writes a fibonacci sequence in Elixir",
    }    
    response = requests.post("http://localhost:11434/api/generate", json=data)
    jsons = response.text.split("\n")
    jsons = [json.loads(j) for j in jsons if j != ""]
    print(jsons)

if __name__ == '__main__':
    main()
