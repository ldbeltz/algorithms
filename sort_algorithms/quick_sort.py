def select_smaller(pivot, arr):
    smaller_then_pivot = []
    for i in range(len(arr)):
        if arr[i] <= pivot:
            smaller_then_pivot.append(arr[i])
    return smaller_then_pivot

def select_higher(pivot, arr):
    higher_then_pivot = []
    for i in range(len(arr)):
        if arr[i] > pivot:
            higher_then_pivot.append(arr[i])
    return higher_then_pivot

def quick_sort1(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller_then_pivot =  select_smaller(pivot, arr[1:])
        higher_then_pivot =  select_higher(pivot, arr[1:])
        return quick_sort(smaller_then_pivot) + [pivot] + quick_sort(higher_then_pivot)
        
def quick_sort(array): #Book version
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smaller = [i for i in array[1:] if i <= pivot]
        higher = [i for i in array[1:] if i > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(higher)
    
if __name__ == '__main__':
    unsorted_array = [100,3,91,7,92,8,89,10,82,20,77,55,64,59,6]
    sorted_array   = [3,6,7,8,10,20,55,59,64,77,82,89,92,91,100]
    inverted_array = [100,91,92,89,82,77,64,59,55,20,10,8,7,6,3]
    
    print(f"Unsorted: {quick_sort1(unsorted_array)}")
    print(f"Inverted: {quick_sort1(inverted_array)}")
    print(f"Sorted:   {quick_sort1(sorted_array)}")    