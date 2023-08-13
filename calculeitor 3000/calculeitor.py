import random

reg=open("datos.txt", "r")
dad=reg.readlines()
reg.close()
reg=open("exet.txt", "r")
mno=reg.readlines()
reg.close()


exa=input("ESCANER?")
dadi=dad
def reorg(mip):
    m=list(range(len(mip)))
    y=1;m[0]=mip[0]
    while y<len(m):
        v=random.randint(1, len(mip)-1)
        m[y]=mip[v]#;print(v,"/",len(mip))
        mip.remove(mip[v])
        y+=1
    #print("{[", m, "]}")
    return m
ss="";x=1
if exa=="":
    while x < len(dad):
        y=0;si=False;punto=""
        while y < len(mno):
            if 0<dad[x].count("="):punto=dad[x].split("=")
            if 0<dad[x].count("\t"):punto=dad[x].split("\t")
            print("AN:",punto)
            if 0<punto[0].count(mno[y].replace("\n", "")):
                si=True
            y+=1
        if si==False:
            print("no coinside<>")
        else:dad.remove(dad[x])
        x+=1
R=dad[0].split(":");n=0
while float(R[1])!=round(n, 2):
    dadi=reorg(dadi)
    x=1;n=0;ss=""
    while x<len(dadi):
        if round(n, 2)<float(R[1]):
            ss+=dadi[x].replace("=", "\t")+"\n"
            if 0<dadi[x].count("="):
                no=dadi[x].split("=")#;print("COMP(=)", dadi[x].count("="))
            if 0<dadi[x].count("\t"):
                no=dadi[x].split("\t")#;print("COMP(tt)")
            #print(dadi[x],"--",no[1])
            n+=float(no[1])
        x+=1
    print( R[1],"><",round(n, 2))
    if round(n, 2)<float(R[1]):print("[ERROR EN LOS DATOS]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(ss)
reg=open("salia.txt", "w")
reg.write(ss)
reg.close()