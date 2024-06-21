import sys
sys.path.append('../../src')
import streamlit as st
import streamlit_validate.utils as utils

 
def display_question(question_id, data, file_path):
    question_data = data[question_id]
    # Left column for question details\
    left_column, right_column = st.columns([7, 10], gap="medium")
    
    with left_column:
        question_data['data']["question"]  = st.text_area(f"**Question: {question_id + 1}**", question_data['data']["question"])
        question_data['subject_tag'][0] = st.text_area(f"**Subject**", question_data['subject_tag'][0])
        question_data['topic_tag'][0] = st.text_area(f"**Topic**", question_data['topic_tag'][0])
        question_data['level_tag'][0] = st.text_area(f"**Level:**", question_data['level_tag'][0])
        
        question_data['data']['subject_tag'][0] = question_data['subject_tag'][0]
        question_data['data']['topic_tag'][0] = question_data['topic_tag'][0]
        question_data['data']['level_tag'][0] = question_data['level_tag'][0]
        
    with right_column:
        
            
        
        question_data['data']["choice_1"] = st.text_area(f"**Choice 1**", 
                                                         question_data['data']["choice_1"],
                                                         key=f"choice_1_{question_id}")
        
        question_data['data']["choice_2"] = st.text_area(f"**Choice 2**", 
                                                         question_data['data']["choice_2"], 
                                                         key=f"choice_2_{question_id}")
        
        question_data['data']["choice_3"] = st.text_area(f"**Choice 3**", 
                                                         question_data['data']["choice_3"], 
                                                         key=f"choice_3_{question_id}")
        
        question_data['data']["choice_4"] = st.text_area(f"**Choice 4**", 
                                                         question_data['data']["choice_4"], 
                                                         key=f"choice_4_{question_id}")
        
        question_data['data']["correct_choice"] = st.text_area(f"**Correct Choice**", 
                                                               question_data['data']["correct_choice"], 
                                                               key=f"correct_choice_{question_id}")
        
        if st.button(f"Save Edited Question"):
            utils.save_json_file(file_path, data)
            st.experimental_rerun()
            
        if st.button(f"Delete"):
            data.pop(question_id)
            utils.save_json_file(file_path, data)
            st.experimental_rerun()