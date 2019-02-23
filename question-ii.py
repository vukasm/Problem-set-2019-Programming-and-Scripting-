#Margarita Vukas, 2019-02-23
#Program that tells you wheather or not today is a day that starts with the letter T.

#Using datetime module to work with dates, in this case weekdays.
import datetime

#If this statement is true, run the following.
#If today is second day of the week, print the following.
#Counting starts from 0, therefore I am using number 1 for second day of the week (Tuesday).
if datetime.datetime.today().weekday() == 1:
  print("Yes, today begins with a T.")
#Using elif statement to check if another statement is true.
#If today is fourth day of the week(Thursday), print the following.
#Counting starts from 0, so I am using number 3 for the fourth day of the week.
elif datetime.datetime.today().weekday() == 3: 
    print("Yes, today begins with a T.")
#If both of those statements are false, print the following.
else:
  print("Unfortunately today does not begin with a T.")