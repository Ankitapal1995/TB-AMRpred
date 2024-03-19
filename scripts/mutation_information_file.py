import sys
import os
#from WHO_COMPARE import mut_annot_who
input_file=sys.argv[1]
#print(input_file)
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

#prefix=input_file.split("_")[0].split(".")[0]
fprep=[]
head,input_file=os.path.split(input_file)
#prefix=input_file.split("_")[0].split(".")[0]
if '_' in input_file:
    fprep.append(input_file.split("_")[0])
else:
    index= input_file.rfind('.')
    result_string=input_file[:index]
    fprep.append(result_string)
prefix=''.join(fprep)

#print(prefix)
path='/home/ankita/Desktop/webserver_tool/mutation/'
ml_pred_mut=[path+'46_Isoniazid_mutations.csv',path+'36_Ehambutol_mutations.csv',path+'36_Rifampicin_mutations.csv',path+'48_Streptomycin_mutations.csv',path+'224_Pyrazindamide_mutations.csv',path+'9_Kanamycin_mutations.csv',path+'6_Ethionamide_mutations.csv',path+'7_Amikacin_mutations.csv',path+'9_Ofloxacin_mutations.csv',path+'5_Moxifloxacin_mutations.csv',path+'26_Cycloserin_mutations.csv',path+'24_Pas_mutations.csv',path+'18_Capreomycin_mutations.csv']
edited_snp_file='edited_'+prefix+".csv"
#print(edited_snp_file)
final_mut_data=[]
for i in ml_pred_mut:
    final_mut_data.append(res_mut(i))
#print(final_mut_data)
drug=['INH','EMB','RIF','STM','PZA','KAN','ETH','AMI','OFLX','MXF','CYCLO','PAS','CAP']
tup=tuple(zip(final_mut_data,drug))
#print(tup)
#fo=open(prefix+"_associated_resistant_associated_mutation_files.csv","w")
#for i in 
from WHO_COMPARE import mut_annot_who
mutation_info=[]
#fo=open(prefix+"_mutation_associated_drug_resistance.csv","w")
for i in tup:
    if len(i[0])==0:
        pass
    else:
        ls=[]
        for j in i[0]:
            ls.append((mut_annot_who(j,i[1]),i[1]))
        mutation_info.append(ls)
#print(mutation_info)
#for i in mutation_info:
#    print(i)
fo=open(prefix+"_predicted_mutation_catalogue.csv","w")
for i in mutation_info:
    for j in i:
        fo.write(j[0].split("__")[0])
        fo.write("\t")
        fo.write(j[0].split("__")[1])
        fo.write("\t")
        fo.write(j[0].split("__")[2])
        fo.write("\t")
        fo.write(j[1])
        fo.write("\n")
fo.close()
