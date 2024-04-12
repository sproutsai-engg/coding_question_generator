import streamlit as st
import utils


def display_question(question_id, question_data, data, file_path):
    # Left column for question details
    left_column, right_column = st.columns([6, 10], gap="medium")
    with left_column:
        st.header(f"Question ID: {question_id}")
        st.write(f"**Question Title:** {question_data['title']}")
        st.write(f"**Question:** {question_data['description']}")
        st.write(f"**Example:** {question_data['example']}")
        st.write(f"**Level:** {question_data['level']}")
        st.write(f"**Tags:** {question_data['tags']}")
    
        ## display test cases
        st.subheader("Test Cases")
        
        ## display inputs 
        st.subheader("Inputs")
        st.text_area("Edit Inputs", question_data['test_cases']['inputs'], height=175+25)
            
        ## display outputs
        st.subheader("Outputs")
        st.text_area("Edit Outputs", question_data['test_cases']['outputs'], height=80)
        
    with right_column:
        for language in ["python", "c++", "java", "javascript"]:
            st.subheader(f":orange[**{language.capitalize()}**]")
            code_lang = language
            if language == "c++":
                code_lang = "cpp"
            height_multiplier = 25
            if language in question_data['sample_code']:
                sample_code_key = f"Sample_code_{language}_{question_id}"
                height = question_data['sample_code'][language].count("\n") * height_multiplier
                st.write(sample_code_key)
                st.code(question_data['sample_code'][language], line_numbers=True, language=code_lang)
                question_data['sample_code'][language] = st.text_area(f"Edit {language.capitalize()} Sample Code", 
                                                                      question_data['sample_code'][language], 
                                                                      key=sample_code_key, 
                                                                      height=height)
                
                
                if st.button(f"Updata {language.capitalize()} Sample Code"):
                    utils.save_json_file(file_path, data)
                    # st.session_state.question_index = 0
                    st.experimental_rerun()
            if language in question_data['structure']:
                structure_key = f"Structure_{language}_{question_id}"
                height = question_data['structure'][language].count("\n") * height_multiplier
                st.write(structure_key)
                st.code(question_data['structure'][language], line_numbers=True, language=code_lang)
                question_data['structure'][language] = st.text_area(f"Edit {language.capitalize()} Structure", 
                                                                    question_data['structure'][language], 
                                                                    key=structure_key, 
                                                                    height=height)

                if st.button(f"Updata {language.capitalize()} Structure"):
                    utils.save_json_file(file_path, data)
                    # st.session_state.question_index = 0
                    st.experimental_rerun()
            if language in question_data['call_functions']:
                call_function_key = f"Call_function_{language}_{question_id}"
                height = question_data['call_functions'][language].count("\n") * height_multiplier
                st.write(call_function_key)
                st.code(question_data['call_functions'][language], line_numbers=True, language=code_lang)
                question_data['call_functions'][language] = st.text_area(f"Edit {language.capitalize()} Call Function", 
                                                                         question_data['call_functions'][language], 
                                                                         key=call_function_key, 
                                                                         height=height)
            
                if st.button(f"Updata {language.capitalize()} Call Function"):
                    utils.save_json_file(file_path, data)
                    # st.session_state.question_index = 0
                    st.experimental_rerun()
            # st.subheader(f"Run {language.capitalize()} Code")
            if language in question_data['sample_code'] and language in question_data['call_functions']:
                code = question_data['sample_code'][language] + "\n\n" + question_data['call_functions'][language]
                
                if language == "python":
                    utils.run_button_python(code)
                elif language == "c++":
                    utils.run_button_cpp(code)
                elif language == "java":
                    utils.run_button_java(code)
            else:
                st.write(f":red[Please add {language.capitalize()} sample code and call function to run the code.]")
                
            