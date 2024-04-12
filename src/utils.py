import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()
import time

openai_bearer = os.getenv("OPENAI_BEARER")

def get_from_gpt(message, model ="gpt35-16k", temperature = 0.01, max_tokens = 6000, api_type = "linkedin_match"):
    url = 'http://gptmodels.sproutsai.com/proxy'
    headers = {
        'accept': 'application/json',
        # 'Authorization': f'Bearer {openai_bearer}',
        'Content-Type': 'application/json',
    }
    data = {
        "api_type": api_type,  # option -> resume, job, match, test
        "model": model,   #option -> gpt35-4k, gpt35-16k. gpt4-8k, gpt4-32k
        "message": message,
        "kwargs": {"temperature":temperature, "max_tokens":max_tokens}
    }

    response = requests.post(url, headers=headers, json=data)
    # print(response)
    if response.status_code == 200:
        # Request was successful
        return response.json()
    else:
        # Request failed
        print("Error in get_from_gpt function")
        return {"error": response.status_code, "message": response.text}

def get_emb_finetuned(text_data):
    while True:
        try:
            # Define the URL
            url = 'http://embeddings.sproutsai.com/embeddings'

            # Define the headers
            headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json',
            }

            # Define the payload as a dictionary
            payload = {
                'text': text_data
            }
            # Convert the payload to JSON format
            payload_json = json.dumps(payload)

            # Make the POST request
            response = requests.post(url, headers=headers, data=payload_json)

            # Check the response status code and content
            if response.status_code == 200:
                result = response.json()
                return result['embeddings']
        except Exception as e:
            time.sleep(2)
            print(e)