def bubble_sort(alist):
    #冒泡排序法
    for i in range(len(alist)-1, 0, -1):
        #班长需要从头走到尾的次数
        count = 0
        for j in range(i):
            #班长从头走到尾的过程
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        if count == 0:
            return alist
    return alist


def bubble_sort2(alist):
    n = len(alist)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


ll = [2,3,1,4,6,5]
print(bubble_sort(ll))
print(bubble_sort2(ll))