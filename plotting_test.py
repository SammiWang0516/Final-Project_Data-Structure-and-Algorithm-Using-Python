import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
y = [0.72, 1.2, 1.57, 2.17, 2.75, 3.24, 3.95, 4.25, 5.25, 5.66, 5.93, 6.82, 7.5, 7.99, 8.94, 9.35, 10.45, 10.46, 11.62, 12.92]
slope, intercept = np.polyfit(x, y, 1)
regression_line = slope * x + intercept
plt.scatter(x, y, color="blue", label="Data Points")
plt.plot(x, regression_line, color="red")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot with Regression Line')
plt.legend()
plt.show()