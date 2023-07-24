from dotenv import load_dotenv

load_dotenv()

from lib.vectordb.index import vectordb
from lib.vectordb.load_docs import create_csv_data, load_hadith_csv_to_documents

create_csv_data(
    './data/source/quran.csv',
    './data/source/hadiths.csv',
    './data/data.csv'
)

documents = load_hadith_csv_to_documents("./data/data.csv")
vectordb.init(documents)
print("Successfully initialized vector database")