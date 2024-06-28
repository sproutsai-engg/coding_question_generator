import sys
sys.path.append('../../src')
import streamlit as st
import json
import streamlit_validate.utils as utils
import display_fun

# define the path of the json file
file_path=r"C:\SaiVinay\SproutsAI\GitHub_\coding_question_generator\json_files\tempCodingQuestionsV3_verified_50.json"

# set the page configuration
st.set_page_config(
    page_title="Code Test Platform Console",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    
)
## run command in terminal
# streamlit run main.py --server.runOnSave true     


def main():
    # file_path = st.file_uploader("Upload JSON File", type=["json"])
    
    st.title("Code Validation Console")
    data = utils.load_json_file(file_path)
    question_ids = list(range(0, len(data)))
    
    # to maintain the session state - question numbers to navigate
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    # to display the question, for the current index
    question_id = question_ids[st.session_state.question_index]
    question_data = data[question_id]

    length_of_questions = len(question_ids)
    current_index = st.session_state.question_index
    #add the current current index vs total questions
    st.write(f"Question {current_index+1}/{length_of_questions}")
    # Previous and Next buttons

    st.sidebar.title("Actions")
    # side_bar_button = st.sidebar.button("")
    idx = st.sidebar.text_input("Question Index", st.session_state.question_index)
    if st.sidebar.button(":blue[Go to Question] :airplane:"):
        st.session_state.question_index = int(idx)
        st.experimental_rerun()
    
    # col1, col2, col3, col4, col5= st.columns(5)
    if st.sidebar.button(f":rewind: Previous Question"):
        st.session_state.question_index = max(0, st.session_state.question_index - 1)
        st.experimental_rerun()
        
    if st.sidebar.button("Refresh"):
        st.experimental_rerun()
    
    if st.sidebar.button("Upload/Update"):
        _id = question_data["_id"]["$oid"]
        utils.save_json_file(file_path, data)
        question_data = data[question_id]
        utils.upload_coding_question_to_db(_id, question_data)
        
    # if st.sidebar.button("Update"):
    #     utils.save_json_file(file_path, data)
    #     utils.update_to_tempCodingQuestionsV3(question_id, question_data)

    if st.sidebar.button(f" Next Question :fast_forward:"):
        st.session_state.question_index = min(len(question_ids) - 1, st.session_state.question_index + 1)
        st.experimental_rerun()
    
    if "languages verified" in question_data:
        st.sidebar.title("Languages Verified")
        for lang in question_data["languages verified"]:
            st.sidebar.code(lang)
        
    # st.write(f"Question ID: {question_id}")
    display_fun.display_question(question_id, question_data, data, file_path)

   

if __name__ == "__main__":
    main()
