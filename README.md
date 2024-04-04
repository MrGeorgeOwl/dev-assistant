# codellama CLI helper

CLI tool to ask locally deployed ollama model to help developer to be more productive at work.


## Requirements:

* Docker
* Python 3.10+
* make

## How to start?

Run following command to prepare environment to use CLI:

```shell
make prepare
```

*Note*: make sure port 11434 is free to use because container will use it to connect with our CLI

The command will create ollama container, pull codellama model and create python virtual environment for CLI to use.

And now you are ready to go!

## How to use?

You can alway ask CLI to show help window:

```shell
./main.py --help
usage: main.py [-h] {generate,review,ask} ...

positional arguments:
  {generate,review,ask}
                        possible methods to use:
    generate            generating answer or file with a code.
    review              reviewing code with codellama model.
    ask                 ask something codellama model.

options:
  -h, --help            show this help message and exit
```

### Ask

You can ask codellama model with ask utility:

```shell
./main.py ask -p "What is the best programming language to learn right now?"
```

Parameters:
* -p - prompt to send to codellama model. Required.

### Generate

You can ask codellama model to generate code with generate utility:

```shell
./main.py generate -p "Generate code for simple API in FastAPI." -o api.py
```

Parameters:
* -p - prompt to send to codellama model. Required.
* -o - output file where generated code should be written to. Default to "". 
If empty then answer will be printed to console.

### Review

You can ask codellama model to review code with review utility:

```shell
./main.py review -p "How can I improve following code?" -f api.py
```

Parameters:
* -p - prompt to send to codellama model. Required.
* -f - file with code to review. Required.
