from langchain.docstore.document import Document
from langchain.vectorstores import Chroma
import chromadb
import uuid
from chromadb.config import Settings

class ChromaDB:
    def __init__(
        self,
        collection_name: str,
    ):
        self.collection_name = collection_name
        self.client = chromadb.HttpClient(settings=Settings(allow_reset=True))

    def init(self, documents: list[Document]):
        # self.client.reset()  # resets the database
        collection = self.client.create_collection(self.collection_name)
        for doc in documents:
            collection.add(
                ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
            )

        # db = Chroma(client=self.client, collection_name=self.collection_name)
        # docs = db.similarity_search(query)
        # print(docs)

    def query(self, query: str) -> list[Document]:
        db = Chroma(client=self.client, collection_name=self.collection_name)
        docs = db.similarity_search(query)
        print(docs)

    def reset(self):
        self.client.reset()