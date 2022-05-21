# importing module 
import matplotlib.pyplot as plt
import math
    
# x = a range of numbers from -1000 to 1000
x = list(range(-1000, 1001))

# convert x to -10 to 10 (in increments 0.01)
for i in range(len(x)):
    x[i] = x[i] * 0.01

# y = a list of 0's the same length as x (default)
y = [0] * len(x)

# set each y to x squared
for i in range(len(y)):
    y[i] = x[i]**2 * math.sin(x[i]**2) 

# Plot the graph and load into RAM
plt.plot(x, y, color='green') 

# y axis displayed
plt.ylim([min(y), max(y)])

# x axis displayed
plt.xlim([min(x), max(x)])

# side labels
plt.xlabel('x') 
plt.ylabel('y') 
  
# displaying the title
plt.title("Linear graph")

# display the graph to screen 
plt.show() 
