# Using Binary Search as Big O(logn)
import csv
import time
import random
def binarysearch(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low + high)//2
        if array[mid][0] == target:
            return mid
        elif array[mid][0] < target:
            low = mid + 1
        elif array[mid][0] > target:
            high = mid - 1
    return -1
def generate_time(array):
    start_time = time.perf_counter()
    binarysearch(array, "H")
    end_time = time.perf_counter()
    duration = round((end_time - start_time) * 1000, 5)
    return f"{duration} ms"
def main():
    # asymptotic data copied from csv file into py file
    Asymptotic_Data_File = "MultiData.csv"
    Asymptotic_Data = []
    with open(Asymptotic_Data_File, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            Asymptotic_Data.append(row)
    # data count --> x-axis
    data_count = [200000]
    for i in range(19):
        data_count.append(data_count[i] + 100000)
    # data traversed from asymptotic data --> for y-axis
    traverse_data = []
    for j in range(len(data_count)):
        traverse_data.append(Asymptotic_Data[:data_count[j]])
    count_time = []
    for k in range(20):
        count_time.append(generate_time(traverse_data[k]))
    print(count_time)
if __name__ == "__main__":
    main()