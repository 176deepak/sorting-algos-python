#Selection Sort Algorithm

def min(arr, size, k):
    min = arr[k]
    loc = k
    for i in range(k+1,size):
        if (min > arr[i]):
            min = arr[i]
            loc = i
    return loc

def SelectionSort(arr, size):
    for i in range(size):
        loc = min(arr, size,i)
        temp = arr[i]
        arr[i] = arr[loc]
        arr[loc] = temp

# array definition
array = []

size = int(input("Enter size of array: "))

for i in range(size):
    Element = int(input("Enter element: "))
    array.append(Element)

print("array before applying SELECTION SORT: ",array)

SelectionSort(array, size)
print("array before applying SELECTION SORT: ",array)
