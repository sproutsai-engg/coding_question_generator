import sys
sys.path.append('../../src')
import streamlit as st
import json
import streamlit_validate.utils as utils
import streamlit_validate.display_MCQs as display_MCQs

# file_path = r"coding_questions_merged.json"
file_path=r"C:\SaiVinay\SproutsAI\GitHub_\coding_question_generator\json_files\lightbeam\mcq_questions_v3 (1).json"

st.set_page_config(
    page_title="MCQs Test Platform Console",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    
)
## run command in terminal
# streamlit run main.py --server.runOnSave true     


def main():
    st.title("MCQs Test Platform Console")
    data = utils.load_json_file(file_path)
    question_ids = list(range(0, len(data)))
    
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    question_id = question_ids[st.session_state.question_index]

    length_of_questions = len(question_ids)
    current_index = st.session_state.question_index
    st.write(f"Question {current_index+1}/{length_of_questions}")

    st.sidebar.title("Actions")
    # side_bar_button = st.sidebar.button("")
    idx = st.sidebar.text_input("Question Index", st.session_state.question_index+1)
    if st.sidebar.button(":blue[Go to Question] :airplane:"):
        st.session_state.question_index = int(idx)
        st.experimental_rerun()
    
    # col1, col2, col3, col4, col5= st.columns(5)
    if st.sidebar.button(f":rewind: Previous Question"):
        st.session_state.question_index = max(0, st.session_state.question_index - 1)
        st.experimental_rerun()
        
    if st.sidebar.button("Refresh"):
        st.experimental_rerun()
    
    if st.sidebar.button(f" Next Question :fast_forward:"):
        st.session_state.question_index = min(len(question_ids) - 1, st.session_state.question_index + 1)
        st.experimental_rerun()
        
    display_MCQs.display_question(question_id, data, file_path)

if __name__ == "__main__":
    main()
