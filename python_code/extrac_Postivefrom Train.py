import re
import os

root_dir=r'D:\project_py\Testing Set'
#extract the seq of donor site and acceptor site
def extract_seq_of_site(file):
    #read the fasta seq from xxx.txt.The aim is to get the lin2,denoting the the site of functional site.
    with open(file) as f:
        line1=f.readline()
        line2=f.readline()
        lines = f.readlines()


        #Get the site number from the line2,the results are two list anmed donor and acceptor
        (donor,acceptor)=separate_donor_accepator(line2)
        #seq_of_site(int((donor[0])), lines)
        sumseq_donor=list_seq(donor,lines)
        sumseq_acceptor=list_seq(acceptor,lines)
    return (sumseq_donor,sumseq_acceptor)


#to get the total seq about training set
def total_sum_seq():
    dit_donor={}
    dit_acceptor={}
    with open(r'D:\project_py\bayes_donor_pos.txt','w') as f:
        for file in os.listdir(root_dir):
            filename=root_dir + "\\"+ file
            #dit_donor[i]=extract_seq_of_site(file)[0]
            #dit_acceptor[i]=extract_seq_of_site(file)[1]
            (donor,acceptor)=extract_seq_of_site(filename)
            for each in donor:
                f.write(str(each))
                f.write('\n')

    f.close()
    with open(r'D:\project_py\bayes_acceptor.txt','w') as f:
        for file in os.listdir(root_dir):
            filename = root_dir + "\\" + file
            # dit_donor[i]=extract_seq_of_site(file)[0]
            # dit_acceptor[i]=extract_seq_of_site(file)[1]
            (donor, acceptor) = extract_seq_of_site(filename)
            for each in acceptor:
                f.write(str(each))
                f.write('\n')

    f.close()






#get the number list of site from line2
def findsite(line2):
    a=re.findall(r'[0-9]+',line2.strip())
    return(a)

#To get number list about functional sites,using findsite() and line2
def separate_donor_accepator(line2):
    list1=findsite(line2)
    donor=list()
    acceptor=list()
    for i in range(2,len(list1)):
        if i%2==0:
            donor.append(list1[i-1])
        else:
            acceptor.append(list1[i-1])
    return(donor,acceptor)

#Get the seq from site
def seq_of_site(n,lines):
    i=0
    stringofsite=str()
    for line in lines:
        for each in line.strip():
            i=i+1
            if each:

                if i+9 >= n and i-9<n:
                        stringofsite=stringofsite+str(each)

    #print(stringofsite)
    return stringofsite

# iteration in donor/acceptor site
def list_seq(site,lines):
    sumseq=[]
    i=0
    for each in site:
        sumseq.append(seq_of_site(int(site[i]), lines))
        i=i+1
    return sumseq

#extract_seq_of_site('AB000381.txt')
total_sum_seq()

