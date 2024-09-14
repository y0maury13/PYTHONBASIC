n=int(input("Enter Any Number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
    print("Count Of Digits:",count)


students=["Juan","John","Luis","Ignacio"]
for student in students:
    print(student)