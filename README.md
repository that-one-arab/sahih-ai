## Setup
- **RECOMMENDED** Create a python virtual environment
- Run `pip install -r requirements.txt`
- Copy `.env.example` and rename to `.env`
- Fill the `.env` variables with your own values
- Run `python lib/vectordb/init.py` to initialize your vector database

## Usage
For development:
- Run `python main.py`

For production:
- Run `export PRODUCTION=True && hypercorn -b 127.0.0.1:8000 main:app`