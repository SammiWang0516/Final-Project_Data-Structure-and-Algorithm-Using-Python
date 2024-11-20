# elapse time for the algorithm: Big O(n^2)
import csv, time, random, pickle
def BubbleSort(array):                                          # Big O(n^2): only applicable for smaller datasets
    count = len(array)
    for i in range(count):                                      # first for loop f(n) = n
        for j in range(0, count - i - 1):                       # second for loop f(n) = n^2
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
def Time_BubbleSort(array):
    start_time = time.perf_counter()
    BubbleSort(array)
    end_time = time.perf_counter()
    duration = round(end_time - start_time, 2)
    return duration
def main():
    with open("data_count_bubble.pkl", "rb") as file3:
        data_count_bubble = pickle.load(file3)
    with open("traverse_data_bubble,pkl", "rb") as file4:
        traverse_data_bubble = pickle.load(file4)
    print("*****Sammi Wang's Final Project*****")
    print(f"The no. of datasets for Big O(n^2) is {data_count_bubble}")
    time_nn = []
    for i in range(20):
        time_nn.append(Time_BubbleSort(traverse_data_bubble[i]))
    print(time_nn)
    with open("time_nn.pkl", "wb") as file8:
        pickle.dump(time_nn, file8)
if __name__ == "__main__":
    main()