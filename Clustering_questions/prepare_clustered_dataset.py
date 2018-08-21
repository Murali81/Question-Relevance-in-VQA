import pickle

with open("ques_ans_pairs_train.pickle","rb") as fh:
    qa=pickle.load(fh)

answer_types={}
question_types={}

number_list=['one','two','three','four','five','six','seven','eight','nine','ten','1','2','3','4','5','6','7','8','9','10']
colors=['purple','white','yellow','cyan','indigo','magenta','black', 'orange', 'red', 'pink', 'violet', 'blue', 'green', 'brown','gray']

classification_ds=[]   # Dataset of [[question,answer,answer_type],[question,answer,answer_type]]
answers={}          # Store unique answers


answers_colors=[]   # To store answers related to colors

for tupl in qa:
    answers[tupl['multiple_choice_answer']]=answers.get(tupl['multiple_choice_answer'],0)+1


#### Detecting Color Related Answers

with open("answers_possible_object.txt",'w') as f , open("answers_possible_colors_.txt",'w') as colf:
    for ans in answers:
        flag=False
        try:
            tokens=ans.replace(",","").replace("and ","").replace("and","").split(" ")
            tokenlen=len(tokens)
            count=0
            for tokn in tokens:
                if tokn in colors:
                    count+=1

            if count==tokenlen:
                flag=True

        except:
            if ans in colors:
                flag=True

        if flag==False:print(ans,file=f)
        if flag==True:print(ans,file=colf);answers_colors.append(ans)

###############################

for tupl in qa:
    answer_type=tupl['answer_type']
    answer=tupl['multiple_choice_answer']
    if answer in answers_colors:
        answer_type='color'
    classification_ds.append([tupl['question'],answer,answer_type])

print(classification_ds[:20])

with open("classification_clusters.pickle","wb") as fh:
    pickle.dump(classification_ds,fh)

'''
Types of answers are:

1. color
2. other (object)
3. yes/no
4. number

'''
