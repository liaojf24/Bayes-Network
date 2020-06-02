import get_probability as pro
import tree_model as TM
import json
import numpy as np

#get coupled nodes
couples=list()#start-stop pairs nodes
pair=list()
for node in TM.MST:
    pair=(node[0],node[1])
    couples.append(pair)

#load json in
fileobject1=open('D:\project_py\pairs_pos.json')
Mt=json.load(fileobject1)
fileobject1.close()
fileobject2=open('D:\project_py\pairs_neg.json')
Mf=json.load(fileobject2)
fileobject2.close()
# print(Mt['-9-3'])


#get the data_array
count_pos=np.loadtxt(r'D:\project_py\bayes_count_pos.txt')
count_neg=np.loadtxt(r'D:\project_py\bayes_count_neg.txt')

# count_pos=pro.count_base_prob_pos
# count_neg=pro.count_base_prob_neg


def scores_for_a_string(MT,MF,count_pos,count_neg,string):
    scores_MT=cal_pro_M(MT,count_pos,string)
    scores_MF=cal_pro_M(MF, count_neg, string)
    P_value=scores_MT/scores_MF
    return (P_value)


#calculate the probability using Model
def cal_pro_M(M,count_base_prob,string):
    string=list(string.lower())#convert str into a list
    p=cal_stable_pro(count_base_prob,string)      #calculate the stable value in +1,+2 nodes
    for couple in couples:
        key=''.join(couple)#key to index 2-D list
        start=int(couple[0])+9
        stop=int(couple[1])+9
        if string[start]=='a':
            if string[stop]=='a':
                p=p*M[key][0][0][0]
            elif string[stop]=='t':
                p = p * M[key][0][0][1]
            elif string[stop]=='c':
                p = p * M[key][0][0][2]
            else:
                p = p * M[key][0][0][3]
        elif string[start]=='t':
            if string[stop]=='a':
                p=p*M[key][0][1][0]
            elif string[stop]=='t':
                p = p * M[key][0][1][1]
            elif string[stop]=='c':
                p = p * M[key][0][1][2]
            else:
                p = p * M[key][0][1][3]
        elif string[start]=='c':
            if string[stop]=='a':
                p=p*M[key][0][2][0]
            elif string[stop]=='t':
                p = p * M[key][0][2][1]
            elif string[stop]=='c':
                p = p * M[key][0][2][2]
            else:
                p = p * M[key][0][2][3]
        else:
            if string[stop]=='a':
                p=p*M[key][0][3][0]
            elif string[stop]=='t':
                p = p * M[key][0][3][1]
            elif string[stop]=='c':
                p = p * M[key][0][3][2]
            else:
                p = p * M[key][0][3][3]
    return(p)

def cal_stable_pro(count_base_prob,string):
    x=string[10]
    y=string[11]
    if x=='a':
        p=count_base_prob[0,10]
    elif x=='t':
        p=count_base_prob[1, 10]
    elif x=='c':
        p=count_base_prob[2, 10]
    else:
        p=count_base_prob[3, 10]

    if y == 'a':
        p = p*count_base_prob[0, 11]
    elif y == 't':
        p = p*count_base_prob[1, 11]
    elif y == 'c':
        p = p*count_base_prob[2, 11]
    else:
        p = p*count_base_prob[3, 11]
    return (p)

# P=scores_for_a_string(Mt,Mf,count_pos,count_neg,'GGAAAGAAGATGGCAGGG')
# print(P)
def score_for_file(file):
    f=open(file,'r')
    lines=f.readlines()
    rows = len(lines)
    scores_pos=np.zeros((rows,2))##np.ones((rows,2)) denotes the positive data
    i=0
    for line in lines:
        if len(line.strip())==18:
            P = scores_for_a_string(Mt, Mf, count_pos, count_neg, line.strip())
            scores_pos[i,0]=P
            i=i+1
    return(scores_pos)

bayes_score_test_neg=score_for_file(r'D:\project_py\bayes_test_neg.txt')
np.savetxt(r'D:\project_py\bayes_s_neg.csv', bayes_score_test_neg,fmt='%f',delimiter=',')