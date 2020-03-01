import os
from sys import argv
def mk_dic(input_file):
    
    me_dic={}
    f=input_file
    for lineL in f.readlines():
        line=lineL.strip().split("\t")
        if line[0]=="ID1":
            continue
        else:
            id=line[0]

            if not id in me_dic:
                me_dic[id]=[line[1]]
            else:
                me_dic[id].append(line[1])

    print(len(me_dic))
    return me_dic
    f.close()
#============================================
def mkdif(dic_1,dic_2):
    f=open(argv[3],"wt")
    for a, b in dic_1.items():
        for c,d in dic_2.items():
            if c in b:
                f.write("ID-1"+"\t"+"ID-2"+"\t"+"ID-3"+"\n")
                for val in d:
                    f.write(a+"\t"+c+"\t"+val+"\n")
    f.close()

a=open(argv[1])
b=open(argv[2])
dic1=mk_dic(a)
dic2=mk_dic(b)
mkdif(dic1,dic2)