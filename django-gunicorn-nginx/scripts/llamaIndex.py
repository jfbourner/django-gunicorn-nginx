import openai
import logging
import sys
import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, GPTVectorStoreIndex

openai.api_key = os.environ["OPENAI_API_KEY"]
def run():

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

    print(f'Running with key')
    # Load you data into 'Documents' a custom type by LlamaIndex
    documents = SimpleDirectoryReader('django-gunicorn-nginx/data').load_data()

    # Create an index of your documents
    index = GPTVectorStoreIndex.from_documents(documents)

    # Query your index!
    query_engine = index.as_query_engine()
    response = query_engine.query("What do you think of Facebook's LLaMa?")
    print(response)
    print("complete")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

