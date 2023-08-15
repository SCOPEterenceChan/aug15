'''
15/8/2023 bY Terence
Algorithm PRIME. Given a positive integer NUM,
this algorithm determine whether or not the numbers is prime. LOOP is an integer loop variable

1. input the number 
   Read(NUM)

2. determine that the NUM is prime or has divisors other than 1 
   2.1 determine if number is divisible by 2
       If NUM = 2                       
       Then NUM is a prime number
       Else If NUM is even
            Then NUM is not a prime number and halt
            Else 2.11  determine if (NUM divisible by odd integers >= 3 and  <=  (square root of NUM))
                       For LOOP := 3 to sqrt(NUM) by 2
                       Do If (NUM mod LOOP) = 0
                          Then NUM is not a prime number and halt

3. if we get here, print a message that NUM is a prime number 
   Write(NUM,"is a prime number");

4. finished
   Halt
'''
import math
num=int(input('enter a integer ')) #input the number

if num == 2:
    print(num, ' is prime')
elif num % 2 == 0:
    print(num, ' is not prime')
else:
    isPrime = True
    for i in range(3,int(math.sqrt(num)),2):
       if num % i == 0:
           print(num, ' is not prime')
           isPrime = False
           break

    if isPrime:
        print(num, ' is prime')
