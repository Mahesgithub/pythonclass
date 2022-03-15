a=153
t=str(a)
z=[]
for i in range(0,len(t)):
    c=int(t[i])
    cu =c*c*c
    z.append(cu)
result=z[0]+z[1]+z[2]
if a==result:
    print("Asn")
else:
    print("no")



