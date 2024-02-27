import matplotlib.pyplot as plt

# Define the x and y value ranges
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='pink', s=10)

# Set the chart title and axes labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the size of the tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the axes ranges
ax.axis([0, 1100, 0, 1100000])

plt.show()