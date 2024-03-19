from sys import argv
s,filename=argv
f1=open(filename,"r").readlines()
all_mutation=[]
for m in f1:
    m=m.strip("\n")
    all_mutation.append(m)
print(all_mutation)
#for i in all_mutation:
#    print(i)
#f2=open(filename,"r").readlines()
'''cds=[]
non_cds=[]
for i in f1:
    i=i.strip("\n")
    l=i.split(",")
    if "CDS" in l:
        if len(l)==14:
            cds.append(','.join(l[-4:-1]))
        elif len(l)>14:
            cds.append(','.join(l[-(4+(len(l)-14)):-((len(l)-14)+1)]))
    else:
        cds.append(','.join(l[1:]))
#print(cds)
genome=[]
masterfile=[]'''
path='/home/ankita/Desktop/webserver_tool/mutation/'
mut_file_list=[path+'5511_iso_res_mut.csv',path+'3185_ethamb_res_mut.csv',path+'5030_rifam_res_mut.csv',path+'2832_strep_res_mut.csv',path+'5964_pyrzmd_res_mut.csv',path+'3552_kana_res_mut.csv',path+'21619_ethion_res_mut.csv',path+'14333_oflox_res_mut.csv',path+'18122_mox_res_sus_mut.csv',path+'3518_cyclo_res_mut.csv',path+'5287_pas_res_mut.csv',path+'13437_amk_res_mut.csv',path+'2289_cap_res_mut.csv']
#mut_file_list=[path+'2289_cap_res_mut.csv']
#for i in cds:
#    genome.append(''.join(i.split(" ")[2:]))

#print(len(genome))
def ml_file_creater(f):
    mut_list=[]
    common_list=[]
    f1=open(f).readlines()
    for i in f1:
        i=i.strip("\n")
        mut_list.append(i)
    #print(len(mut_list))
    ls=['1' if i in all_mutation else '0' for i in mut_list]
    mut_n=['f'+str(i) for i in range(len(mut_list))]
    mut_n.append('label')
    ls.append('1')
    prepf=[]
    if filename.count('.')==2:
        prepf.append('.'.join(filename[7:].split(".")[:2]))
    else:
        prepf.append('.'.join(filename[7:].split(".")[:1]))

    result_string=''.join(prepf)
    #print(ls)
    #print(result_string)
    fo=open(result_string+"_"+f.split("/")[-1].split("_")[1]+"_ml.csv","w")
    fo.write(','.join(mut_n))
    fo.write("\n")
    fo.write(','.join(ls))
    fo.close()
    #fi=open(filename+"_"+f.split("_")[1]+"_dl.csv",'w')
    #fi.write(','.join(ls))
    #fi.close()


for i in mut_file_list:
    ml_file_creater(i)
