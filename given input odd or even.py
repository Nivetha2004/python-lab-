#Python program to check if the give in put number is odd or even.
#A number is even if even if division by 2 gives a remainder of 0.
# if the remainder is 1, it is an odd number
num = int(input("Enter a number:"))
if(num%2)==0:
    print("{0} is Even".format(num))
else:
    print("{0} is odd".format(num))
    
