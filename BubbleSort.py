# Bubble Sort Algorithm

def BubbleSort(arr, size):
    for i in range(1,size):
        for j in range(0,size-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


# array definition
array = []

size = int(input("Enter size of array: "))

for i in range(size):
    Element = int(input("Enter element: "))
    array.append(Element)

print("array before applying MERGE SORT: ",array)

BubbleSort(array,size)
print("array after applying MERGE SORT: ",array)