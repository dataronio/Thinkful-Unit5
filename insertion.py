def insertion(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            #print(arr)
            j -= 1
        i += 1
    return arr

z = [6,5,3,1,8,7,2,4]
print("unsorted array = ", z)
print("Sorted array = ",insertion(z))
