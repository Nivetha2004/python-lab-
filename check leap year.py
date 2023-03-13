#Python program to check if year is a leap year or not
year = int(input("Enter a year:"))
#dived by 100 means century year(ending with 100)
if (year%400==0)and (year%100==0):
    print("{0] is a leap year".format(year))
#not didved by 100 means not a century year
#year divided by 4 is a leap year
elif(year%4==0)and (year%100!=0):
    print("{0} is a leap year".format(year))
#if not divided by both 400(century year) and 4(not century year)
#year is not a leap year
else:
    print("{0} is not a leap year".format(year))
