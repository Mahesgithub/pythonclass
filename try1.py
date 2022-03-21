a=100
try:
    c=a/100
except ZeroDivisionError:
    print("error")
else:
    print(c)
finally:
    print("nice")