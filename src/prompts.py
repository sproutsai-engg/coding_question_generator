import utils
import json

def prompt_codingQ_details(ques_description):
    """This function generates the coding question details based on the given description.
    Args:
        ques_description (str): Description of the problem.
    Returns:
        dict: JSON format of the coding question details."""

    format = """{"title": "title of the problem",
              "description": "description of the problem",
              "example":"example of the problem",
              "level": "level of the problem",
              "tags": [
                    "tag1",
                    "tag2",
                    "tag3"
                ],
              "test_cases": {
                    "inputs":["List of test cases in their original data type"],
                    "outputs":["List of expected outputs in their original data type"]
                } }"""
                
    message=[{"role":"system","content":f"You are an expert in creating coding questions and you are tasked with generating a coding question based \
                                            on the given {ques_description}. Follow the Instructions given below to generate the coding question."},
             {"role":"user","content":f"""Generate a coding question based on the given description.
                Here is the description: \n\n ###{ques_description}### \n\n
                Here is the JSON format to be filled: \n\n ###{format}### \n\n
                Instructions:
                1. Extract the general information from the {ques_description}.
                    "title": Create a concise and descriptive title that accurately reflects the problem.
                    "description": Expand on the problem description, providing clear instructions and any necessary context. Pharaphrase the description.
                    "example":Include one well-formatted code example (input, expected output and explanation) to illustrate the problem.
                    "level": Choose the appropriate difficulty level (Easy, Medium, Hard) for the question.
                    "tags": Assign relevant tags related to the problem based on the type of problem (e.g., array, string, sorting).
                2. "test_cases":"Provide at least 20 test cases to validate the solution. Include both sample and edge cases to ensure the question is well-tested.
                    Store inputs inside the "inputs" key and expected outputs inside the "outputs" key. 
                3. Important: Keep the test cases in their respective data type. Example - "inputs": [1,2,3], "outputs": 6 for list of integers or "inputs": "hello", "outputs": "olleh" for strings. Don't mix data types.
                4. Make sure the JSON format is correct and all the fields are filled accurately.
                    Make sure there are no syntax issues or unexpected characters in the JSON format. Take care of the escape characters and the quotes.
                Important: This is for production use. Maintain consistent output, adhere to the template and avoid generating unnecessary or abusive content."""},
             {"role": "user", "content": f"Use \" insted of ' for the response keys. In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important."},
             {"role": "user", "content": f"Insted of Bachelor's, don't, can't, won't etc. Insted use ` like Bachelor`s, don`t, can`t."}]
    num_of_retries = 3
    for i in range(num_of_retries):
        try:
            model ="gpt35-16k"
            response = utils.get_from_gpt(message=message, model=model, temperature = 0.01, max_tokens = 6000)
            # print(response["content"])
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

def get_in_json(response, format):
    
    
    
    message = [{"role": "system", "content": "Convert the given response into JSON format with doubel quotes for keys and values.\
        You can refer to this format."},]    


def prompt_lang_structure(ques_description, language:list):
    
    format =  {
        "sample_code": {
            "c": "sample code in c",
            "cpp": "sample code in cpp",
            "javascript": "sample code in java",
            "python": "sample code in python"
        },
        "structure": {
            "c": "structure of the code in c",
            "cpp": "structure of the code in cpp",
            "javascript": "structure of the code in javascript",
            "python": "structure of the code in python"
        },
        "call_functions":{
            "c": "function name in c",
            "cpp": "function name in cpp",
            "javascript": "function name in javascript",
            "python": "function name in python"}
    }
    
    pass