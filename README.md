## About
The Sahih AI server.
Handles serving Chat GPT plugin requests

## Setup
- **RECOMMENDED** Create a python virtual environment
- Run `pip install -r requirements.txt`
- Run `pip install pinecone-client sentence_transformers` to install vector db related dependencies
- Copy `.env.example` and rename to `.env`
- Fill the `.env` variables with your own values
- Run `python vectordb.py init` to initialize your vector database

## Usage
For development:
- Run `python main.py`

For production:
- Run `export PRODUCTION="True" && gunicorn -k uvicorn.workers.UvicornWorker main:app`

## Notes
- This project was developed using python version 3.10 and pip version 23.1