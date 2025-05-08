def add(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        number = arr.pop()
        return number + add(arr)
    
if __name__ == '__main__':
    arr = [2,4,6,10]
    print(add(arr))