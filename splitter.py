import matplotlib.pyplot as plt
import numpy as np

# A scatter plot
# x = np.linspace(0, 10, 30)
# y = np.sin(x)


# plt.figure(figsize=(10,6))
# plt.scatter(x, y, label = "y = sin(x)" )
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.title('Scatter Plot in Matplotlib')
# plt.legend()
# plt.show()

# A bar graph
# Set seed for reproducibility
# np.random.seed(100)

# # Generate the x-axis variable as 10 categories using numpy's arange function
# x = np.arange(10)

# # For y-axis, generate 10 random quantities
# y = np.random.randn(10)

# plt.figure(figsize=(10,6))

# # Use the bar() function to create a plot using the above values of x and y. Add a label.
# plt.bar(x, y, label='Sample Data')

# plt.xlabel('X Values - Categories')
# plt.ylabel('Y Values - Quantities')

# plt.title('Bar Plot in Matplotlib')
# plt.legend()

# # Output the final plot
# plt.show()

# Histo
# Set seed for reproducability
# np.random.seed(100)

# # Generate a data set of 200 retirement age values
# x = 5*np.random.randn(200) + 65

# #Plot the histogram with hist() function
# plt.hist(x, bins = 10, edgecolor='black')

# plt.xlabel('Retirement Age')
# plt.ylabel('Frequency of Values')
# plt.title('Histograms in Matplotlib')
# plt.show()

# # Set seed for reproducability
# np.random.seed(100)

# Generate a data set of 10000 retirement age values
x = 5*np.random.randn(10000) + 65

# #Plot the distogram with hist() function
# plt.hist(x, bins=50, edgecolor="black")

# plt.xlabel('Retirement Age')
# plt.ylabel('Frequency of Values')
# plt.title('Histograms in Matplotlib')
# plt.show()
