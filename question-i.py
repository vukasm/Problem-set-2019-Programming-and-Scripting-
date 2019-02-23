#Margarita Vukas, 2019-02-23
#Program tgat calculates the sum of all numbers between 1 and n

#asking the user to enter a positive integer which will be the n variable 
#int stands for integer ie whole number
n= int (input("Please enter a positive integer:"))

#setting value of variables sum and i to 0 at the start
i=0
sum=0

#initializing variable i with a value of 1
i=1
#as long as value of i is less or equal to n(condition is true), run the fallowing
#if i(i=1) is less or equal to n, the new value of sum is sum+i
#the new value of i is now increased by 1 so i=2 
#the condition is now questioned again with the new value of i
while i<=n:
    sum=sum+i
    i=i+1

#if the condition is false (i>n) print the current value of sum to the screen
print(sum)