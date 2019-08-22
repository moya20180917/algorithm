def binary_search(alist, item):
    #二分查找,递归版本
    n = len(alist)
    if n > 0:
        mid = n // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False



def binary_search_2(alist,item):
    #二分法查找，非递归的方式
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        elif item > alist[mid]:
            first = mid + 1
    return False







ll = [1,2,3,4,5,6,7]
print(binary_search(ll,3))
print(binary_search(ll,10))
print(binary_search_2(ll,4))
print(binary_search_2(ll,10))
