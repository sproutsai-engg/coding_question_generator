
import sys
sys.path.append('../../src')
import requests
import streamlit as st
import streamlit_validate.utils as utils
import json

def testCases(question_data):
    for i in range(len(question_data['test_cases']['inputs'])):
            try:
                input_data = question_data['test_cases']['inputs'][i]
                input_type = type(input_data)
                output_data = question_data['test_cases']['outputs'][i]
                output_type = type(output_data)
                st.write(f"**Input {i+1}:** \t    {input_data} \t --> \t {input_type}")
                
                # st.code(input_data, line_numbers=True, language="python")
                st.write(f"**Output {i+1}:**    {output_data}  -->  {output_type}")
                # question_data['test_cases']['inputs'][i] = st.text_area(f"Edit Input {i+1}", input_data)
                # question_data['test_cases']['outputs'][i] = st.text_area(f"Edit Input {i+1}", output_data)
                # # st.code(output_data, line_numbers=True, language="python")
                # st.write("---")
                
                # Get user input as text
                edited_input = st.text_area(f"Edit Input {i+1}", input_data)
                edited_output = st.text_area(f"Edit Output {i+1}", output_data)

                # Convert text back to original type
                try:
                    if input_type == int:
                        question_data['test_cases']['inputs'][i] = int(edited_input)
                    elif input_type == float:
                        question_data['test_cases']['inputs'][i] = float(edited_input)
                    elif input_type == str:
                        question_data['test_cases']['inputs'][i] = edited_input
                    elif input_type == list:
                        question_data['test_cases']['inputs'][i] = json.loads(edited_input)
                    elif input_type == dict:
                        question_data['test_cases']['inputs'][i] = json.loads(edited_input)
                    elif input_type == bool:
                        question_data['test_cases']['inputs'][i] = json.loads(edited_input)
                    else:
                        st.warning(f"Unsupported input type: {input_type}")
                except ValueError as e:
                    st.error(f"Error converting input {i+1}: {e}")

                try:
                    if output_type == int:
                        question_data['test_cases']['outputs'][i] = int(edited_output)
                    elif output_type == float:
                        question_data['test_cases']['outputs'][i] = float(edited_output)
                    elif output_type == str:
                        question_data['test_cases']['outputs'][i] = edited_output
                    elif output_type == list:
                        question_data['test_cases']['outputs'][i] = json.loads(edited_output)
                    elif output_type == dict:
                        question_data['test_cases']['outputs'][i] = json.loads(edited_output)
                    elif output_type == bool:
                        question_data['test_cases']['outputs'][i] = json.loads(edited_output)
                    else:
                        st.warning(f"Unsupported output type: {output_type}")
                except ValueError as e:
                    st.error(f"Error converting output {i+1}: {e}")
            except:
                continue