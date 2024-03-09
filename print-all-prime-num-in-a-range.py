numrange =  int(input("Enter the range: "))

count = 0

for i in range(1,numrange+1):
    if i%2==0:
        count = count + 1 
    else:
        print(i)
