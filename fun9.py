def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def divi(a,b):
    print(a/b)

a = int(input("no1 :"))
b = int(input('no2 :'))

print("1.add")
print("2.sub")
print("3.multi")
print("4.div")

choice = int(input("choice:"))

if choice == 1:
    add(a,b)

elif choice ==2:
    sub(a,b)

elif choice ==3:
    mult(a,b)

elif choice == 4:
    divi(a,b)

else:
    print("error")


