def is_prime(number):
    for i in range(2,number):
        if number % i == 0 :
            print("not prime")
            return
    print("prime")
            
is_prime(24)