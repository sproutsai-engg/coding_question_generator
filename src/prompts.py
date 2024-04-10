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

def get_in_json(response, format):
    
    
    
    message = [{"role": "system", "content": "Convert the given response into JSON format with doubel quotes for keys and values.\
        You can refer to this format."},]  
    pass  


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


def prompt_call_func(language, sample_code):
    """This function generates the call function of the given sample code.
    Args:
        sample_code (str): Sample code of the problem."""
        
    format = {"sample_code": "sample code in c",
                  "call_functions": "function name in c"}    
    
    if language == "c++" or language == "cpp":
        ## few shot example according to the format
        example = {"sample_code": "#include <iostream>\nusing namespace std;\n\nbool isPowerOfFour(int n) {\n    if (n < 1) return false;\n    while (n % 4 == 0) n /= 4;\n    return n == 1;\n}\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    cout << boolalpha << result << endl;\n    return 0;\n}\n",
                   "call_functions": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    cout << boolalpha << result << endl;\n    return 0;\n}\n"}
    elif language == "python":
        example = {"sample_code": "def twoSum(nums, target):\n    map = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in map:\n            return [map[complement], i]\n        map[num] = i\n    return []\n",
                   "call_functions": "if __name__ == \"__main__\":\n    nums = $args[0]\n    target = $args[1]\n    result = twoSum(nums, target)\n    print(result)"}
    elif language == "java":
        example = {"sample_code": "import java.util.*;\n\npublic class Main {\n    public static boolean isPowerOfFour(int n) {\n        if (n < 1) return false;\n        while (n % 4 == 0) n /= 4;\n        return n == 1;\n    }\n\n    public static void main(String[] args) {\n        int n = $args;\n        boolean result = isPowerOfFour(n);\n        System.out.println(result);\n    }\n}\n",
                     "call_functions": "public static void main(String[] args) {\n        int n = $args;\n        boolean result = isPowerOfFour(n);\n        System.out.println(result);\n    }\n"}
    elif language == "javascript":
        example = {"sample_code": "function isPowerOfFour(n) {\n    if (n < 1) return false;\n    while (n % 4 === 0) n /= 4;\n    return n === 1;\n}\n\nfunction main() {\n    const n = $args;\n    const result = isPowerOfFour(n);\n    console.log(result);\n}\n",
                     "call_functions": "function main() {\n    const n = $args;\n    const result = isPowerOfFour(n);\n    console.log(result);\n}\n"}
    elif language == "c":
        example = {"sample_code": "#include <stdio.h>\n#include <stdbool.h>\n\nbool isPowerOfFour(int n) {\n    if (n < 1) return false;\n    while (n % 4 == 0) n /= 4;\n    return n == 1;\n}\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    printf(\"%s\", result ? \"true\" : \"false\");\n    return 0;\n}\n",
                     "call_functions": "#include <stdio.h>\n#include <stdbool.h>\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    printf(\"%s\", result ? \"true\" : \"false\");\n    return 0;\n}\n"}
    else:
        example = None
    
    if example:
        example_prompt = f"Here is the example in {language}: \n\n ###{example}### \n\n Take the above as just an example, I will provide you the actual sample code."
    else:
        example_prompt = ""
        
    message=[{"role":"system","content":f"You are an expert in creating a call function for the given sample code. \
                A 'call function' typically refers to invoking or executing a function in a programming context. \
                {example_prompt} \
                The sample code in {language} is provided here: \n\n {sample_code} \n\n"},
            {"role":"user","content":f""" Follow the Instructions given below to generate the call function of coding question sample code.
             
                    1. Function Declaration: Define function.
                    2. Argument Assignment: Assign the value of the input special variable as $args.
                    3. Function Invocation: Invoke the function with the argument  and assign the result to a constant named result.
                    4. Output: Print the value of the result.
                    
                Here is the JSON format to be filled: \n\n ###{format}### \n\n
                
                Important: 
                This is for production use. Maintain consistent output, adhere to the template and avoid generating unnecessary or abusive content.
                Use \" insted of ' for the response keys. In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important.
                Insted of Bachelor's, don't, can't, won't etc. Insted use ` like Bachelor`s, don`t, can`t."""}]
            
    num_of_retries = 3
    model ="gpt35-16k"
    for i in range(num_of_retries):
        try:
            
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
            model ="gpt4-8k"
            print(e)
            print(response["content"])
            if i == num_of_retries - 1:
                raise {"error": e}
            continue