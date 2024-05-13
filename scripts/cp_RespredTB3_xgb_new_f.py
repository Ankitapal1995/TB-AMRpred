from sys import argv
import os
import subprocess
import time
#from contextlib import contextmanager
#import sys, os
from contextlib import contextmanager
import multiprocessing as mp
import sys, os
import argparse

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
suppress_stdout()

from sys import argv
import sys
#s,input_file=argv
################################### input file preparation ############################
input_ls=sys.argv
input_file=input_ls[1]
fprep=[]
#prefix=input_file.split("_")[0].split(".")[0]
head,input_file=os.path.split(input_file)
if '_' in input_file:
    fprep.append(input_file.split("_")[0])
else:
    index= input_file.rfind('.')
    result_string=input_file[:index]
    fprep.append(result_string)
prefix=''.join(fprep)
#print(input_file)
#print(prefix)
#print(input_file)
#print(os.path.join(head, input_file))
prefix=''.join(fprep)
#print(prefix)

#prefix=input_file.split(".")[0]
outdir =prefix+"_dir"
out = prefix+"_snp.csv"
snp_file=prefix+'.csv'
edited_snp_file='edited_'+prefix+".csv"
#print(snp_file)
#print(edited_snp_file)
#dl_file=prefix+".csv_dl_file"
#ml_file = prefix+".csv_ml_file"
################################## adding all file path ###################################
from paths_variable import m_path, mu_path, s_path
#model_path='/home/ankita/Desktop/TB-AMRpred-main/models/'
model_path=m_path
#mutation_path='/home/ankita/Desktop/TB-AMRpred-main/mutation/'
mutation_path=mu_path
#script_path='/home/ankita/Desktop/TB-AMRpred-main/scripts/'
script_path=s_path


################################# loading all the models for prediction ####################
ml_models=[(model_path+'pickle_inh_model.csv',prefix+"_inh_ml.csv","inh"),(model_path+'pickle_emb_model.csv',prefix+"_emb_ml.csv","emb"),(model_path+'pickle_rif_model.csv',prefix+'_rif_ml.csv',"rif"),(model_path+'pickle_stm_model.csv',prefix+"_stm_ml.csv","stm"),(model_path+'pickle_pza_model.csv',prefix+'_pza_ml.csv',"pza"),(model_path+'pickle_kan_model.csv',prefix+'_kan_ml.csv',"kan"),(model_path+'pickle_eth_model.csv',prefix+'_eth_ml.csv',"eth"),(model_path+'pickle_ami_model.csv',prefix+'_ami_ml.csv',"ami"),(model_path+'pickle_oflx_model.csv',prefix+'_oflx_ml.csv',"oflx"),(model_path+'pickle_mxf_model.csv',prefix+'_mxf_ml.csv',"mxf"),(model_path+'pickle_cyclo_model.csv',prefix+'_cyclo_ml.csv',"cyclo"),(model_path+'pickle_pas_model.csv',prefix+'_pas_ml.csv',"pas"),(model_path+'pickle_cap_model.csv',prefix+'_cap_ml.csv',"cap")]

#ml_models=[(model_path+'pickle_default_new_version_1500_1500_pyrzmd_res_sus_5964_mut_prof_for_ml.csv',mutation_path+'224_pza_imp_res_mut_combined_ann_xgb_name.csv',prefix+'_pyrzmd_ml.csv',"pza")]
t1=time.time()


################################### AMR prediction ##################################

