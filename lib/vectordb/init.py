from lib.vectordb.index import vectordb
from lib.vectordb.load_docs import create_csv_data, load_hadith_csv_to_documents

create_csv_data(
    # quran_data_file_path='./data/source/quran.csv'
    quran_data_file_path=None,
    hadiths_data_file_path='./data/source/hadiths.csv',
    data_file_path='./data/data.csv'
)

documents = load_hadith_csv_to_documents("./data/data.csv")
print("Initializing and loading documents to vector database...")
vectordb.init(documents)
print("Successfully initialized vector database.")