#Margarita Vukas, 2019-02-25
#Program that prints all numbers between 1000 and 10000 devisable by 6 but not 12.

#Created a sequence of numbers from 1000 to (not including) 10 000.
#Two conditions: n is devisable by 6 and n is not devisable by 12.
#If both conditions are true, print the following (n)
for n in range(1000,10000):
    if n%6==0 and n%12!=0:
        print(n)