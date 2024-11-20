# put all elapse time for all four algorithms: Big O(logn), Big O(n), Big O(nlogn), Big O(n^2)
import csv, time, random, pickle
def BinarySearch(array, target):                                # ~~~Big O(logn): the fastest algorithm~~~ #
    low = 0                                                     # the very least index is first set to be 0
    high = len(array) - 1                                       # the greatest index is len(array) - 1
    while low <= high:                                          # keep searching until low is no longer smaller than high
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
    return -1                                                   # return -1 means that there is no match with the target
def MaximumSearch(array):                                       # ~~~Big O(n): the second fastest algorithm~~~ #
    max_value = array[0]                                        # assume the maximum value is the first element in the list
    for i in range(len(array)):                                 # one for loop means that each element will be scanned
        if array[i] > max_value:
            max_value = array[i]
    return max_value
def QuickSort(array):                                           # Big O(nlogn): decent speed
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]                          # pivot set to be the element at the middle index
        left = []                                               # create two empty list for storage
        right = []
        for element in array:
            if element < pivot:
                left.append(element)                            # element which value is smaller than pivot will be stored in left list
            elif element > pivot:
                right.append(element)                           # element which value is greater than pivot will be stored in right list
        return QuickSort(left) + [pivot] + QuickSort(right)     # recursive if the size of left or right array doesn't equal to 1 or less than 1
def BubbleSort(array):                                          # Big O(n^2): only applicable for smaller datasets
    count = len(array)
    for i in range(count):                                      # first for loop f(n) = n
        for j in range(0, count - i - 1):                       # second for loop f(n) = n^2
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
def Time_BinarySearach(array):
    total_time = 0
    random_index = random.randint(0, len(array) - 1)
    for i in range(5):
        start_time = time.perf_counter()
        BinarySearch(array, array[random_index])
        end_time = time.perf_counter()
        duration = round((end_time - start_time) * 1000, 5)
        total_time += duration
    return round(total_time/5, 5)
def Time_MaximumSearch(array):
    total_time = 0
    for i in range(5):
        start_time = time.perf_counter()
        MaximumSearch(array)
        end_time = time.perf_counter()
        duration = round(end_time - start_time, 2)
        total_time += duration
    return round(total_time/5, 2)
def Time_QuickSort(array):
    total_time = 0
    for i in range(5):
        start_time = time.perf_counter()
        QuickSort(array)
        end_time = time.perf_counter()
        duration = round(end_time - start_time, 2)
        total_time += duration
    return round(total_time/5, 2)
def Time_BubbleSort(array):
    start_time = time.perf_counter()
    BubbleSort(array)
    end_time = time.perf_counter()
    duration = round(end_time - start_time, 2)
    return duration
def main():
    with open("data_count.pkl", "rb") as file1:
        data_count = pickle.load(file1)
    with open("traverse_data.pkl", "rb") as file2:
        traverse_data = pickle.load(file2)
    print("*****Sammi Wang's Final Project*****")
    print(f"The x-axis is {data_count}")
    time_logn = []
    time_n = []
    time_nlogn = []
    for i in range(20):
        time_logn.append(Time_BinarySearach(traverse_data[i]))
        time_n.append(Time_MaximumSearch(traverse_data[i]))
        time_nlogn.append(Time_QuickSort(traverse_data[i]))
    print(time_logn)
    print(time_n)
    print(time_nlogn)
    with open("time_logn.pkl", "wb") as file5:
        pickle.dump(time_logn, file5)
    with open("time_n.pkl", "wb") as file6:
        pickle.dump(time_n, file6)
    with open("time_nlogn.pkl", "wb") as file7:
        pickle.dump(time_nlogn, file7)
if __name__ == "__main__":
    main()