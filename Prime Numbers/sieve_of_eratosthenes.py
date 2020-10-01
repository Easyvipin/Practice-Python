"""
Python program to print all prime number smaller than or equal
to the given input using Sieve of Eratosthenes.
"""


def sieve_of_eratosthenes(num):
    # List to store whether a number is prime or not
    prime = [True for i in range(num+1)]
    p = 2
    while (p*p <= num):
        # If prime[p] is True, then p is a prime number
        if (prime[p] == True):
            # Update all multiples of Prime p
            for i in range(p*p, num+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p),


if __name__ == '__main__':
    num = int(input())
    print("Following are the prime numbers smaller than or equal to {}".format(num))
    sieve_of_eratosthenes(num)
