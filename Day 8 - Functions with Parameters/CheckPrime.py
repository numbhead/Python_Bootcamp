def check_prime(number):
    isPrime = True
    for i in range(2, number):
        if(number%i == 0):
            isPrime = False
    
    if(isPrime):
        print("It is a prime number!")
    else:
        print("It is not a prime number")


num = int(input("Enter the number to check : "))
check_prime(num)

