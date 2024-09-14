def findmax(x,y):
    if x>y:
        return x
    else:
        return y
    
def findmin(a,b):
    if a<b:
        return a
    else:
        return b
    
a=int(input("Enter First Value:"))
b=int(input("Enter Second Value:"))

print("Maxium Value=",findmax(a,b))
print("Minium Value=",findmin(a,b))