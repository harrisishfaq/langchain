######
INSTALLATION
######
1: Langchain
2: uv

######
STEPS
######
uv init                         #FOR CREATE PROJECT DIRECTORY
uv add langchain
uv add python-dotenv 
uv add black isort              #FOR PYTHON FORMATTING
uv add langchain-ollama         #FOR OLLAMA LLM
uv add langchain-google-genai   #FOR GOOGLE GEMINI API


######
TO RUN SCRIPTS
######
uv run main.py
