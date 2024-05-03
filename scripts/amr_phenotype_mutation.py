import sys
import subprocess
import os
input_file=sys.argv[1]
#file_path='/home/ankita/Desktop/webserver_tool/'
#output_path='/home/ankita/Desktop/webserver_tool/result/'
fprep=[]
head,input_file=os.path.split(input_file)
prefix=input_file.split("_")[0].split(".")[0]
if '_' in input_file:
    fprep.append(input_file.split("_")[0])
else:
    index= input_file.rfind('.')
    result_string=input_file[:index]
    fprep.append(result_string)
prefix=''.join(fprep)

#print(prefix)

f=prefix+"_drug_resistant_data.csv"
f2=prefix+"_predicted_mutation_catalogue.csv"
f1=open(f).readlines()
amr={}
for i in f1:
    i=i.strip("\n")
    if i.startswith("predicted"):
        pass
    else:
        amr[i.split(",")[1]]=i.split(",")[0]
#print(amr)

f2=open(f2).readlines()
mut=[]
for i in f2:
    i=i.strip("\n")
    mut.append((i.split("\t")[0],i.split("\t")[1],i.split("\t")[2],i.split("\t")[3]))
#print(mut)

mut_result={}
for item in mut:
    key=item[3]
    if key not in mut_result:
        mut_result[key]=[]
    mut_result[key].append(item[:3])
#print(mut_result)
new_mut={}
for i in mut_result:
    value=[]
    for j in mut_result[i]:
        value.append(j[0]+" ("+j[1]+")")
    new_mut[i]=value
#print(new_mut)

import pandas as pd
import csv
result_dict={}

'''for key,value in amr.items():
    result_dict[key]={}
    if value in result_dict[key]:
        result_dict[key][value].extend(mut_result.get([key,[]]))'''
for key,value in amr.items():
    if value=="R":
        result_dict[key]={value:new_mut.get(key,[])}
    else:
        result_dict[key]={value:['']}
#print(result_dict)

data=[(key,subkey,','.join(tup)) for key,subdict in result_dict.items() for subkey,tup in subdict.items()]
#print(data)

with open(prefix+"_drug_resistant_with_mutation_prediction.csv","w",newline='') as csvfile:
    csv_writer=csv.writer(csvfile)
    csv_writer.writerow(['Drugs','Predicted AMR phenotype','Predicted resistance associated mutation'])
    csv_writer.writerows(data)


subprocess.run(['rm',prefix+"_drug_resistant_data.csv",prefix+"_predicted_mutation_catalogue.csv",'edited_'+prefix+'.csv'])
#subprocess.run(['rm','edited_'+prefix+'.csv'])

