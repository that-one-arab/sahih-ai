from dotenv import load_dotenv

load_dotenv()

from lib.vectordb.index import vectordb

vectordb.reset()