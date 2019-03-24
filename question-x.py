#Margarita Vukas, 2019-03-23
#Program that displays a plot of the functions x, x^2 and 2^x in the range [0,4].

#Impoting numpy library.
import numpy

#Importing matplot.pyplot library.
import matplotlib.pyplot as pl

#Making three sets of data x,y1,y2 and y3.
#x are the values on the abscissa.
#y1,y2 and y3 are the values on the ordinate.

x=[0,1,2,3,4]
#Function y=x.
y1=x
#Function y=x^2.
y2=[0,1,4,9,16]
#Function y=2^x.
y3=[1,2,4,8,16]

#Function Pl.plot() makes a line graph of two given data sets.
pl.plot(x,y1)
pl.plot(x,y2)
pl.plot(x,y3)
#Pl.show function shows given plots on the screen.
pl.show()