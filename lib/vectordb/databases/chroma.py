import os
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma
import chromadb
from chromadb.config import Settings
from lib.embeddings.index import embeddings
from chromadb.utils import embedding_functions

chroma_server_url = os.getenv('CHROMA_SERVER_URL')

class ChromaDB:
    def __init__(
        self,
        collection_name: str,
    ):
        self.collection_name = collection_name
        self.client = chromadb.HttpClient(settings=Settings(allow_reset=True, anonymized_telemetry=False, chroma_server_host=chroma_server_url))

        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-mpnet-base-v2') # for list of available models see: https://www.sbert.net/docs/pretrained_models.html
        if type(embeddings).__name__ == 'OpenAIEmbeddings':
            self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(api_key=os.getenv('OPENAI_API_KEY'))

    def init(self, documents: list[Document]):
        self.client.reset()  # resets the database
        collection = self.client.create_collection(self.collection_name, embedding_function=self.embedding_function)
        for doc in documents:
            collection.add(
                ids=doc.metadata['id'], metadatas=doc.metadata, documents=doc.page_content
            )

    def query(self, query: str) -> list[Document]:
        db = Chroma(client=self.client, collection_name=self.collection_name, embedding_function=embeddings)
        docs = db.similarity_search(query)
        return docs

    def reset(self):
        self.client.reset()