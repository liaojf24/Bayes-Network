import tree_model as TM
import get_chi_donor as chi
import get_probability
from collections import defaultdict
import json

import numpy as np
#get coupled nodes
pairs=list()#start-stop pairs nodes
pair=list()
for node in TM.MST:
    pair=(node[0],node[1])
    pairs.append(pair)
# print(pairs)

#get the data_array
data_array=chi.data_to_array(r'D:\project_py\bayes_donor.txt')
data_array1=chi.data_to_array(r'D:\project_py\bayes_neg_18.txt')
#get the dependence probability between i-th and j-th position
def depend_pro(i,j,array):

    #the label in contingency is 0,1,2,3,4...17
    contingency=chi.get_contingency(i,j,array)
    E_row = contingency.sum(axis=1)#calculate the sum of 4 rows

    dependence_pro=list()#dependence_pro is 2-D list
    wait_pro=list()
    for k in range(4):
        for m in range(4):
            if E_row[m]:
                wait_pro.append(contingency[k,m]/E_row[k])
            else:
                wait_pro.append(0)
            if m==3:
                dependence_pro.append(wait_pro)
                wait_pro = list()
            # dependence_pro[i,j]=contingency[i,j]/E_row[i]
    return(dependence_pro)


#get all dependence probability about pairs
def pairs_depend(pairs,array):
    pairs_dependence=defaultdict(list) #containing all the pairs dependent
    for pair in pairs:
        dependence_pro=depend_pro(int(pair[0])+9, int(pair[1])+9, array)
        key=''.join(pair)
        pairs_dependence[key].append(dependence_pro)
    return(pairs_dependence)

# pairs_dependence_pos=pairs_depend(pairs,data_array)

pairs_dependence_neg=pairs_depend(pairs,data_array1)
# (count_base,count_base_prob_pos)=get_probability.count_base_of_file(data_array)
# (count_base,count_base_prob_neg)=get_probability.count_base_of_file(data_array1)

# jsObj1 = json.dumps(pairs_dependence_pos)
# fileObject1 = open('D:\project_py\pairs_pos.json', 'w')
# fileObject1.write(jsObj1)
# fileObject1.close()

jsObj2 = json.dumps(pairs_dependence_neg)

fileObject2 = open('D:\project_py\pairs_neg.json', 'w')
fileObject2.write(jsObj2)
fileObject2.close()

# dependence_pro=depend_pro(-9,-3,data_array)
# print(dependence_pro)


