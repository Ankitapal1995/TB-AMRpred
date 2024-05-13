from sys import argv
s,filename=argv
f=open(filename,"r").readlines()
cds=[]
for i in f:
    i=i.strip("\n")
    l=i.split(",")
    if "CDS" in l:
        if len(l)==14:
            v=','.join(l[-4:-1])
            cds.append(v.split(" ")[2])
        elif len(l)>14:
            v=','.join(l[-(4+(len(l)-14)):-((len(l)-14)+1)])
            cds.append(v.split(" ")[2])
    else:    
        cds.append(','.join(l[1:]))

index= filename.rfind('.')
result_string=filename[:index]
fo = open("edited_"+result_string+".csv","w")
for i in cds:
#    print(''.join(i.split(" ")[2:]))
    fo.write(i)
    fo.write("\n")
fo.close()

