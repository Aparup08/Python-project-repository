print("Welcome to Calculator V1")
a=int(input("Enter first number:"))
operator=input("Enter operator:")
b=int(input("Enter second number:"))
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("Invalid operator")