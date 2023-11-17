import matplotlib.pyplot as plt

# Example data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]

# Create a histogram
plt.hist(data, bins=range(min(data), max(data) + 2), edgecolor='black')

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Example Data')

# Show the plot
plt.show()
