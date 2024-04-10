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

def get_gpt(message, model =gpt_model, max_tokens = 5000, temperature=0.01):
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
    
with open("description_temp.json","r") as desc_template:
    template=json.load(desc_template)

def generate_coding_ques(ques_description):
    n=0
    while n<3:
        try:
            response=get_gpt(
                message=[{"role":"system","content":f"You are an expert in creating coding questions and you are tasked with generating a coding question based on the given {ques_description}. Follow the Instructions given below to generate the coding question."},
                {"role":"user","content":f"""Generate a coding question based on the given description.
                 Here is the description: \n\n ###{ques_description}### \n\n
                    Here is the JSON format to be filled: \n\n ###{template}### \n\n
                    Instructions:
                    1. Extract the general information from the {ques_description}.
                        "title": Create a concise and descriptive title that accurately reflects the problem.
                        "description": Expand on the problem description, providing clear instructions and any necessary context.
                        "example":Include one well-formatted code example (input, expected output and explanation) to illustrate the problem.
                        "level": Choose the appropriate difficulty level (Easy, Medium, Hard) for the question.
                        "tags": Assign relevant tags related to the problem based on the type of problem (e.g., array, string, sorting).
                    2. "test_cases":"Provide at least 10 test cases to validate the solution. Include both sample and edge cases to ensure the question is well-tested. Store inputs inside the "inputs" key and expected outputs inside the "outputs" key.
                        Make sure there are no syntax issues or unexpected characters in the JSON format. Take care of the escape characters and the quotes.
                    Important: This is for production use. Maintain consistent output, adhere to the template and avoid generating unnecessary or abusive content."""},
                    
                    {"role": "user", "content": f"In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important."},
                {"role": "user", "content": f"Insted of Bachelor's, don't, can't, won't etc. Insted use ` like Bachelor`s, don`t, can`t."}],)
            
            temp_dict=json.loads(response['content'])
            
            return temp_dict
        
        except Exception as e:
            print(response)
            print(e)
            if n==2:
                
                logger.error(f"GPT response issue: {e}", exc_info=True)
        n+=1


l = ['cpp','java', 'python', 'javascript']

def generate_call_fun(sample_code):


    format = """ {"call_functions":
            {"cpp": "get he idea from example - #include <iostream>\n#include <string>\n\nint main() {\n \\\write your code \n  return 0;\n} but write the call function as per sample code",
              "java": "get he idea from example " - import java.util.Scanner;\n public class Main { \n public static void main(String[] args) {\n
            // Your code here\n } write the call function as per sample code \n",
            "python":"call(main) function for python from sample code",
              "javascript": "call(main) function for javascript sample code",
              } }
                """
    
    message=[{"role":"system","content":f"You are an expert in creating coding question call function (main function) and you are tasked with generating a call function of sample codes  based on the given {sample_code}. Follow the Instructions given below to generate the call function of coding question sample code."},
                {"role":"user","content":f"""Generate a coding question call function based on the given sample code.
                 Here is the sample: \n\n ###{sample_code}### \n\n
                    Here is the JSON format to be filled: \n\n ###{format}### \n\n
                    These are the Instructions:
                    1. write only the call(main) function from the {sample_code}.
                        "cpp": from sample code of cpp just write the call(main) function of it correctly, do not forget to write #include .
                        "java": from sample code of java just write the call(main) function of it, do not forget to write import.java .
                        "python":from sample code of python just write the code to run the functions from sample code of python
                        "javascript": from sample code of javascript just write the call(main) function of it.
                        
                    
                        Make sure there are no syntax issues or unexpected characters in the JSON format. Take care of the escape characters and the quotes.
                    Important: This is for production use. Maintain consistent output, adhere to the template and avoid generating unnecessary or abusive content."""},
                    
                    {"role": "user", "content": f"In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important."},
                {"role": "user", "content": f"Insted of Bachelor's, don't, can't, won't etc. Insted use ` like Bachelor`s, don`t, can`t."}]
            
    num_of_retries = 3
    for i in range(num_of_retries):
        try:
            model ="gpt35-16k"
            response = get_gpt(message=message, model=model, temperature = 0.01, max_tokens = 6000)
            print(response["content"])
            response_json = json.loads(response["content"])
            return response_json 
        
        except json.JSONDecodeError as e: ## If the response is not in JSON format
            print(e)
            try:
                response = response["content"][response["content"].find("{"): response["content"].rfind("}")+1]
                response_json = json.loads(response)
                return response_json 
            except Exception as f:
                print(f)
        
        except Exception as e: ## If there is any other error
            print(e)
            print(response["content"])
            if i == num_of_retries - 1:
                raise {"error": e}
            continue
            
            
    