def ml_predict(input_f,input_f2=None):
    #print(input_f)
    #print(input_f2)
    #if input_f2 is None:
    #    print("input file is one")
    #else:
    #    print("input files are two")
    if input_f2 is None:
        input_f=os.path.join(head, input_f)
        #print(input_f)
        subprocess.run(['snippy','--ref',script_path+'AL123456_h37rv.gb','--ctgs',input_f,'--prefix',prefix,'--outdir',".","--force","--cpus","20"])
    else:
        input_f=os.path.join(head, input_f)
        input_f2=input_f=os.path.join(head, input_f2)
        subprocess.run(['snippy','--ref',script_path+'AL123456_h37rv.gb','--R1',input_f,'--R2',input_f2,'--prefix',prefix,'--outdir',".","--force","--cpus","20"])
    ls=[prefix+".bam",prefix+".bam.bai",prefix+".raw.vcf",prefix+".filt.vcf",prefix+".vcf",prefix+".tab",prefix+".subs.vcf",prefix+".vcf.gz",prefix+".vcf.gz.csi",prefix+".consensus.fa",prefix+".consensus.subs.fa",prefix+".log",prefix+".aligned.fa",prefix+".txt",prefix+".html",prefix+".gff",prefix+".bed"]
 
    for i in ls:
       subprocess.run(['rm',i])

    #subprocess.run(['python',script_path+'ai_file_creater.py',snp_file])
    subprocess.run(['python',script_path+'mut_analyzer.py',snp_file])
    subprocess.run(['python',script_path+'cp_ai_file_creater.py',edited_snp_file])
    final_multi_class_data=[]
    for i in ml_models:
        ls=[]
        #print(i[4]+"models")
        subprocess.run(['python',script_path+'cp_both_ann_xgb_model_for_amr_prediction_testing_with_cutoff.py',i[0],i[1],i[2]])
        #print(i[4]+"prediction done")
        print(i[2].upper()+"-------done")
        fo=open(prefix+".csv_"+i[2]+"_xgb_prediction.csv","r")
        #print(f'final file fetching---{prefix+".csv_"+i[2]+"_xgb_prediction.csv"}')
        for line in fo:
               ls.append(line.strip("\n"))
               #ls.append(res_mut(i[1]))
        final_multi_class_data.append(ls)
    #filepath='/home/ankita/Desktop/webserver_tool/result/'
    #print(f'this is the final prefix value:{prefix}')
    output=prefix+"_drug_resistant_data.csv"
    #print(f'this is final output file {output}')
    #final_file=open(prefix+"_drug_resistant_data.csv","w")
    final_file=open(output,'w')
    final_file.write('predicted phenotype')
    final_file.write(",")
    final_file.write("drug")
    #final_file.write("\t")
    #final_file.write("Predicted resistant mutations")
    final_file.write("\n")
    for i in final_multi_class_data:
        final_file.write(i[0].split("\t")[0])
        final_file.write(",")
        final_file.write(i[0].split("\t")[1].upper())
        #final_file.write("\t")
        #final_file.write((',').join(i[1]))
        final_file.write("\n")
    final_file.close()
    return final_file

################# executing AMR prediction function ########################

if len(input_ls)==3:
    ml_predict(input_ls[1],input_ls[2])
else:
    ml_predict(input_ls[1])

############################### deleting all the temp file ##################
subprocess.run(['rm',prefix+"_rif_ml.csv",prefix+"_inh_ml.csv",prefix+"_emb_ml.csv",prefix+"_stm_ml.csv",prefix+"_pza_ml.csv",prefix+"_pas_ml.csv",prefix+"_oflx_ml.csv",prefix+"_mxf_ml.csv",prefix+"_kan_ml.csv",prefix+"_eth_ml.csv",prefix+"_cyclo_ml.csv",prefix+"_cap_ml.csv",prefix+"_ami_ml.csv",prefix+".csv_inh_xgb_prediction.csv",prefix+".csv_emb_xgb_prediction.csv",prefix+".csv_rif_xgb_prediction.csv",prefix+".csv_stm_xgb_prediction.csv",prefix+".csv_pza_xgb_prediction.csv",prefix+".csv_kan_xgb_prediction.csv",prefix+".csv_eth_xgb_prediction.csv",prefix+".csv_ami_xgb_prediction.csv",prefix+".csv_oflx_xgb_prediction.csv",prefix+".csv_mxf_xgb_prediction.csv",prefix+".csv_cyclo_xgb_prediction.csv",prefix+".csv_pas_xgb_prediction.csv",prefix+".csv_cap_xgb_prediction.csv"])


