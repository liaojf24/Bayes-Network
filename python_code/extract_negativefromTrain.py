import re
import os

root_dir=r'D:\project_py\Testing Set'

#extract negative from Training Set
def total_sum_negative_data():
    dit_negative={}
    with open(r'D:\project_py\bayes_test_neg.txt','w') as f:
        for file in os.listdir(root_dir):
            filename=root_dir + "\\"+ file
            list_of_string=extract_negative_seq(filename)
            for each in list_of_string:
                f.write(str(each))
                f.write('\n')

    f.close()

# extract negative data from one file--main file
def extract_negative_seq(file):
    #f=open(file, "r")
    with open(file) as f:
        line1 = f.readline()
        line2 = f.readline()
        lines=f.readlines()

    # get the loaction of functional site
        loaction_of_functional_site = findsite(line2) #loaction_of_functional_site is a number list
        list_of_string=seq_of_site(loaction_of_functional_site,lines)
    return (list_of_string)


# get the number list of site from line2
def findsite(line2):
    a = re.findall(r'[0-9]+', line2.strip())
    return (a)

# get the seq (9 bases) at a specific site except for loaction_of_functional_site.Get the negative data.
def seq_of_site(loaction_of_functional_site,lines):
    j=0
    i=0
    wait_list=list()
    string=str()
    list_of_string=list() # a list containing all the negative string from a fasta file
    (list_of_seq)=sum_bases_seq(lines)
    for i in range(len(list_of_seq)-18):

        if (i+9) not in loaction_of_functional_site:
            for j in range(18):
                wait_list.append(list_of_seq[i+j])
            # make j=0 and string is null, to prepare for next string assignment
            string=''.join(wait_list)
            list_of_string.append(string)
            string=str()
            wait_list=[]
    return(list_of_string)


# count the total bases from one sequence
def sum_bases_seq(lines):
    sum=0
    list_sum_seq=list()
    for line in lines:
        for each in line.strip():
            if each:
                list_sum_seq.append(each)

    return(list_sum_seq)

#filename=root_dir + "\\"+ 'AB000381.txt'

#(list_of_string)=extract_negative_seq(filename)
#print(list_of_string)
#print(b)
total_sum_negative_data()
