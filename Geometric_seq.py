#this python file is to generate a geometric sequence
#assume to flip a coin, keep flip a coin until a head is get, probability of getting a head is 1/2
import numpy as np
import matplotlib.pyplot as plt

p = 1/2 #the probability is 1/2
n = np.arange(1,10)#total trial numbers from 1 to 10
x = np.power(p,n)

#draw the bar graph with n as x-axis, x as y-axis
plt.bar(n, x)

#show the graph
plt.show()