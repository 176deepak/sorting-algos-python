# Insertion Sort Algorithm

# insertion sort function
def InsertionSort(arr,n):
    k = 1
    while(k <= n-1):
        temp = arr[k]
        j = k-1
        while((temp < arr[j]) and (j >= 0)):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
        k+= 1

array = []

size = int(input("Enter size of array: "))

for i in range(size):
    Element = int(input("Enter element: "))
    array.append(Element)

print("Array before INSERTION SORT: ",array)

InsertionSort(array,len(array))
print("Array after INSERTION SORT: ",array)