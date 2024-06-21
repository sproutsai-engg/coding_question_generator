import utils
import json
import time


def prompt_codingQ_details(ques_description):
    """This function generates the coding question details based on the given description.
    Args:
        ques_description (str): Description of the problem.
    Returns:
        dict: JSON format of the coding question details."""

    format = """{"title": "title of the problem",
              "description": "Expand on the problem description of the problem",
              "example":"example of the problem",
              "level": "level of the problem EASY/MEDIUM/HARD",
              "tags": [
                    "Assign relevant tags related to the problem based on the type of problem"
                ],
              "test_cases": {
                    "inputs":["List of test cases in their original data type, atleast 10"],
                    "outputs":["List of expected outputs in their original data type, atleast 10"]
                } }"""

    message = [
        {
            "role": "system",
            "content": f"You are an expert in creating coding questions and you are tasked with generating a coding question based \
                                            on the given {ques_description}. Follow the Instructions given below to generate the coding question.",
        },
        {
            "role": "user",
            "content": f"""Generate a coding question based on the given description.
                Here is the description: \n\n ###{ques_description}### \n\n
                
                Here is the JSON format to be filled: \n {format}\n\n Use \" insted of ' for the response keys. In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important.
                
                Instructions:
                1. Extract the general information from the {ques_description}.
                2. Important: Keep the test cases in their respective data type. Example - "inputs": [1,2,3], "outputs": 6 for list of integers or "inputs": "hello", "outputs": "olleh" for strings. Don't mix data types.
               """,
        },
        {
            "role": "user",
            "content": f"Important: Use \" insted of ' for the response keys. In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important.",
        },
        {
            "role": "user",
            "content": f"Insted of Bachelor's, don't, can't, won't etc. Insted use ` like Bachelor`s, don`t, can`t.",
        },
    ]
    num_of_retries = 3
    for i in range(num_of_retries):
        try:
            model = "gpt4-8k"
            api_type = "linkedin_match"
            response = utils.get_from_gpt(
                message=message,
                model=model,
                temperature=0.01,
                max_tokens=2000,
                api_type=api_type,
            )
            print(response)
            response_json = json.loads(response["content"].replace("\n", ""))
            return response_json

        except json.JSONDecodeError as e:  ## If the response is not in JSON format
            try:
                response = response["content"][
                    response["content"].find("{") : response["content"].rfind("}") + 1
                ]
                response_json = json.loads(response)
                return response_json
            except Exception as f:
                print(f"Json Error in prompt_codingQ_details: {f}")

        except Exception as e:  ## If there is any other error
            print(f"Error in prompt_codingQ_details: {e}")
            print(response["content"])
            if i == num_of_retries - 1:
                raise {"error": e}
            time.sleep(10)
            continue


def get_in_json(response, format):

    message = [
        {
            "role": "system",
            "content": "Convert the given response into JSON format with doubel quotes for keys and values.\
        You can refer to this format.",
        },
    ]
    pass


def prompt_lang_structure(ques_description, language: list):

    format = {
        "sample_code": {
            "c": "sample code in c",
            "cpp": "sample code in cpp",
            "javascript": "sample code in java",
            "python": "sample code in python",
        },
        "structure": {
            "c": "structure of the code in c",
            "cpp": "structure of the code in cpp",
            "javascript": "structure of the code in javascript",
            "python": "structure of the code in python",
        },
        "call_functions": {
            "c": "function name in c",
            "cpp": "function name in cpp",
            "javascript": "function name in javascript",
            "python": "function name in python",
        },
    }

    pass


