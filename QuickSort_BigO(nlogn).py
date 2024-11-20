# Using Bubble Sort as Big O(nlogn)
import csv
import time
def quicksort(array):                                           # Big O (nlogn) / Divide and Conquer
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array)//2]                            # take middle element as pivot
        left = []
        right = []
        for element in array:
            if element < pivot:
                left.append(element)
            elif element > pivot:
                right.append(element)
        return quicksort(left) + [pivot] + quicksort(right)     # recurse the left array and right array
def generate_time(array):
    start_time = time.perf_counter()
    quicksort(array)
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
    # create data count and used time --> x-axis and y-axis
    count_time = []
    for k in range(20):
        count_time.append(generate_time(traverse_data[k]))
    # create points for further plotting
    new_file = "time_data.csv"
    with open(new_file, "w", newline="") as file2:
        csv_writer = csv.writer(file2)
        csv_writer.writerow(["", "Big O (nlogn)", "Big O (n^2)", "Big O (n)", "Big O (logn)"])
        for i in range(len(data_count)):
            csv_writer.writerow([data_count[i]])
    print(count_time)
if __name__ == "__main__":
    main()