from django.shortcuts import render
import sys
from llama_index import VectorStoreIndex, SimpleDirectoryReader, GPTVectorStoreIndex, SimpleMongoReader, ListIndex
import os
import openai

template = 'myapp/index.html'
host = "localhost"
port = 27017
db_name = "local"
collection_name = "<collection_name>"
field_names = ["text"]
query_dict = {}
reader = SimpleMongoReader(host, port)
openai.api_key = os.environ["OPENAI_API_KEY"]

def index(request):
    response = ""
    if request.method == "GET":
        return render(request, template)
    if request.method == "POST":
        documents = reader.load_data(
            db_name, collection_name, field_names, query_dict=query_dict
        )
        p = ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        print(ROOT_DIR + "/static/myapp/data/")
        documents2 = SimpleDirectoryReader(ROOT_DIR + "/static/myapp/data").load_data()
        print(documents2)
        # Create an index of your documents
        index = ListIndex.from_documents(documents2)
        print(documents)

        # Query your index!
        query_engine = index.as_query_engine()
        query_text = request.POST['llam-search']
        response = query_engine.query(query_text)

        # response = query_engine.query(search_string)
        print(response)
        context = {
            "result": response,
        }
        return render(request, template, context)


def upload(request):
    return "Success"
