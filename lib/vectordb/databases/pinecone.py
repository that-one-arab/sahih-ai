import os
import pinecone
from langchain.docstore.document import Document
from langchain.vectorstores import Pinecone
from lib.embeddings.index import embeddings

class PineconeDB:
    def __init__(
        self,
        index_name: str,
    ):
        self.index_name = index_name

    def init(self, documents: list[Document]):
        pinecone.init(
            api_key=os.environ['PINECONE_API_KEY'],
            environment=os.environ['PINECONE_ENVIRONMENT']
        )

        Pinecone.from_documents(documents, embeddings, index_name=self.index_name)

    def query(self, query: str) -> list[Document]:
        pinecone.init(      
            api_key=os.environ['PINECONE_API_KEY'],
            environment=os.environ['PINECONE_ENVIRONMENT']
        )

        docsearch = Pinecone.from_existing_index(self.index_name, embeddings)

        docs = docsearch.similarity_search(query)
        return docs

    def reset(self):
        index = pinecone.Index(self.index_name)
        index.delete(delete_all=True)