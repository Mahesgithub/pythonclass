a = int(input("no1 :"))
b = int(input('no2 :'))

print("1.add")
print("2.sub")
print("3.multi")
print("4.div")

choice = int(input("choice:"))

if choice == 1:
    print(a+b)

elif choice ==2:
    print(a-b)

elif choice ==3:
    print(a*b)

elif choice == 4:
    print(a/b)

else:
    print("error")