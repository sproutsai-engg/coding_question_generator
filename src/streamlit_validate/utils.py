import sys
sys.path.append('../../src')
import json
import subprocess
import streamlit as st
import streamlit_validate.db as db
from bson import ObjectId



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
    run_process = subprocess.run(["java", "Main"],capture_output=True,text=True)
    stdout, stderr =  run_process.stdout, run_process.stderr
    
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
def upload_coding_question_to_db(_id, question_id, data, file_path):
    question_data = data[question_id]
    if _id is None:
        collection = db.toyCodingQuestions
        id = collection.insert_one(question_data)
        question_data["_id"] = str(id.inserted_id)
        save_json_file(file_path, data)
        st.success('Question uploaded successfully!', icon="✅")
    else:
        collection = db.toyCodingQuestions
        exists = collection.find_one({"_id": ObjectId(_id)})

        if exists:
            question_data["_id"] = ObjectId(_id)
            collection.update_one({"_id": ObjectId(_id)}, {"$set": question_data})
            st.success('Question updated successfully!', icon="✅")
            # st.error(f'Question with the same title already exists with Qid {Qid}. Current Qid is {question_id}', icon="🚫")
        else:
            question_data["_id"] = ObjectId(_id)
            collection.insert_one(question_data)
            st.success('Question uploaded successfully!', icon="✅")
        
def update_to_tempCodingQuestionsV3(question_id, data):
    collection = db.tempCodingQuestionsV3()
    title = data['title']
    exists = collection.find_one({"title": title})
    if exists:
        id = exists["_id"]
        collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        st.success('Question updated successfully!', icon="✅")
    else:
        st.error('Question not found! Please upload the question first.', icon="🚫")



### run javascript code

def run_javascript(code):
    # Save the code to a temporary file
    with open("script.js", "w") as file:
        file.write(code)

    # Execute the JavaScript code
    run_process = subprocess.run(["node", "script.js"],capture_output=True,text=True)
    stdout, stderr = run_process.stdout, run_process.stderr

    return stdout, stderr

def run_button_javascript(code):
    # Add a button to run the JavaScript code
    if st.button(":yellow[Run JavaScript]"):
        stdout, stderr = run_javascript(code)

        # Display the output and errors
        if stdout:
            st.subheader("Output:")
            st.code(stdout)
            st.success('Success!', icon="✅")
        else:
            st.subheader("Error:")
            st.code(stderr)
