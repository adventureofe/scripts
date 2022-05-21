# importing module
import matplotlib.pyplot as plt
import math

# x = a range of numbers from -1000 to 1000
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

y = [1,4,1,5,9,2,6,5,3,5, 8, 9, 7, 9, 3, 2, 8, 4, 6, 2, 6]

# Plot the graph and load into RAM
plt.plot(x, y, color='green')

# y axis displayed
plt.ylim([0, 10])

# x axis displayed
plt.xlim([min(x), max(x)])

# side labels
plt.xlabel('x')
plt.ylabel('y')

# displaying the title
plt.title("Linear graph")

# display the graph to screen
plt.show()
