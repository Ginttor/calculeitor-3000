
reg=open("pante_pdf.txt", "r")
dad=reg.readlines()
reg.close()

print("aqui");sss=""
imu=dad[len(dad)-1].split("SUBTOTAL 12%");print(imu)
sss+="T:"+imu[1].replace("  ", "")+"\n"
print("T:",imu[1])
x=0;nn=0
while x < len(dad):
    #nn=dad[x].index("\n")
    if len(dad[x])>155 and 0==dad[x].count("o") and 0==dad[x].count("SUBTOTAL 12%"):
        nn=""
        y=len(dad[x])-7;num="";print(dad[x])
        while y < len(dad[x]):
            if dad[x][y]!=" ":num+=dad[x][y]
            y+=1
        if 42<len(dad[x-1]):
            y=42
            while y < len(dad[x-1]):
                if dad[x-1][y]!="\n":nn+=dad[x-1][y]
                y+=1
        if 42<len(dad[x]):
            y=42
            while y < 81:
                if dad[x][y]!="\n":nn+=dad[x][y]
                y+=1
        if 42<len(dad[x+1]):
            y=42
            while y <  len(dad[x+1]):
                if dad[x+1][y]!="\n":nn+=dad[x+1][y]
                y+=1
        print("CAB::",nn)
        sss+=nn.replace("  ", "")+"="+num
        print("T--",str(nn)+"="+num.replace("\n", ""))
    x+=1
reg=open("datos.txt", "w")
reg.write(sss)
reg.close()
print(sss)