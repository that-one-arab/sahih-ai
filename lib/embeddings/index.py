import os

is_openai_embeddings = os.getenv('EMBEDDINGS') == 'openai'

embeddings = None

if is_openai_embeddings:
    print("Embeddings: Open AI")
    from langchain.embeddings.openai import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings()
else:
    print("Embeddings: Sentence Transformer")
    from langchain.embeddings import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings()
