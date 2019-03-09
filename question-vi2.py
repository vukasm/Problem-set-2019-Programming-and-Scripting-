#Margarita Vukas, 2019-03-09
#Program that asks the user to input a string and outputs every other word.


#asking a user to input a string in a form of sentence.
#Giving this string a name 'Sentence'.
sentence=input("Enter a Sentence:")

#Splitting the string in separate elements.
sentence=sentence.split()
#Using range, the new sentence contains every second element from the old sentence string.
#Two colon marks represent start and stop in range since they are not relevant here.
sentence=sentence[::2]
#Putting the elements back together in a string.
sentence=' '.join(sentence)
#Printing the new sentence on the screen.
print(sentence)