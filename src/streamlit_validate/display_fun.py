import sys
sys.path.append('../../src')
import requests
import streamlit as st
import streamlit_validate.utils as utils
import streamlit_validate.display_testCases as display_testCases
import json


def display_question(question_id, question_data, data, file_path):
    # Left column for question details
    left_column, right_column = st.columns([7, 10], gap="medium")
    
    # left column is to display all the question details
    with left_column:
        height_multiplier = 30
        
        if "languages verified" not in question_data:
            question_data["languages verified"] = []
    
        st.header(f"Question ID: {question_id + 1}")
        st.write(f"**Question Title:** {question_data['title']}")
        
        description = question_data['description'] if 'description' in question_data else question_data['question']
        height = 180
        question_data['description'] = st.text_area("**Question:**",
                                                description,
                                                height=height)
        
        height = question_data['example'].count("\n") * height_multiplier
        question_data['example'] = st.text_area("**Example:**", 
                                                question_data['example'], 
                                                height=height)
        
        st.write(f"**Level:** {question_data['level']}")
        st.write(f"**Tags:** {question_data['tags']}")
    
        ## display test cases
        st.subheader("Test Cases: $args")
        display_testCases.testCases(question_data)
        
        
    # right column is for the code editor
    with right_column:
        # separate tabs for each language
        python_tab, javascript_tab, cpp_tab, java_tab = st.tabs(["Python", "Javascript", "C++", "Java"])
        
        for language in ["python","javascript", "c++", "java"]:
            if language == "python":
                with python_tab:
                     tab_function(question_id, question_data, data, file_path, language)
            elif language == "javascript":
                with javascript_tab:
                    tab_function(question_id, question_data, data, file_path, language)
            elif language == "c++":
                with cpp_tab:
                    # st.write("C++")
                    tab_function(question_id, question_data, data, file_path, language)
            elif language == "java":
                with java_tab:
                    tab_function(question_id, question_data, data, file_path, language)


                   
def tab_function(question_id, question_data, data, file_path, language):
    # check if the code is verified for the language
    if language in question_data["languages verified"]:
        verified = st.radio(f"{language.capitalize()} code verified..?",options=["Yes", "No"],index=0)
        if verified == "No":
            question_data["languages verified"].remove(language)
            utils.save_json_file(file_path, data)
            st.experimental_rerun()

    else:
        verified = st.radio(f"{language.capitalize()} code verified..?",options=["Yes", "No"],index=1)
        if verified == "Yes":
            question_data["languages verified"].append(language)
            utils.save_json_file(file_path, data)
            st.experimental_rerun()

    # display the code editor
    st.subheader(f":orange[**{language.capitalize()}**]")
    code_lang = language
    if language == "c++":
        code_lang = "cpp"
    height_multiplier = 30
    
    #display the sample code
    if language in question_data['sample_code']:
        sample_code_key = f"Sample_code_{language}_{question_id}"
        height = question_data['sample_code'][language].count("\n") * height_multiplier
        st.write(sample_code_key)
        # to display the code as in the IDE
        st.code(question_data['sample_code'][language], line_numbers=True, language=code_lang)
        # editor to edit the sample code
        question_data['sample_code'][language] = st.text_area(f"Edit {language.capitalize()} Sample Code", 
                                                            question_data['sample_code'][language], 
                                                            key=sample_code_key, 
                                                            height=height)
        
    #display the structure
    if language in question_data['structure']:
        structure_key = f"Structure_{language}_{question_id}"
        height = question_data['structure'][language].count("\n") * height_multiplier
        st.write(structure_key)
        # to display the code as in the IDE
        st.code(question_data['structure'][language], line_numbers=True, language=code_lang)
        # editor to edit the structure
        question_data['structure'][language] = st.text_area(f"Edit {language.capitalize()} Structure", 
                                                            question_data['structure'][language], 
                                                            key=structure_key, 
                                                            height=height)

        
    #display the call function
    if language in question_data['call_functions']:
        call_function_key = f"Call_function_{language}_{question_id}"
        height = question_data['call_functions'][language].count("\n") * height_multiplier + 50
        st.write(call_function_key)
        # to display the code as in the IDE
        st.code(question_data['call_functions'][language], line_numbers=True, language=code_lang)
        # editor to edit the call function
        question_data['call_functions'][language] = st.text_area(f"Edit {language.capitalize()} Call Function", 
                                                                question_data['call_functions'][language], 
                                                                key=call_function_key, 
                                                                height=height)
    
    if st.button(f"Updata {language.capitalize()} Code"):
        utils.save_json_file(file_path, data) 
        st.experimental_rerun()
            
    # to run the code in respective language
    # check the sample code and call function is available
    if language in question_data['sample_code'] and language in question_data['call_functions']:
        # aggregate the sample code and call function
        code = question_data['sample_code'][language] + "\n\n" + question_data['call_functions'][language]
        
        # run the code
        if language == "python":
            utils.run_button_python(code)
            run_all_test_cases(question_data, language= "python")
        elif language == "c++":
            utils.run_button_cpp(code)
            run_all_test_cases(question_data, language= "cpp")
        elif language == "java":
            # for java, add the necessary imports
            include_line = "import java.util.*;\nimport java.util.regex.Pattern;\n\npublic class Main {\n"
            end_line = "\n}"
            code = include_line + code + end_line
            utils.run_button_java(code)
            run_all_test_cases(question_data, language= "java")
        elif language == "javascript":
            utils.run_button_javascript(code)
            run_all_test_cases(question_data, language= "javascript")
    else:
        st.write(f":red[Please add {language.capitalize()} sample code and call function to run the code.]")

def run_all_test_cases(question_data, language):
    url = "https://dev.api.sproutsai.com/compiler/run_payload/"
    payload = {"language": language,
               "payload" : question_data}
    if st.button(f"Run All Test Cases in {language}"):
        response = requests.post(url, json=payload).json()
        
        failed_test_cases = []
        passed_test_cases = []
        failed_test_cases_number = []
        for i in range(len(response["data"])):
            _dict = response["data"][i]
            if _dict["testPassed"] == False:
                failed_test_cases.append(_dict)
                failed_test_cases_number.append(i+1)
            else:
                passed_test_cases.append(_dict)
        
        if len(failed_test_cases) == 0:
            st.success("All test cases passed!", icon="✅")
        else:
            st.error(f"{len(failed_test_cases)} test cases failed!", icon="🚫")
            st.error(f"Check these test cases: {failed_test_cases_number}")
        st.subheader("Failed Test Cases:")
        st.write(failed_test_cases)
        
        st.subheader("Passed Test Cases:")
        st.write(passed_test_cases)
        
    