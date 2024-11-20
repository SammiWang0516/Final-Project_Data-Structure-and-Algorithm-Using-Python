# plotting using numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pickle
def plot_logn(x, y):
    # plot the scatter points and regression line for Big O(logn)
    plt.scatter(x, y, color="blue", label="Big O(logn)")
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * x + intercept
    plt.plot(x, regression_line, color="red")
def plot_n(x, y):
    # plot the scatter points and regression line for Big O(n)
    plt.scatter(x, y, color="green", label="Big O(n)")
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * x + intercept
    plt.plot(x, regression_line, color="red")
def plot_nlogn(x, y):
    # plot the scatter points and regression line for Big O(nlogn)
    plt.scatter(x, y, color="purple", label="Big O(nlogn)")
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * x + intercept
    plt.plot(x, regression_line, color="red")
def plot_nn(x, y):
    # plot the scatter points and regression line for Big O(n^2)
    plt.scatter(x, y, color="orange", label="Big O(n^2)")
    coefficients = np.polyfit(x, y, 2)
    x_curve = np.linspace(min(x), max(x), 20)
    y_curve = np.polyval(coefficients, x)
    plt.plot(x_curve, y_curve, color="red")
def main():
    # load the pickles from the same directory
    with open("time_logn.pkl", "rb") as file1:
        time_logn = np.array(pickle.load(file1))/1000
    with open("time_n.pkl", "rb") as file2:
        time_n = np.array(pickle.load(file2))
    with open("time_nlogn.pkl", "rb") as file3:
        time_nlogn = np.array(pickle.load(file3))
    with open("time_nn.pkl", "rb") as file4:
        time_nn = np.array(pickle.load(file4))
    with open("data_count.pkl", "rb") as file5:
        data_count = np.array(pickle.load(file5))
    with open("data_count_bubble.pkl", "rb") as file6:
        data_count_bubble = np.array(pickle.load(file6))
    # plot the Big O(n^2)
    plot_nn(data_count_bubble, time_nn)
    plt.xlabel('No. of Element')
    plt.ylabel("Operation times (s)")
    plt.title("Time Complexity Big O(n^2) vs. Operation Times")
    plt.legend()
    plt.show()
    # plot the Big O(logn)
    plot_logn(data_count, time_logn)
    plt.xlabel('No. of Element')
    plt.ylabel("Operation times (s)")
    plt.title("Time Complexity Big O(logn) vs. Operation Times")
    plt.legend()
    plt.show()
    # plot the Big O(nlogn)
    plot_nlogn(data_count, time_nlogn)
    plt.xlabel('No. of Element')
    plt.ylabel("Operation times (s)")
    plt.title("Time Complexity Big O(nlogn) vs. Operation Times")
    plt.legend()
    plt.show()
    # plot the Big O(n)
    plot_n(data_count, time_n)
    plt.xlabel('No. of Element')
    plt.ylabel("Operation times (s)")
    plt.title("Time Complexity Big O(n) vs. Operation Times")
    plt.legend()
    plt.show()
    # plot the Big O(logn) & Big O(n)
    plot_logn(data_count, time_logn)
    plot_n(data_count, time_n)
    plt.xlabel('No. of Element')
    plt.ylabel("Operation times (s)")
    plt.title("Time Complexity Big O(logn) & Big O(n) vs. Operation Times")
    plt.legend()
    plt.show()
    # plot the Big O(logn) & Big O(n) & Big O(nlogn)
    plot_logn(data_count, time_logn)
    plot_n(data_count, time_n)
    plot_nlogn(data_count, time_nlogn)
    plt.xlabel('No. of Element')
    plt.ylabel("Operation times (s)")
    plt.title("Time Complexity Big O(nlogn) vs. Big O(n) & Big O(logn)")
    plt.legend()
    plt.show()
    # plot them all (Comparison)
    plot_logn(data_count, time_logn)
    plot_n(data_count, time_n)
    plot_nlogn(data_count, time_nlogn)
    plot_nn(data_count_bubble, time_nn)
    plt.xlabel('No. of Element')
    plt.ylabel("Operation times (s)")
    plt.title("Time Complexity Big O(nlogn) vs. Big O(n) vs. Big O(logn) vs. Big O(n^2)")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()