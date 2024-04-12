import streamlit as st
import json
import utils
import display_fun

file_path = r"coding_questions_merged.json"

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
    question_ids = list(data.keys())
    
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    question_id = question_ids[st.session_state.question_index]
    question_data = data[question_id]
    
     # Previous and Next buttons
    col1, col2= st.columns(2)
    if col1.button(f"Previous Question: {question_id}"):
        st.session_state.question_index = max(0, st.session_state.question_index - 1)
    st.write(f"Question ID: {question_id}")
    if col2.button(f"Next Question: {question_id}"):
        st.session_state.question_index = min(len(question_ids) - 1, st.session_state.question_index + 1)

    display_fun.display_question(question_id, question_data, data, file_path)

    # Save button
    if st.button("Save Changes"):
        utils.save_json_file(file_path, data)
        st.success("Changes saved successfully!")

    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    if st.session_state.question_index > 0:
        if col1.button("Previous Question"):
            st.session_state.question_index -= 1
            st.experimental_rerun()
    if st.session_state.question_index < len(question_ids) - 1:
        if col3.button("Next Question"):
            st.session_state.question_index += 1
            st.experimental_rerun()
    if col2.button("Reset"):
        st.session_state.question_index = 0
        st.experimental_rerun()

if __name__ == "__main__":
    main()
