import requests
import os
from dotenv import load_dotenv
import logging
from typing import List
import json

# Set up logging
logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

# Create a logger 
logger = logging.getLogger(__name__)


# Load environment variables from .env file
load_dotenv()

gpt_url = os.getenv("gpt_url")
gpt_model = os.getenv("gpt_model")
gpt_bearer = os.getenv("bearer")

def get_gpt(message, model =gpt_model, max_tokens = 2000, temperature=0.01):
    url = gpt_url
    headers = {
        'accept': 'application/json',
        'Authorization': gpt_bearer,
        'Content-Type': 'application/json',
    }
    data = {
        "api_type": "job",  # option -> resume, job, resume_match, linkedin_match
        "model": model,   #option -> gpt35-4k, gpt35-16k. gpt4-8k, 
        "message": message,
        "kwargs": {"max_tokens": max_tokens, "temperature": temperature}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # Request was successful
        return response.json()
    else:
        # Request failed
        return response.text
    
with open("coding_ques_template.json","r") as coding_ques_template:
    template=json.load(coding_ques_template)

def generate_coding_ques(ques_description,language:List):
    n=0
    while n<3:
        try:
            response=get_gpt(
                message=[{"role":"system","content":f"You are an expert in creating coding questions and you are tasked with generating a coding question based on the given {ques_description} and programming languages given in {language}. Follow the Instructions given below to generate the coding question."},
                {"role":"user","content":f"""Generate a coding question based on the given description for different programming languages mentioned in the list.
                    Here is the description: \n\n ###{ques_description}### \n\n
                    Here is the list of programming languages: \n\n ###{language}### \n\n
                    Here is the JSON format to be filled: \n\n ###{template}### \n\n
                    Instructions:
                    1. Extract the general information from the {ques_description}.
                        "title": Create a concise and descriptive title that accurately reflects the problem.
                        "description": Expand on the problem description, providing clear instructions and any necessary context.
                        "example":Include one well-formatted code example (input, expected output and explanation) to illustrate the problem.
                        "level": Choose the appropriate difficulty level (Easy, Medium, Hard) for the question.
                        "tags": Assign relevant tags related to the problem based on the type of problem (e.g., array, string, sorting).
                    2. "test_cases":"Provide at least 10 test cases to validate the solution. Include both sample and edge cases to ensure the question is well-tested. Store inputs inside the "inputs" key and expected outputs inside the "outputs" key.
                    3. For each language in {language}, fill out the following fields:
                        "sample_code": Provide a sample solution in the specified language using the language_name as key.
                        "structure:" Provide the structure of the code in the specified language using the language_name as key.This is the skeleton of code that the candidate will complete.
                        "call_functions": Provide the function call that would call the implemented function in the specified language using the language_name as key. Do include relevant include statements. Also, pass $args in place of the arguments.

                        Make sure there are no syntax issues or unexpected characters in the JSON format. Take care of the escape characters and the quotes.
                    Important: This is for production use. Maintain consistent output, adhere to the template and avoid generating unnecessary or abusive content."""}],)
            
            temp_dict=json.loads(response['content'])
            
            return temp_dict
        
        except Exception as e:
            if n==2:
                logger.error(f"An unexpected error occurred: {e}", exc_info=True)
        n+=1
    return "GPT response issue"
