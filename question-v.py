#Margarita Vukas, 2019-03-03
#Program that tells you whether or not n is a prime number.
#Prime number is a number that is devisible only by itself and 1.

#Asking the user to enter a positive integer which will be the value of n.
n=int(input("Enter a positive integer:"))

#Condition is that n has to be greater than 1 because prime numbers are greater than 1.
if n>1:
    #Checking if n is devisible by any number between 2 and n.
    #If it is, n is not a prime number and that is printed on the screen.
    for x in range (2,n):
        if n%x==0:
            print (n, "is not a prime number.")
            #Found the answer half way through the loop, so I am breaking it.
            break
        #If n is not devisible by any number between 2 and n, it is a prime number and that is printed on the screen.
        else:
            print (n, "is a prime number.")
            break
#loop fell through without finding an answer because integer entered was 1.
#One is not a prime number and that is printed on the screen.
else:
    print(n, "is not a prime number.")
