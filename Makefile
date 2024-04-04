run_model:
	if [ -n $(docker ps -a | grep ollama) ]; then \
	    echo "starting already created ollama model" && \
	    docker start ollama;\
	else \
	    echo "There is no ollama yet, creating..." && \
	    docker run -d -v ./ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama;\
	fi

prepare_env:
	@if [ -d ./env ]; then \
	    echo "environment exists"; \
	else \
	    echo "Creating environment..."; \
	    python -m venv env \
	    && source ./env/bin/activate \
	    && pip install -U pip \
	    && pip install -r requirements.txt; \
	    echo '\nUse "source env/bin/activate" command to use newly created environment'; \
	fi; \

format: prepare_env
	source ./env/bin/activate && ruff format .

check: prepare_env
	source ./env/bin/activate && ruff check . --fix
