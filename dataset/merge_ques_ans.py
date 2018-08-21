import pickle
from tqdm import tqdm

filename='val'

with open("cleaned_answers_hashes_{}.pickle".format(filename),"rb") as fh:
    answers=pickle.load(fh)

with open("cleaned_questions_hashes_{}.pickle".format(filename),"rb") as fh:
    questions=pickle.load(fh)

common_keys=['question_id','image_id']

# questions=questions[:9]

ques_ans_pairs=[]

for ques_key in tqdm(questions.keys()):
    ques=questions[ques_key]
    ans=answers[ques_key]
    qa_pair=ans.copy()
    qa_pair.update(ques)
    ques_ans_pairs.append(qa_pair)


with open("ques_ans_pairs_{}.pickle".format(filename),"wb") as fh:
    pickle.dump(ques_ans_pairs,fh)
