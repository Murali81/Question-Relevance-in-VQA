import json
from tqdm import tqdm


filename='val'

with open('v2_OpenEnded_mscoco_{}2014_questions.json'.format(filename)) as f:
    data = json.load(f)



attributes=['image_id','question','question_id']

common_keys=['question_id','image_id']

revised_tupls=[]        # List , where each instance is a Dictionary with attributes as keys and info as values.
revised_tupls_hashs={}    # Dictionary with "question_id and image_id" as key and "attributes with info" as values

for tupl in tqdm(data['questions']):

    local_dict={}
    for attr in attributes:
        local_dict[attr]=tupl[attr]
    revised_tupls.append(local_dict)
    revised_tupls_hashs[str(tupl[common_keys[0]])+" "+str(tupl[common_keys[1]])] = local_dict

import pickle
with open("cleaned_questions_{}.pickle".format(filename),"wb") as fh:
    pickle.dump(revised_tupls,fh)

with open("cleaned_questions_hashes_{}.pickle".format(filename),"wb") as fh:
    pickle.dump(revised_tupls_hashs,fh)
