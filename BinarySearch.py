# Binary Search Algorithm

array = [10,20,30,40,50,60,70,80,90,100]

def BinarySearch(a,start,end,ele):
    a.sort()
    mid = (start+end)//2

    if ele == a[mid]:
        return "Element position is ", mid
    elif ele < a[mid]:
        return BinarySearch(a,start,mid-1,ele)
    elif ele > a[mid]:
        return BinarySearch(a,mid+1,end,ele)

Element = int(input("Enter element: "))
result = BinarySearch(array,0,len(array)-1,Element)
print(result)