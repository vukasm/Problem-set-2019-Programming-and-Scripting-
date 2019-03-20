#Margarita Vukas, 2019-03-20
#Program that reads in a text file and outputs every second line.
#The program takes the filename from an argument on the command line.


#Asking a user to input a filename.
filename= input("Enter a filename:")

#Opening that file for reading.
with open(filename, 'r') as f:
    #Setting a value of 'count' to zero. 
    #This will represent the number of the line.
    count=0
    #For every line in this file, run this:
    for l in f:
        #For every line, the value of count is growing by 1.
        count=count+1
        #If line number is devisable by 2, print the line on the screen.
        if count%2==0:
            print(l)