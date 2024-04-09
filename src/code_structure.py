import json


with open(r'C:\Users\udayr\Sproutsai\coding_question_generator\json_files\leetcode_question.json') as f:
    questions = json.load(f)

# This method below fails if the sample code has a class defined
all_structures= {}

for ques in questions:
    struct={}
    for key,val in ques['answer'].items():
        if key!='explanation':
            start=val.find('\n') if key=='python' else val.find('{')
            end=val.rfind('\n',start) if key=='python' else val.rfind('}')
            if key=='python':
                struct[str(key)]=f"{val[:start]}\n    # Your code here\n{val[end:]}"
            else:
                struct[str(key)]=f"{val[:start]}\n    // Your code here\n{val[end:]}"
    # struct[ques["Q_id"]]["sample_code"]=ques['answer']
    # struct["Q_id"]["structure"]=structure
    all_structures[ques["Q_id"]] = {"sample_code": ques['answer'],"structure": struct}

with open(r'C:\Users\udayr\Sproutsai\coding_question_generator\json_files\structures.json','w') as file:
    json.dump(all_structures, file, indent=4)