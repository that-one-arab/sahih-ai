from langchain.docstore.document import Document

from lib.vectordb.index import vectordb


def query_docs(query: str) -> list[Document]:
	return vectordb.query(query)