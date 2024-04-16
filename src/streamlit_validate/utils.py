import json
import subprocess
import streamlit as st
import db



def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


### Run Python code
def run_python_code(code):
    # Save the code to a temporary file
    with open("temp.py", "w") as file:
        file.write(code)

    # Execute the Python script using subprocess
    process = subprocess.Popen(["python", "temp.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Return the output and any errors
    return stdout.decode(), stderr.decode()

def run_button_python(code):
    if st.button(":green[Run Python Code]"):
        stdout, stderr = run_python_code(code)

        # Display the output and errors
        if stdout:
            st.subheader("Output:")
            st.code(stdout)
            st.success('Success!', icon="✅")
        else:
            st.subheader("Errors:")
            st.code(stderr)

### Run C++ code
def run_cpp_code(code):
    # Save the code to a temporary file
    with open("temp.cpp", "w") as file:
        file.write(code)

    # Compile the C++ code
    compile_process = subprocess.Popen(["g++", "temp.cpp", "-o", "temp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    compile_stdout, compile_stderr = compile_process.communicate()

    if compile_stderr:
        # Return compilation error if any
        return None, compile_stderr.decode()

    # Execute the compiled binary
    run_process = subprocess.Popen(["./temp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = run_process.communicate()

    return stdout.decode(), stderr.decode()

def run_button_cpp(code):
    # Add a button to compile and run the code
    if st.button(":green[Compile and Run C++]"):
        stdout, stderr = run_cpp_code(code)

        # Display the output and errors
        if stdout:
            st.subheader("Output:")
            st.code(stdout)
            st.success('Success!', icon="✅")
        else:
            st.subheader("Compilation Error:")
            st.code(stderr)
            
            
### java code
def compile_and_run_java(code):
    # Save the code to a temporary file
    with open("Main.java", "w") as file:
        file.write(code)

    # Compile the Java code
    compile_process = subprocess.Popen(["javac", "Main.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    compile_stdout, compile_stderr = compile_process.communicate()

    if compile_stderr:
        # Return compilation error if any
        return None, compile_stderr.decode()

    # Execute the compiled Java program
    run_process = subprocess.Popen(["java", "Main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = run_process.communicate()
    
    return stdout, stderr
def run_button_java(code):
    # Add a button to compile and run the code
    if st.button(":green[Compile and Run Java]"):
        stdout, stderr = compile_and_run_java(code)

        # Display the output and errors
        if stdout:
            st.subheader("Output:")
            st.code(stdout)
            st.success('Success!', icon="✅")
        else:
            st.subheader("Compilation Error:")
            st.code(stderr)
            
## upload to db
def upload_to_tempCodingQuestionsV3(question_id, data):
    collection = db.tempCodingQuestionsV3()
    title = data['title']
    exists = collection.find_one({"title": title})
    
    # return exists["Qid"]
    if exists:
        Qid = exists["Qid"]
        st.error(f'Question with the same title already exists with Qid {Qid}. Current Qid is {question_id}', icon="🚫")
        return
    else:
        data["Qid"] = question_id
        collection.insert_one(data)
        st.success('Question uploaded successfully!', icon="✅")