def count_list(arr):
    if len(arr) <= 1:
        return len(arr)
    else:
        arr.pop()
        return 1 + count_list(arr)
    
if __name__ == '__main__':
    arr = [2,4,6,10]
    print(count_list(arr))