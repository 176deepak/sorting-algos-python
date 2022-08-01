# Counting Sort Algorithm


from itertools import count


def max(arr, n):
    max = arr[0]
    for i in range(1,n):
        if max < arr[i]:
            max = arr[i]
    return max

def CountingSort(arr,n):
    output = [None]*n
    count = max(arr, n)
    count_array = [0]*(count+1)
    
    for i in range(n):
        count_array[arr[i]]+= 1

    for i in range(1, count+1):
        count_array[i]+= count_array[i-1]

    for i in range(n,0,-1):
        output[count_array[arr[i-1]] - 1] = arr[i-1];  
        count_array[arr[i-1]]-= 1
    
    for i in range(n):
        arr[i] = output[i]

# array definition
array = []

size = int(input("Enter size of array: "))

for i in range(size):
    Element = int(input("Enter element: "))
    array.append(Element)

print("array before applying COUNTING SORT: ",array)

CountingSort(array, size)
print("array before applying COUNTING SORT: ",array)