# Extract enormous datasets from csv file
# Singleton Pattern so such enormous datasets will need to run once
import csv, pickle
def main():

    # Create data_count for x-axis
    data_count = []
    data_count.append(2000000)
    for i in range(19):
        data_count.append(data_count[i] + 1000000)
    with open("data_count.pkl", "wb") as file1:
        pickle.dump(data_count, file1)

    # Create data_count for bubble sort (Big O(n^2))
    data_count_bubble = []
    data_count_bubble.append(10000)
    for j in range(19):
        data_count_bubble.append(data_count_bubble[j] + 10000)
    with open("data_count_bubble.pkl", "wb") as file2:
        pickle.dump(data_count_bubble, file2)

    # Traverse the data from csv file to list in py file
    Asymptotic_Data_File = "MultiData.csv"                  # csv file from assignment#5 (times 50 times so now the size of datasets is 100 millions)
    row_count = 0
    Asymptotic_Data = []
    with open(Asymptotic_Data_File, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row_count <= data_count[19]:
                Asymptotic_Data.append(row)                 # put those asymptotic data into list in python
                row_count += 1
    with open("asymptotic_data.pkl", "wb") as file3:
        pickle.dump(Asymptotic_Data, file3)

    # Traverse the exact length for processing in another py file
    traverse_data = []
    for k in range(len(data_count)):
        traverse_data.append(Asymptotic_Data[:data_count[k]])
    with open("traverse_data.pkl", "wb") as file4:
        pickle.dump(traverse_data, file4)

    # Traverse the exact length for bubble sort algorithms in another py file
    traverse_data_bubble = []
    for z in range(len(data_count_bubble)):
        traverse_data_bubble.append(Asymptotic_Data[:data_count_bubble[z]])
    with open("traverse_data_bubble,pkl", "wb") as file5:
        pickle.dump(traverse_data_bubble, file5)

if __name__ == "__main__":
    main()