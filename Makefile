run_model:
	if [ -n $(docker ps -a | grep ollama) ]; then \
	    echo "starting already created ollama model" && \
	    docker start ollama;\
	else \
	    echo "There is no ollama yet, creating..." && \
	    docker run -d -v ./ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama;\
	fi
