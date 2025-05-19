# Run this cell without changes
import numpy as np
import matplotlib.pyplot as plt

# # Replace None with appropriate code
# height =[40, 30, 10, 50, 25, 5]  # movie counts
# x = list(range(6))
# labels = ['crime', 'science fiction', 'drama', 'comedy', 'action', 'documentary']

# # Create the plot
# fig, ax = plt.subplots(figsize=(8, 6))

# # Plot vertical bars of fixed width by passing x and height values to .bar() function 
# ax.bar(x, height, tick_label=labels)

# # Give a title to the bar graph and label the axes
# ax.set_title('Number of Movies by Genre at Jim\'s Video Library')
# ax.set_xlabel('Genre')
# ax.set_ylabel('Number of Movies')
# plt.tight_layout()
# plt.show()




# # Data
# weight = [2750, 3125, 2100, 4082, 2690, 3640, 4380, 2241, 2895, 3659]
# mpg = [29, 23, 33, 28, 20, 21, 14, 25, 31, 17]
# # Create the plot
# fig, ax = plt.subplots(figsize=(8, 6))
# # Plot with scatter()
# ax.scatter(weight, mpg, color='blue', label='Car Data')
# # Set x and y axes labels, legend, and title
# ax.set_xlabel('Weight (lbs)')
# ax.set_ylabel('Miles per Gallon (MPG)')
# ax.set_title('Relationship Between Car Weight and MPG')
# ax.legend()
# # Show the plot
# plt.tight_layout()
# plt.show()


# Data
x = [43.1, 35.6, 37.5, 36.5, 45.3, 43.4, 
     40.3, 50.2, 47.3, 31.2, 42.2, 45.5, 
     30.3, 31.4, 35.6, 45.2, 54.1, 45.6, 
     36.5, 43.1]
# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
# Plot the histogram
ax.hist(x, bins=5, color='blue', edgecolor='blue')
# Label axes and set title
ax.set_xlabel('Waiting Time (seconds)')
ax.set_ylabel('Number of Customers')
ax.set_title('Customer Waiting Times at the Bank')

# Show the plot
plt.tight_layout()
plt.show()