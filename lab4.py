import csv 
#Imported csv 

def fetchData(): #This function will grab the data
    try: #It will try
        with open("budget_data.csv") as file: #to fetch the budget_data and be name as file 
            fetchData = csv.reader(file)  #where it will be read by the csv reader and be stored in fetch Data
            next(fetchData) #Skipping the header
            data = [] #With an empty list
            for row in fetchData: #Each row in fetchData
                date = row[0] #The date is in the row first column
                profit_loss = int(row[1]) #and profit loss is in the second column
                data.append([date, profit_loss]) #It will be appended to the data list 
            return data #and be returned
    except FileNotFoundError: #If the file is not founder
        print("The file was not found.") #It will print out this error
    except ValueError: #If a wrong input was in the file
        print("An error occurred with the Value.") #it will print out an error

def dataSorting(data, size): #This function will sort the data using Selection sort
    for index in range(size): #for each index in the range largest amount of data
        min_index = index #the min will be set as the index
        for j in range(index + 1, size): #For j in range of the index + 1 and size 
            if data[j][0] < data[min_index][0]: #If the data j first column is less than data minimum data set first column
                min_index = j #the min index will be set as j
        
        (data[index], data[min_index]) = (data[min_index], data[index]) #This will swap the data around
    return data #and return back the data

def dataInsertionSort(data,size):#This function will sort the data using Insertion sort 
    for index in range(1, size): #For each index in range between 1 and the max size of length of the data list
        key = data[index] #the key is the data index
        j = index - 1 #j is equal to the index - 1
        while j >= 0 and data[j][0] > key [0]: #while j is greater than or equal to 0 and the data j and first column is greater than the key
            data[j + 1] = data[j] #the data will add the j + 1 is data j
            j -= 1 #j will decrement by 1
        data[j + 1] = key #then it will be replaced by the key
    return data #and return the data

def sorting(): #this is the junction function to joint together the entire program
    data = fetchData()  #this will fetch the data
    if data: #if the data is acquired
        print(f"Original Data (First Few Records):")
        for record in data[:5]: #For each record in data from index 0-5, it will print the record
            print(record)

        selection = dataSorting(data[:], len(data)) #This is the selection function being held as a variable to print
        print(f"\nData Sorted by Selection Sort (First few Records):") #For each record in data from index 0-5, it will print the record
        for record in selection[:5]:
            print(record)

        insertion = dataInsertionSort(data, len(data)) #This is the insertion function being held as a variable to print
        print(f"\nData Sorted by Insertion Sort (First few Records):") #For each record in data from index 0-5, it will print the record
        for record in insertion[:5]:
            print(record)

def main():
    while True:
        try:
            sorting()
            repeat = input("Would you like to continue?(Y|N)").upper()  
            if repeat != "Y".upper():
                print("program ended")
                break
        except ValueError:
            print("ValueError")
        except FileNotFoundError:
            print("File is not Found")
    
main()