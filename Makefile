prepare: prepare_python_env run_model
	@echo "Environment is ready to use CLI"

run_model:
	@docker start ollama || \
		(docker run -d -v ./ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama && \
		docker exec -it ollama ollama pull codellama)

prepare_python_env:
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

format: prepare_python_env
	source ./env/bin/activate && ruff format .

check: prepare_python_env
	source ./env/bin/activate && ruff check . --fix
