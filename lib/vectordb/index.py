import os

is_pinecone = bool(os.getenv('PINECONE_API_KEY'))

index_name = "sahih-ai"

vectordb = None

if is_pinecone:
    print("Vector Database: Pinecone")
    from lib.vectordb.databases.pinecone import PineconeDB
    vectordb = PineconeDB(index_name)
else:
    print("Vector Database: Chroma")
    from lib.vectordb.databases.chroma import ChromaDB
    vectordb = ChromaDB(index_name)
