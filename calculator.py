op=input("Enter the operation symbol you want to perform: ")
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
if op=='+':
    print(a,"+",b,"=",a+b)
elif op=='-':
    print(a,"-",b,"=",a-b)
elif op=='/':
    print(a,"/",b,"=",a/b)
elif op=='*':
    print(a,"*",b,"=",a*b)
else:
    print("IVALID INPUT")