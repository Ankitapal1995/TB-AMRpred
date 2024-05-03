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

def res_mut(file_name):
    ls_file=[]
    ls_genome=[]
    common_mut=[]
    f=open(edited_snp_file).readlines()
    for i in f:
        ls_genome.append(i.strip("\n"))
    f1=open(file_name).readlines()
    for ele in f1:
        ls_file.append(ele.strip("\n"))

    for i in ls_file:
        if i in ls_genome:
           common_mut.append(i)

    return common_mut
from sys import argv
import sys
#s,input_file=argv
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
from paths_variable import m_path, mu_path, s_path
#model_path='/home/ankita/Desktop/TB-AMRpred-main/models/'
model_path=m_path
#mutation_path='/home/ankita/Desktop/TB-AMRpred-main/mutation/'
mutation_path=mu_path
#script_path='/home/ankita/Desktop/TB-AMRpred-main/scripts/'
script_path=s_path
ml_models=[(model_path+'pickle_default_new_version_3512_3512_iso_res_sus_5511_mut_matrix_train_for_ml.csv',mutation_path+'45_iso_res_mut_xgboost_cut_off_name.csv',prefix+"_iso_ml.csv","inh"),(model_path+'pickle_default_new_version_1500_1500_ethamb_res_sus_pure_3185_mut_matrix_train_for_ml.csv',mutation_path+'105_ethamb_imp_res_mut_combined_score.csv',prefix+"_ethamb_ml.csv","emb"),(model_path+'pickle_default_new_version_2750_2750_rifam_res_full_sus_5030_mut_matrix_train_for_ml.csv',mutation_path+'55_combined_xgb_shap_rifam_res_mut.csv',prefix+'_rifam_ml.csv',"rif"),(model_path+'pickle_default_new_version_1500_1500_res_sus_2832_mut_prof_for_ml.csv',mutation_path+'60_xgb_ann_shap_strep_combind_mutation_list.csv',prefix+"_strep_ml.csv","stm"),(model_path+'pickle_default_new_version_1500_1500_pyrzmd_res_sus_5964_mut_prof_for_ml.csv',mutation_path+'224_pza_imp_res_mut_combined_ann_xgb_name.csv',prefix+'_pyrzmd_ml.csv',"pza"),(model_path+'pickle_default_new_version_500_500_kana_res_sus_3552_mut_prof_for_ml.csv',mutation_path+'27_kana_res_imp_mut_combined_shap_xgb.csv',prefix+'_kana_ml.csv',"kan"),(model_path+'pickle_default_new_version_1076_1076_ethion_res_sus_21619_mut_matrix_train_for_ml.csv',mutation_path+'49_ethion_imp_res_mut_xgb_for_prediction_name.csv',prefix+'_ethion_ml.csv',"eth"),(model_path+'pickle_default_new_version_350_350_amk_res_sus_13437_mut_prof_for_ml.csv',mutation_path+'11_xgb_ann_amk_imp_res_mut_name.csv',prefix+'_amk_ml.csv',"ami"),(model_path+'pickle_default_new_version_959_959_oflx_res_sus_14333_mut_matrix_train_for_ml.csv',mutation_path+'34_ofloxacin_xgb_prediction_imp_mutation_name.csv',prefix+'_oflox_ml.csv',"oflox"),(model_path+'pickle_default_new_version_242_242_mox_res_sus_18122_mut_matrix_train_for_ml.csv',mutation_path+'18122_mox_res_sus_mut.csv',prefix+'_mox_ml.csv',"mox"),(model_path+'pickle_default_new_version_100_100_cyclo_res_sus_3518_mut_prof_for_ml.csv',mutation_path+'26_combined_ann_xgb_cyclo_imp_res_mut.csv',prefix+'_cyclo_ml.csv',"cyclo"),(model_path+'pickle_default_new_version_90_90_res_sus_5287_mut_prof_for_ml.csv',mutation_path+'40_combined_ann_xgb_pas_imp_mut.csv',prefix+'_pas_ml.csv',"pas"),(model_path+'pickle_default_new_version_400_400_cap_res_sus_2289_mut_prof_for_ml.csv',mutation_path+'20_imp_cap_res_mut_combined_xgb_shap.csv',prefix+'_cap_ml.csv',"cap")]
#ml_models=[(model_path+'pickle_default_new_version_1500_1500_pyrzmd_res_sus_5964_mut_prof_for_ml.csv',mutation_path+'224_pza_imp_res_mut_combined_ann_xgb_name.csv',prefix+'_pyrzmd_ml.csv',"pza")]
t1=time.time()

def ml_predict(input_f,input_f2=None):
    print(input_f)
    print(input_f2)
    #if input_f2 is None:
    #    print("input file is one")
    #else:
    #    print("input files are two")
    if input_f2 is None:
        input_f=os.path.join(head, input_f)
        print(input_f)
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
        subprocess.run(['python',script_path+'cp_both_ann_xgb_model_for_amr_prediction_testing_with_cutoff.py',i[0],i[2],i[3]])
        #print(i[4]+"prediction done")
        print(i[3].upper()+"-------done")
        fo=open(prefix+".csv_"+i[3]+"_xgb_prediction.csv","r")
        print(f'final file fetching---{prefix+".csv_"+i[3]+"_xgb_prediction.csv"}')
        for line in fo:
               ls.append(line.strip("\n"))
               ls.append(res_mut(i[1]))
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
        if i[0].split("\t")[1]=="mox":
            final_file.write('MXF')
        else:
            final_file.write(i[0].split("\t")[1].upper())
        #final_file.write("\t")
        #final_file.write((',').join(i[1]))
        final_file.write("\n")
    final_file.close()
    return final_file

if len(input_ls)==3:
    ml_predict(input_ls[1],input_ls[2])
else:
    ml_predict(input_ls[1])
subprocess.run(['rm',prefix+"_rifam_ml.csv",prefix+"_iso_ml.csv",prefix+"_ethamb_ml.csv",prefix+"_strep_ml.csv",prefix+"_pyrzmd_ml.csv",prefix+"_pas_ml.csv",prefix+"_oflox_ml.csv",prefix+"_mox_ml.csv",prefix+"_kana_ml.csv",prefix+"_ethion_ml.csv",prefix+"_cyclo_ml.csv",prefix+"_cap_ml.csv",prefix+"_amk_ml.csv",prefix+".csv_inh_xgb_prediction.csv",prefix+".csv_emb_xgb_prediction.csv",prefix+".csv_rif_xgb_prediction.csv",prefix+".csv_stm_xgb_prediction.csv",prefix+".csv_pza_xgb_prediction.csv",prefix+".csv_kan_xgb_prediction.csv",prefix+".csv_eth_xgb_prediction.csv",prefix+".csv_ami_xgb_prediction.csv",prefix+".csv_oflox_xgb_prediction.csv",prefix+".csv_mox_xgb_prediction.csv",prefix+".csv_cyclo_xgb_prediction.csv",prefix+".csv_pas_xgb_prediction.csv",prefix+".csv_cap_xgb_prediction.csv"])
t2=time.time()
print(f'time taken:{t2-t1}')
