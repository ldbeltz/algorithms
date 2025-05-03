def binary_search(sorted_array, value) -> int: #The algorithm recieves a sorted_array and a value to be searched, it should return the index of the value in the array
    smaller_number = 0  #index position of the smaller number of the array
    highest_number = len(sorted_array) - 1  #index position of the highest number of the array
    while smaller_number <= highest_number:
        middle_number = (highest_number + smaller_number) // 2
        if sorted_array[middle_number] == value:
            return middle_number
        if sorted_array[middle_number] < value:
            smaller_number = middle_number + 1
        else:
            highest_number = middle_number - 1
    return None
if __name__ == '__main__':
    sorted_array = [3,6,7,8,10,20,55,59,64,77,82,89,92,91,100]
    found_index = binary_search(sorted_array, -1)
    print(found_index)