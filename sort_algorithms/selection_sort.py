def selection_sort(array) -> list:
    sorted_array = [] #starts the reusult array empty
    for i in range(len(array)):
        smallest_num = array[0] # assume that first number is the smallest
        smallest_index = 0 
        for j in range(1, len(array)): #starts the second loop in the next number
            if array[j] < smallest_num:
                smallest_num = array[j] #if the next number is smaller then the current number then the new smallest number is the next
                smallest_index = j
        sorted_array.append(array.pop(smallest_index)) #At the end of the loop the smallest_number is removed from the main array and added to the result array.
    return sorted_array

if __name__ == '__main__':
    unsorted_array = [100,3,91,7,92,8,89,10,82,20,77,55,64,59,6]
    sorted_array   = [3,6,7,8,10,20,55,59,64,77,82,89,92,91,100]
    inverted_array = [100,91,92,89,82,77,64,59,55,20,10,8,7,6,3]
    
    print(f"Unsorted: {selection_sort(unsorted_array)}")
    print(f"Inverted: {selection_sort(inverted_array)}")
    print(f"Sorted:   {selection_sort(sorted_array)}")