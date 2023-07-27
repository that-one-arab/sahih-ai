from dotenv import load_dotenv

load_dotenv()

import os
import quart
import quart_cors
from quart import request, jsonify
from lib.vectordb.query import query_docs
from langchain.docstore.document import Document

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

IS_PRODUCTION = os.getenv('PRODUCTION') == "True"
PRODUCTION_URL = os.getenv('PRODUCTION_URL')
PRODUCTION_EMAIL = os.getenv('PRODUCTION_CONTACT_EMAIL')

def transform_documents_to_response(documents: list[Document]):
    new_list = []

    for doc in documents:
        new_dict = {}
        new_dict['english'] = doc.page_content
        # new_dict['id'] = doc.metadata['id'] # ID is not utilized, omit it for now, maybe delete it permanently later.
        new_dict['arabic'] = doc.metadata['arabic']
        new_dict['source'] = doc.metadata['source']
        new_list.append(new_dict)
    
    return new_list

def get_answer_template():
    """
    Defines the shape of the plugin's answer. This is the answer shape that the plugin will return
    """
    return """
**English**: 
{english}
**Arabic**: 
{arabic}
**Source**: 
{source}
"""

@app.get('/hello')
async def hello():
    return jsonify(message="Hello, World!")

@app.post("/api/query")
async def query_docs():
    request = await quart.request.get_json(force=True)
    query: str = request['query']

    response = query_docs(query)
    template = get_answer_template()
    # Transform class objects to dictionaries
    answers = transform_documents_to_response(response)

    return jsonify({
        "template": template,
        "hadiths": answers
    })

@app.get("/logo.png")
async def plugin_logo():
    filename = './static/openai/logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open("./static/openai/.well-known/ai-plugin.json") as f:
        text = f.read()
        if IS_PRODUCTION:
            text = text.replace("http://localhost:8000", PRODUCTION_URL)
            text = text.replace("test@test.com", PRODUCTION_EMAIL)
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    with open("./static/openai/openapi.yaml") as f:
        text = f.read()
        if IS_PRODUCTION:
            text = text.replace("http://localhost:8000", PRODUCTION_URL)
        return quart.Response(text, mimetype="text/yaml")

@app.get("/legal_info")
async def legal_info():
    host = request.headers['Host']
    with open("./static/html/legal_info.html") as f:
        html = f.read()
        return quart.Response(html)

def dev():
    app.run(debug=True, host="0.0.0.0", port=8000)

def main():
    app.run()

if __name__ == "__main__":
    if not IS_PRODUCTION:
        dev()
    else:
        main()