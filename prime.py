from operator import truediv
a=int(input("no"))
b=False
if a!=0:
    for i in range(2,a):
        if a%i:
            b=True
            break
if b:
    print("np")
else:
    print("p")