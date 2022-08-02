# QUICK SORT ALGORITHM

def partition(arr, lb, ub):
    start = lb
    end = ub
    loc = lb
    flag = False
    while(not flag):
        while (arr[loc] <= arr[end]) and (loc != end):
            end-= 1
            if (loc == end):
                flag = True
            elif arr[loc] > arr[end]:
                temp = arr[loc]
                arr[loc] = arr[end]
                arr[end] = temp 
                loc = end
            
            if (not flag):
                while((arr[loc] >= arr[start]) and (loc != start)):
                    start+= 1
                    if loc == start:    
                        flag = True
                    elif arr[loc] < arr[start]:
                        temp = arr[loc]
                        arr[loc] = arr[start]
                        arr[start] = temp
                        loc = start
    return loc

def QuickSort(arr, lb, ub):
    if lb < ub:
        p = partition(arr, lb, ub)
        QuickSort(arr, lb, p-1)
        QuickSort(arr, p+1, ub)
# array definition
array = []

size = int(input("Enter size of array: "))

for i in range(size):
    Element = int(input("Enter element: "))
    array.append(Element)

print("array before applying QUICK SORT: ",array)

QuickSort(array, 0, size-1)
print("array after applying QUICK SORT: ",array)
