def mut_annot_who(mut,k):
    mut=str(mut)
    from cp_non_cds_mutations_annotation import non_cds_annot
    file=open("/home/ankita/Desktop/webserver_tool/scripts/WHO_MUTATION_CATALOGUE.csv","r").readlines()
    who_mut=[]
    who_mut_pos=[]
    who_mut_confi=[]
    for line in file:
        if k in line.split(","):
            who_mut.append(line.strip("\n").split(",")[1])
            if line.strip("\n").split(",")[3]=='':
                who_mut_pos.append("none")
            else:
                who_mut_pos.append(line.strip("\n").split(",")[3])
            who_mut_confi.append(' '.join(line.strip("\n").split(",")[4].split(" ")[1:]))
    who_dict=dict(zip(who_mut,zip(who_mut_pos,who_mut_confi)))
    #print(who_dict)
    f_who_dict={}
    who_gene=[]
    who_mut=[]
    for i in who_dict:
        if who_dict[i][0]=='none':
            f_who_dict[i+";cds"]=[who_dict[i][1]]
            who_gene.append(i.split("_")[0])
            who_mut.append(i.split("_")[1])
        else:
            if len(i.split("_"))==3:
                f_who_dict[who_dict[i][0]+"_"+i.split("_")[1].split(" ")[0][0].upper()+">"+i.split("_")[1].split(" ")[0][-1].upper()+";non_cds"]=[who_dict[i][1]]
                who_gene.append(who_dict[i][0])
                who_mut.append(i.split("_")[1].split(" ")[0][0].upper()+">"+i.split("_")[1].split(" ")[0][-1].upper())
            elif len(i.split("_"))==2:
                f_who_dict[who_dict[i][0]+"_"+i.split("_")[1][0].upper()+">"+i.split("_")[1][-1].upper()+";non_cds"]=[who_dict[i][1]]
                who_gene.append(who_dict[i][0])
                who_mut.append(i.split("_")[1].split(" ")[0][0].upper()+">"+i.split("_")[1].split(" ")[0][-1].upper())
            elif len(i.split("_"))>3:
                f_who_dict[who_dict[i][0]+"_"+i.split("_")[-2].upper()+">"+i.split("_")[-1].upper()+";non_cds"]=[who_dict[i][1]]
                who_gene.append(who_dict[i][0])
                who_mut.append(i.split("_")[-2].upper()+">"+i.split("_")[-1].upper())

    #print(f_who_dict)
    if len(mut.split(","))>3:
        mut=','.join([mut.split(",")[0],mut.split(",")[2]+">"+mut.split(",")[3]])
    else:
        mut=mut

    singleletter = {'Cys': 'C', 'Asp': 'D', 'Ser': 'S', 'Gln': 'Q', 'Lys': 'K',
    'Trp': 'W', 'Asn': 'N', 'Pro': 'P', 'Thr': 'T', 'Phe': 'F', 'Ala': 'A',
    'Gly': 'G', 'Ile': 'I', 'Leu': 'L', 'His': 'H', 'Arg': 'R', 'Met': 'M',
    'Val': 'V', 'Glu': 'E', 'Tyr': 'Y', '---': '','Ter':'!'}

    final_ml_mut=[]
    #for i in ml_mut:
    if mut.startswith("p."):
        if mut.split(",")[0][-3:] in singleletter:
            if '' not in mut.split(","):
                #print(i)
                final_ml_mut.append(mut.split(",")[2].strip()+"_"+(mut.split(',')[0].replace((mut.split(",")[0][2:5]),(singleletter[mut.split(",")[0][2:5]])).replace((mut.split(",")[0][-3:]),(singleletter[mut.split(",")[0][-3:]])))[2:].strip()+";cds")
            else:
                #print(i)
                final_ml_mut.append(mut.split(",")[1].strip()+"_"+(mut.split(",")[0].replace((mut.split(",")[0][2:5]),(singleletter[mut.split(",")[0][2:5]])).replace((mut.split(",")[0][-3:]),(singleletter[mut.split(",")[0][-3:]])))[2:].strip()+";cds")
        else:
            if '' not in mut.split(","):
                final_ml_mut.append(mut.split(",")[2].strip()+"_"+(mut.split(',')[0].replace((mut.split(",")[0][2:5]),(singleletter[mut.split(",")[0][2:5]]))[2:].strip())+";cds")
                #print(i)
            else:
                final_ml_mut.append(mut.split(",")[1].strip()+"_"+(mut.split(',')[0].replace((mut.split(",")[0][2:5]),(singleletter[mut.split(",")[0][2:5]]))[2:].strip())+";cds")
                #print(i)
    else:
        final_ml_mut.append('_'.join(mut.split(","))+";non_cds")
    #print(final_ml_mut)
    final_info=[]
    for i in final_ml_mut:
        if i in f_who_dict:
            if i.split(";")[1]=='cds':
                final_info.append(i.split(";")[0]+"__"+'_'.join(f_who_dict[i])+"__"+"Known_region_known_mut")
            if i.split(";")[1]=='non_cds':
                final_info.append(non_cds_annot(i.split(";")[0])+"__"+'_'.join(f_who_dict[i])+"__"+"Known_region_known_mut")
        else:
            if i.split(";")[1]=='cds':
                if i.split(";")[0].split("_")[0] in who_gene:
                    final_info.append(i.split(";")[0]+"__"+"Known region new mutation"+"__"+"Known_region_new_mutation")
                else:
                    final_info.append(i.split(";")[0]+"__"+"New gene mutation"+"__"+"New_gene")
            else:
                if i.split(";")[0].split("_")[0] in who_gene:
                    final_info.append(non_cds_annot(i.split(";")[0])+"__"+"Known region new mutation"+"__"+"Known region new mutation")
                else:
                    final_info.append(non_cds_annot(i.split(";")[0])+"__"+"New gene mutation"+"__"+"New gene")
    return ''.join(final_info)
'''import sys
mutation=sys.argv[1]
drug=sys.argv[2]
result=mut_annot_who(mutation,drug)
print(result)'''




