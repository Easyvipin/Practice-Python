#Write a program to find all the prime numbers in a range using list comprehension

lower=int(input("Enter the lower bound of the range:"))
upper=int(input("Enter the upper bound of the range:"))

prime=[]
if lower >0 and upper >0 and lower<upper:
    if lower == 1:
        prime = [x for x in range(2,upper) if 0 not in [ x%i for i in range(2,int(x/2)+1)]]
    else:
        prime = [x for x in range(lower,upper) if 0 not in [ x%i for i in range(2,int(x/2)+1)]]
    print("All prime number from {} to {} are:".format(lower,upper))
    print(prime)
else:
    print("Enter a valid range.Try Again!")
