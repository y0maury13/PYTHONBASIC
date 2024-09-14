a=float(input("Enter the First Side Of Trianguale:"))
b=float(input("Enter the Second Side Of Trianguale:"))
c=float(input("Enter the Third Side Of Trianguale:"))
s=(a+b+c)/2
print("s=",s)
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area=",area)