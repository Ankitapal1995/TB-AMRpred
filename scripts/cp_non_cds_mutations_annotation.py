#from sys import argv
#s,mut,kl = argv
def non_cds_annot(mutation):
    f=open('/home/ankita/Desktop/webserver_tool/scripts/al123456.gff3').readlines()
    gff_data=[]
    for j,i in enumerate(f):
        i = i.strip("\n")
        if i.startswith("#"):
           pass
        elif i.split("\t")[2]=='gene':
           pass
        else:
       #print(i)
           gff_data.append((i.split("\t")[2],i.split("\t")[3],i.split("\t")[4],i.split("\t")[8].split(";")))
#print(gff_data)
    final_gff_data=[]
    for i in gff_data:
        ls=[]
        for k,j in enumerate(i[3]):
            if j.startswith("gene") or j.startswith("locus"):
               ls.append(i[3][k])
        final_gff_data.append((i[0],i[1],i[2],','.join(ls)))
#print(len(final_gff_data))
    gff_full_gene=[]
    for j,i in enumerate(final_gff_data):
        if j+1<len(final_gff_data):
           t=(final_gff_data[j],int(final_gff_data[j][2])+1,int(final_gff_data[j+1][1])-1,final_gff_data[j+1])
           gff_full_gene.append(t)
        else:
           t=(final_gff_data[j],int(final_gff_data[j][2])+1,int(000000),('none',0,0,'none'))
           gff_full_gene.append(t)
    #3print(gff_full_gene)
    coordinate=str(mutation).split("_")[0]
    prev_pos=str(mutation).split("_")[1].split(">")[0]
    curr_pos=str(mutation).split("_")[1].split(">")[1]
    for i in gff_full_gene:
        #print(i[3][3].split(",")[0][5:])
        if int(coordinate) in range(int(i[0][1]),int(i[0][2])):
           if i[3][3].startswith("gene"):
              return str(i[3][3].split(",")[0][5:])+"_n."+str(abs(int(i[0][1])-int(coordinate)))+prev_pos+">"+curr_pos
           else:
              return str(i[3][3][10:])+"_n."+str(abs(int(i[0][1])-int(coordinate)))+prev_pos+">"+curr_pos
        if int(coordinate) in range(i[1],i[2]):
           if i[3][3].startswith("gene"):
              return str(i[3][3].split(",")[0][5:])+"_c.-"+str(abs(int(coordinate)-(i[2]))+1)+prev_pos+">"+curr_pos
           else:
              return str(i[3][3][10:])+"_c.-"+str(abs(int(coordinate)-(i[2]))+1)+prev_pos+">"+curr_pos
        if int(coordinate) in range(int(i[3][1]),int(i[3][2])):
           if i[3][3].startswith("gene"):
              return str(i[3][3].split(",")[0][5:])+"_c.-"+str(abs(int(i[3][1]) - int(coordinate)))+prev_pos+">"+curr_pos
           else:
              return str(i[3][3][10:])+"_c.-"+str(abs(int(i[3][1]) - int(coordinate)))+prev_pos+">"+curr_pos


'''if __name__ == '__main__':
    #import sys
    #mut=sys.argv[1]
    print(non_cds_annot(str(mut)))'''
