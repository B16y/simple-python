#using third  variable

# a = int(input("enter the  number:"))
# b = int(input("enter the  number:"))

# c = a 
# a = b 
# b = c

# print("the numbers a and b after swapping:",a , b )

#without using third variable

# method-1
# a = int(input("enter the  number:"))
# b = int(input("enter the  number:"))

# a = a + b
# b = a - b
# a =  a - b

# print("the numbers after swapping:",a,b)

# method-2

a = int(input("enter the  number:"))
b = int(input("enter the  number:"))

a , b = b , a

print("the numbers after swapping:",a,b)