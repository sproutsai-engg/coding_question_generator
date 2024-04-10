import json
with open(r'C:\Users\udayr\Sproutsai\coding_question_generator\src\coding_q_gen.json') as f:
    question_descriptions = json.load(f)

with open(r'C:\Users\udayr\Sproutsai\coding_question_generator\json_files\call_functions.json') as f:
    call_functions = json.load(f)

with open(r'C:\Users\udayr\Sproutsai\coding_question_generator\json_files\structures.json') as f:
    structures = json.load(f)

# print(question_descriptions["20"])
# print(call_functions["20"])
# print(structures["20"])

def valid_key(ques_id,object):
    if ques_id in object.keys() and object[ques_id] is not None:
        return True
    
all_questions={}
for key in call_functions.keys():
    if valid_key(key,question_descriptions) and valid_key(key,call_functions) and valid_key(key,structures):
        all_questions[key]={"Q_id":key,"title":question_descriptions[key]["title"],"description":question_descriptions[key]["description"],"example":question_descriptions[key]["example"],"level":question_descriptions[key]["level"],"tags":question_descriptions[key]["tags"],"sample_code":structures[key]["sample_code"],"test_cases":question_descriptions[key]["test_cases"],"structure":structures[key]["structure"],"call_functions":call_functions[key]["call_functions"]}

with open(r'C:\Users\udayr\Sproutsai\coding_question_generator\json_files\all_questions.json','w') as file:
    json.dump(all_questions, file, indent=4)