def prompt_call_func(language, sample_code):
    """This function generates the call function of the given sample code.
    Args:
        sample_code (str): Sample code of the problem."""

    format = """{"call_functions": "Give the call function here"}"""

    if language == "c++" or language == "cpp":
        ## few shot example according to the format
        example = {
            "sample_code": "#include <iostream>\nusing namespace std;\n\nbool isPowerOfFour(int n) {\n    if (n < 1) return false;\n    while (n % 4 == 0) n /= 4;\n    return n == 1;\n}\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    cout << boolalpha << result << endl;\n    return 0;\n}\n",
            "call_functions": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    cout << boolalpha << result << endl;\n    return 0;\n}\n",
        }

    elif language == "python":
        example = {
            "sample_code": "def twoSum(nums, target):\n    map = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in map:\n            return [map[complement], i]\n        map[num] = i\n    return []\n",
            "call_functions": 'if __name__ == "__main__":\n    nums = $args[0]\n    target = $args[1]\n    result = twoSum(nums, target)\n    print(result)',
        }

    elif language == "java":
        example = {
            "sample_code": "import java.util.*;\n\npublic class Main {\n    public static boolean isPowerOfFour(int n) {\n        if (n < 1) return false;\n        while (n % 4 == 0) n /= 4;\n        return n == 1;\n    }\n\n    public static void main(String[] args) {\n        int n = $args;\n        boolean result = isPowerOfFour(n);\n        System.out.println(result);\n    }\n}\n",
            "call_functions": "public static void main(String[] args) {\n        int n = $args;\n        boolean result = isPowerOfFour(n);\n        System.out.println(result);\n    }\n",
        }

    elif language == "javascript":
        example = {
            "sample_code": "function isPowerOfFour(n) {\n    if (n < 1) return false;\n    while (n % 4 === 0) n /= 4;\n    return n === 1;\n}\n\nfunction main() {\n    const n = $args;\n    const result = isPowerOfFour(n);\n    console.log(result);\n}\n",
            "call_functions": "function main() {\n    const n = $args;\n    const result = isPowerOfFour(n);\n    console.log(result);\n}\n",
        }

    elif language == "c":
        example = {
            "sample_code": '#include <stdio.h>\n#include <stdbool.h>\n\nbool isPowerOfFour(int n) {\n    if (n < 1) return false;\n    while (n % 4 == 0) n /= 4;\n    return n == 1;\n}\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    printf("%s", result ? "true" : "false");\n    return 0;\n}\n',
            "call_functions": '#include <stdio.h>\n#include <stdbool.h>\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    printf("%s", result ? "true" : "false");\n    return 0;\n}\n',
        }
    else:
        example = None

    if example:
        example_prompt = f"Here is the example in {language}: \n\n ###{example}### \n\n Take the above as just an example, I will provide you the actual sample code."
    else:
        example_prompt = ""

    message = [
        {
            "role": "system",
            "content": f"You are an expert in creating a call function for the given sample code. \
                A 'call function' typically refers to invoking or executing a function in a programming context. \
                {example_prompt} \
                The sample code in {language} is provided here: \n\n {sample_code} \n\n",
        },
        {
            "role": "user",
            "content": f""" Follow the Instructions given below to generate the call function of coding question sample code.
             
                    1. Function Declaration: Define function.
                    2. Argument Assignment: Assign the value of the input special variable as $args.
                    3. Function Invocation: Invoke the function with the argument  and assign the result to a constant named result.
                    4. Output: Print the value of the result.
                    5. Important note: Donot give sample code in the call function. Call function should be a standalone code that can be run to test the sample code.
                    
                Here is the JSON format to be filled: \n\n {format} \n\n Use \" insted of ' for the response keys. In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important.
                
                Important: 
                This is for production use. Maintain consistent output, adhere to the template and avoid generating unnecessary or abusive content.
                """,
        },
        {
            "role": "user",
            "content": f"Insted of Bachelor's, don't, can't, won't etc. Insted use ` like Bachelor`s, don`t, can`t.",
        },
    ]

    num_of_retries = 3
    model = "gpt4-8k"
    api_type = "linkedin_match"
    for i in range(num_of_retries):
        try:

            response = utils.get_from_gpt(
                message=message,
                model=model,
                temperature=0.01,
                max_tokens=2000,
                api_type=api_type,
            )
            response_json = json.loads(response["content"])
            return response_json

        except json.JSONDecodeError as e:  ## If the response is not in JSON format

            try:
                response = response["content"][
                    response["content"].find("{") : response["content"].rfind("}") + 1
                ].replace("'", '"')
                response_json = json.loads(response)
                return response_json
            except Exception as f:
                model = "gpt4-8k"
                print(f"Json Error in prompt_call_func: {f}")

        except Exception as e:  ## If there is any other error
            model = "gpt4-8k"
            print(f"Error in prompt_call_func: {e}")
            print(response["content"])
            if i == num_of_retries - 1:
                raise {"error": e}
            time.sleep(10)
            continue


