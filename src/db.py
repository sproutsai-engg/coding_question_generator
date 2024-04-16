from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# MongoDB Atlas connection string. from .env file
load_dotenv()
uri = os.getenv('NLPCLUSTER')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def tempCodingQuestionsV3():
    return client.questionGeneration.tempCodingQuestionsV3

