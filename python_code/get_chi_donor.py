import re
import os
import numpy as np

#get the chi table of donor.txt
def chi_table(file):
    data_array=data_to_array(file)

    chi_chart=np.zeros((18,18))
    for i in range(18):
        for j in range(18):
            chi_chart[i,j]=get_chi(i,j,data_array)
    return(chi_chart)

#define dependence according to chi_chart
def dependence_from_chi(chi_chart):
    dependence_chart=np.zeros((18,18))
    for i in range(18):
        for j in range(18):
            if chi_chart[i, j]<55.4491:
                dependence_chart[i,j]=0
            else:
                dependence_chart[i, j] =chi_chart[i,j]

    return(dependence_chart)

#get the value of chi between position i and position j
# def total_chi(file):
#     data_array=data_to_array(file)
#     contingency_i_and_j==get_contingency(i,j,data_array)
def get_chi(i,j,data_array):
    chi=0
    contingency_i_and_j=get_contingency(i,j,data_array)
    E_row=contingency_i_and_j.sum(axis=1)#calculate the sum of 4 rows
    E_col=contingency_i_and_j.sum(axis=0)#calculate the sum of 4 cols
    Y=sum(E_row)

    for m in range(4):
        for n in range(4):
            E_mn=E_row[m]*E_col[n]/Y
            if E_mn:
                chi+=np.square(contingency_i_and_j[m,n]-E_mn)/E_mn
    return(chi)

def get_contingency(i,j,data_array):
    sum_rows = len(data_array)
    contingency_table=np.zeros((4,4))
    for k in range(sum_rows):# i represents the postion; j represents the rowth
        if data_array[k,i]=='a':
            if data_array[k,j]=='a':
                contingency_table[0,0]+=1
            elif data_array[k,j] == 't':
                contingency_table[0,1] += 1
            elif data_array[k, j] == 'c':
                contingency_table[0, 2] += 1
            else:
                contingency_table[0,3]+=1

        elif data_array[k, i] == 't':
            if data_array[k, j] == 'a':
                contingency_table[1, 0] += 1
            elif data_array[k, j] == 't':
                contingency_table[1, 1] += 1
            elif data_array[k, j] == 'c':
                contingency_table[1, 2] += 1
            else:
                contingency_table[1, 3] += 1

        elif data_array[k, i] == 'c':
            if data_array[k, j] == 'a':
                contingency_table[2, 0] += 1
            elif data_array[k, j] == 't':
                contingency_table[2, 1] += 1
            elif data_array[k, j] == 'c':
                contingency_table[2, 2] += 1
            else:
                contingency_table[2, 3] += 1

        else :
            if data_array[k, j] == 'a':
                contingency_table[3, 0] += 1
            elif data_array[k, j] == 't':
                contingency_table[3, 1] += 1
            elif data_array[k, j] == 'c':
                contingency_table[3, 2] += 1
            else:
                contingency_table[3, 3] += 1
    return (contingency_table)


# convert .txt into a data array
def data_to_array(file):
    data_array=[]
    with open(file)as f:
        lines=f.readlines()
        for line in lines:
            data1=line.strip().lower()
            data2=list(data1)
            data_array.append(data2)
    data_array=np.array(data_array)
    return(data_array)

chi_chart=chi_table(r'D:\project_py\bayes_donor.txt')
dependence_chart=dependence_from_chi(chi_chart)


if __name__ == '__main__':
    sumrows=list(chi_chart.sum(axis=1))
    print(sumrows.index(max(sumrows)))
#print(dependence_chart)


