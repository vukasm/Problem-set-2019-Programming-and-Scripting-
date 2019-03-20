#Margarita Vukas, 2019-03-20
#Program that outputs today's date in a format "Monday, January 10th 2019 at 1:15 pm".

#This line will import datetime module.
import datetime

#Making a datetime object and calling it 'dt'.
dt= datetime.datetime.now()

#Using a strftime method to create a string representing the date and time under the control of an explicit format string.
#By using specific format codes, creating the format we want.
dt=datetime.datetime.strftime(datetime.datetime.now(), "%A, %B %d %Y at %I:%M %p")


#Printing current date and time in a specific format on the screen.
print(dt)