############################# analyzing resistance associated mutation ########################
def res_mut(file_name):
    ls_file=[]
    ls_genome=[]
    common_mut=[]
    f=open(edited_snp_file).readlines()
    for i in f:
        ls_genome.append(i.strip("\n"))
    f1=open(file_name).readlines()
    for ele in f1:
        ele=ele.strip("\n")
        ls_file.append([ele.split("\t")[0],ele.split("\t")[1],ele.split("\t")[2]])
    for i in ls_file:
        if i[0] in ls_genome:
           common_mut.append([i[1],i[2]])

    return common_mut

########################### loading all the predicted mutations highly relevant to drug resistance #############################
ml_pred_mut=[mu_path+"Isoniazid_mutation_comparison_WHO.csv",mu_path+"Ethambutol_mutation_comparison_WHO.csv",mu_path+"Rifampicin_mutation_comparison_WHO.csv",mu_path+"Streptomycin_mutation_comparison_WHO.csv",mu_path+"Pyrazinamide_mutation_comparison_WHO.csv",mu_path+"Kanamycin_mutation_comparison_WHO.csv",mu_path+"Ethionamide_mutation_comparison_WHO.csv",mu_path+"Amikacin_mutation_comparison_WHO.csv",mu_path+"Ofloxacin_mutation_comparison_WHO.csv",mu_path+"Moxifloxacin_mutation_comparison_WHO.csv",mu_path+"Cycloserin_mutation_comparison_WHO.csv",mu_path+"PAS_mutation_comparison_WHO.csv",mu_path+"Capreomycin_mutation_comparison_WHO.csv"]
#edited_snp_file='edited_'+prefix+".csv"
#print(edited_snp_file)
final_mut_data=[]
for i in ml_pred_mut:
    final_mut_data.append(res_mut(i))
#print(final_mut_data)
drug=['INH','EMB','RIF','STM','PZA','KAN','ETH','AMI','OFLX','MXF','CYCLO','PAS','CAP']
tup=tuple(zip(final_mut_data,drug))
#print(tup)
mutation_info=[]
for i in tup:
    if len(i[0])==0:
        pass
    else:
        ls=[]
        ls.append(('; '.join(str('__'.join(v)) for v in i[0]),i[1]))
        mutation_info.append(ls)
    #print(mutation_info)


fo=open(prefix+"_predicted_mutation_catalogue.csv","w")
for i in mutation_info:
    for j in i:
        #print(j[0])
        for k in j[0].split(";"):
            if k.split("__")[1]=='Assoc w R':
                fo.write(k.split("__")[0])
            else:
                fo.write(k.split("__")[0])
            fo.write("\t")
            fo.write("Predicted")
            fo.write("\t")
            fo.write("mutation")
            fo.write("\t")
            fo.write(j[1])
            fo.write("\n")

fo.close()


######################### combining AMR prediction and predicted resistance associated mutations ########################################

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
        value.append(j[0])
    new_mut[i]=value
#print(new_mut)

import pandas as pd
import csv
result_dict={}

for key,value in amr.items():
    if value=="R":
        result_dict[key]={value:new_mut.get(key,[])}
    else:
        result_dict[key]={value:['']}
#print(result_dict)

data=[(key,subkey,';'.join(tup)) for key,subdict in result_dict.items() for subkey,tup in subdict.items()]
#print(data)

#####################################  final file prepararion ################################################

with open(prefix+"_drug_resistant_with_mutation_prediction.csv","w",newline='') as csvfile:
    csv_writer=csv.writer(csvfile)
    csv_writer.writerow(['Drugs','Predicted AMR phenotype','Predicted resistance associated mutation'])
    csv_writer.writerows(data)
subprocess.run(['rm',prefix+"_drug_resistant_data.csv", prefix+"_predicted_mutation_catalogue.csv",'edited_'+prefix+'.csv',prefix+'.csv'])

t2=time.time()
print(f'time taken:{t2-t1}')
