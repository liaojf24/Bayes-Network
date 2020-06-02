import re
import os
import numpy as np
import  json

# root_dir=r'C:\Users\Dell\PycharmProjects\untitled1'
# filename1=root_dir+"\\"+'donor.txt'
# filename2=root_dir+"\\"+'acceptor.txt'


#mainfile.get the probability matrix and other matrix
def probability(file):
    data_array = data_to_array(file)
    (count_base,count_base_probability)=count_base_of_file(data_array)# the number of bases in 9 positions
    count_dependent=count_dependent_base(data_array)# the number of bases of dependence
    probability_matrix=count_probability(count_base,count_dependent)
    return(probability_matrix,count_base_probability)



#calculate the probability
def count_probability(count_base,count_dependent):
    # data_array = data_to_array(file)
    # count_base = count_base_of_file(data_array) +np.ones((4,9))# the number of bases in 9 positions
    # count_dependent = count_dependent_base(data_array)  # the number of bases of dependence
    probability_matrix=np.zeros(((4,4,8)))
    # count_base=count_base_of_file(data_array)# the number of bases in 9 positions
    # count_dependent=count_dependent_base(data_array)# the number of bases of dependenc
    for i in range(8): #specify one site i
        for j in range(4):# specify row in count_dependent
            for k in range(4):
                probability_matrix[j,k,i]=(count_dependent[j,k,i]+1)/(count_base[j,i]+4)
    return(probability_matrix)




def count_base_of_file(data_array):
    sum_rows=len(data_array)
    count_base=np.zeros((4,18))# define a two-demsional array.The colom is 0~8 indicating the 9 postions.And 4 rows indicats 'a','t','g','c'
    for i in range(18):
        for j in range(sum_rows):
            if data_array[j,i]=='a':
                count_base[0,i]=count_base[0,i]+1
            elif data_array[j,i]=='t':
                count_base[1,i] =count_base[1,i] + 1
            elif data_array[j,i] == 'c':
                count_base[2,i] = count_base[2,i] + 1
            else:
                count_base[3,i] =count_base[3,i] + 1

    # calculate the probability of'atcg' at each site
    count_base_prob=np.zeros((4,18))
    for col in range(18):
        for row in range(4):
            count_base_prob[row,col]=(count_base[row,col]+1)/(4+sum_rows) #denominator+4,numerator+1.the aim is to avoid 0
    return(count_base,count_base_prob)

#calculate the probability at every site



#count the number of dependent bases
def count_dependent_base(data_array):
    sum_rows = len(data_array)
     #count_dependent is a matrix.the sequence is a,t,c,g.one-dim:(i-1),the front base;two-dim:i,the latter base;3-dim:8 postions
    count_dependent=np.zeros(((4,4,8)))
    for i in range(8):
        for j in range(sum_rows):# i represents the postion; j represents the rowth
            if data_array[j,i]=='a':
                if data_array[j,i+1]=='a':
                    count_dependent[0,0,i]+=1
                elif data_array[j,i+1]=='t':
                    count_dependent[0,1,i]+=1
                elif data_array[j,i+1]=='c':
                    count_dependent[0,2,i]+=1
                else:
                    count_dependent[0,3,i]+=1
            elif data_array[j][i]=='t':
                if data_array[j][i+1]=='a':
                    count_dependent[1,0,i]+=1
                elif data_array[j,i+1]=='t':
                    count_dependent[1,1,i]+=1
                elif data_array[j,i+1]=='c':
                    count_dependent[1,2,i]+=1
                else:
                    count_dependent[1,3,i]+=1
            elif data_array[j,i]=='c':
                if data_array[j,i+1]=='a':
                    count_dependent[2,0,i]+=1
                elif data_array[j,i+1]=='t':
                    count_dependent[2,1,i]+=1
                elif data_array[j,i+1]=='c':
                    count_dependent[2,2,i]+=1
                else:
                    count_dependent[2,3,i]+=1
            else:
                if data_array[j,i+1]=='a':
                    count_dependent[3,0,i]+=1
                elif data_array[j,i+1]=='t':
                    count_dependent[3,1,i]+=1
                elif data_array[j,i+1]=='c':
                    count_dependent[3,2,i]+=1
                else:
                    count_dependent[3,3,i]+=1
    return(count_dependent)




#count the number of bases in one line
#def number_base_of_line(lines):


#read the data,and convert the data into a dit
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

#(lines,n)=data_to_dit(filename)
#data_array=data_to_array(filename)


def out_put(filename1):
    (Pos_donor,count_base_donor_probability)=probability(filename1)
    #(Pos_acceptor,count_base_acceptor_probability) = probability(filename2)
    return(Pos_donor,count_base_donor_probability)
#print(Pos_donor)
#print(Pos_donor)

#get the data_array
#data_array=data_to_array(r'D:\project_py\bayes_donor.txt')
#
# #get the probability of each sites
# #(count_base,count_pos)=count_base_of_file(data_array)
# (count_base,count_neg)=count_base_of_file(data_array1)


# #np.savetxt(r'D:\project_py\bayes_count_pos.txt', count_pos)
# # count_pos=np.loadtxt(r'D:\project_py\bayes_count_pos.txt')
# np.savetxt(r'D:\project_py\bayes_count_neg.txt', count_neg)
#
# jsObj2 = json.dumps(count_neg)
# file2=open('D:\project_py\bayes_count_neg.json','w')
# file2.write(jsObj2)
# file2.close()

