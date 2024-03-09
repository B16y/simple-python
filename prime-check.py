num = int(input("enter the number:"))
count = 0

if num>0:
 for i in range(1,num+1):
    if num%i==0:
        count+=1
    else:
        pass
if count==2:
    print("prime number")
else:
    print("not prime number")