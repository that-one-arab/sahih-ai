from lib.vectordb.databases.pinecone import PineconeDB
# from lib.vectordb.databases.chroma import ChromaDB

index_name = "sahih-ai"

vectordb = PineconeDB(index_name)
# vectordb = ChromaDB(index_name)
