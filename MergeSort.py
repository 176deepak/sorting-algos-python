# Merge Sort Algorithm

# Merge function - merging two listed into sorted order
def Merge(arr,lb,mid,ub):
    global size
    i = lb
    j = mid+1
    k = lb
    sort_rray = [None] * (ub+1)

    while (i <= mid) and (j <= ub):
        if arr[i] <= arr[j]:
            sort_rray[k] = arr[i]
            i+= 1
        else:
            sort_rray[k] = arr[j]
            j+= 1
        k+= 1
    if i > mid:
        while j <= ub:
            sort_rray[k] = array[j]
            j+= 1
            k+= 1
    else:
        while i <= mid:
            sort_rray[k] = array[i]
            i+= 1
            k+= 1
    
    for i in range(lb,ub+1):
        array[i] = sort_rray[i]

# MergeSort - divide an array into parts
def MergeSort(arr,lb,ub):
    if lb < ub:
        mid = (lb+ub)//2
        MergeSort(arr,lb,mid)
        MergeSort(arr,mid+1,ub)
        Merge(arr,lb,mid,ub)


# array definition
array = []

size = int(input("Enter size of array: "))

for i in range(size):
    Element = int(input("Enter element: "))
    array.append(Element)

print("array before applying MERGE SORT: ",array)

MergeSort(array, 0, size-1)
print("array after MERGE SORT: ", array)