def sample_code_and_call_function_generator(language, title, example, description):
    """This function generates sample code for the given title, example and description.
    Args:
        sample_code (str): Sample code of the problem."""

    format = """{"sample_code": "Give the sample code here",
                "call_functions": "Give the call function here"}"""

    if language == "c++" or language == "cpp":
        ## few shot example according to the format
        few_shot_example = {
            "sample_code": "#include <iostream>\nusing namespace std;\n\nbool isPowerOfFour(int n) {\n    if (n < 1) return false;\n    while (n % 4 == 0) n /= 4;\n    return n == 1;\n}\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    cout << boolalpha << result << endl;\n    return 0;\n}\n",
            "call_functions": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    cout << boolalpha << result << endl;\n    return 0;\n}\n",
        }

    elif language == "python":
        few_shot_example = {
            "sample_code": "def twoSum(nums, target):\n    map = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in map:\n            return [map[complement], i]\n        map[num] = i\n    return []\n",
            "call_functions": 'if __name__ == "__main__":\n    nums = $args[0]\n    target = $args[1]\n    result = twoSum(nums, target)\n    print(result)',
        }

    elif language == "java":
        few_shot_example = {
            "sample_code": "import java.util.*;\n\npublic class Main {\n    public static boolean isPowerOfFour(int n) {\n        if (n < 1) return false;\n        while (n % 4 == 0) n /= 4;\n        return n == 1;\n    }\n\n    public static void main(String[] args) {\n        int n = $args;\n        boolean result = isPowerOfFour(n);\n        System.out.println(result);\n    }\n}\n",
            "call_functions": "public static void main(String[] args) {\n        int n = $args;\n        boolean result = isPowerOfFour(n);\n        System.out.println(result);\n    }\n",
        }

    elif language == "javascript":
        few_shot_example = {
            "sample_code": "function isPowerOfFour(n) {\n    if (n < 1) return false;\n    while (n % 4 === 0) n /= 4;\n    return n === 1;\n}\n\nfunction main() {\n    const n = $args;\n    const result = isPowerOfFour(n);\n    console.log(result);\n}\n",
            "call_functions": "function main() {\n    const n = $args;\n    const result = isPowerOfFour(n);\n    console.log(result);\n}\n",
        }

    elif language == "c":
        few_shot_example = {
            "sample_code": '#include <stdio.h>\n#include <stdbool.h>\n\nbool isPowerOfFour(int n) {\n    if (n < 1) return false;\n    while (n % 4 == 0) n /= 4;\n    return n == 1;\n}\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    printf("%s", result ? "true" : "false");\n    return 0;\n}\n',
            "call_functions": '#include <stdio.h>\n#include <stdbool.h>\n\nint main() {\n    int n = $args;\n    bool result = isPowerOfFour(n);\n    printf("%s", result ? "true" : "false");\n    return 0;\n}\n',
        }
    else:
        few_shot_example = None

    if example:
        example_prompt = f"Here is the few shot example in {language}: \n\n ###{few_shot_example}### \n\n Take the above as just an example, I will provide you the actual sample code."
    else:
        example_prompt = ""

    message = [
        {
            "role": "system",
            "content": f"You are an expert in creating a sample code and call function for the given sample code. \
                The sample code should be written to solve any test case given to it. You will be provided an sample test cases of input and expected outputs.\
                Here are the details of the question:\nTitle of the question: {title}\nDescription: {description}\nSample test cases or exmple inputs and outputs: {example}\
                A 'call function' typically refers to invoking or executing a function in a programming context. \
                {example_prompt} \
                ",
        },
        {
            "role": "user",
            "content": f""" Follow the Instructions given below to generate the call function of coding question sample code.
             
                    1. Function Declaration: Define function.
                    2. Argument Assignment: Assign the value of the input special variable as $args.
                    3. Function Invocation: Invoke the function with the argument  and assign the result to a constant named result.
                    4. Output: Print the value of the result.
                    5. Important note: Donot give sample code in the call function. Call function should be a standalone code that can be run to test the sample code.
                    
                Here is the JSON format to be filled: \n\n {format} \n\n Use \" insted of ' for the response keys. In the generated data avoid using ' in generated data, use \" (double quotes),  This is very important.
                
                Important: 
                This is for production use. Maintain consistent output, adhere to the template and avoid generating unnecessary or abusive content.
                """,
        },
        {
            "role": "user",
            "content": f"Insted of Bachelor's, don't, can't, won't etc. Insted use ` like Bachelor`s, don`t, can`t.",
        },
    ]

    num_of_retries = 3
    model = "gpt4-8k"
    api_type = "linkedin_match"
    for i in range(num_of_retries):
        try:

            response = utils.get_from_gpt(
                message=message,
                model=model,
                temperature=0.01,
                max_tokens=2000,
                api_type=api_type,
            )
            response_json = json.loads(response["content"])
            return response_json

        except json.JSONDecodeError as e:  ## If the response is not in JSON format

            try:
                response = response["content"][
                    response["content"].find("{") : response["content"].rfind("}") + 1
                ].replace("'", '"')
                response_json = json.loads(response)
                return response_json
            except Exception as f:
                model = "gpt4-8k"
                print(f"Json Error in prompt_call_func: {f}")

        except Exception as e:  ## If there is any other error
            model = "gpt4-8k"
            print(f"Error in prompt_call_func: {e}")
            print(response["content"])
            if i == num_of_retries - 1:
                raise {"error": e}
            time.sleep(10)
            continue