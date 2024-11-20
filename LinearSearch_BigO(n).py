# Using Bubble Sort as Big O(n)
import csv
import time
def linearsearch(array):
    max_value = array[0]
    for i in range(len(array)):
        if array[i] > max_value:
            max_value = array[i]
    return max_value
def generate_time(array):
    start_time = time.perf_counter()
    linearsearch(array)
    end_time = time.perf_counter()
    duration = round(end_time - start_time, 2)
    return duration
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
    print(linearsearch(traverse_data[0]))
if __name__ == "__main__":
    main()