
#grabs a number and says if its prime or not

#numbers below 2 are not prime
#any number devisible by any number other than 1 and itself is not prime


x = input("Which number do you wanna check for prime?")

def is_prime(x):
    isPrime = False
    if x < 2:
        isPrime = False
    if x == 2:
        isPrime = True
    elif x>2: 
        for i in range(2,x):
            if (x % i) == 0:
                isPrime = False
                break
            else:
                isPrime = True
          
    return isPrime 


#print("15 is prime :", is_prime(15))
#print("9 is prime:" ,is_prime(9))
#print(is_prime(4))
print(is_prime(int(x)))


