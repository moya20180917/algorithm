def sel_sort(alist):
    n = len(alist)
    for j in range(n-1):#0<=j<=n-2 
        min_index = j
        for i in range(j+1, n):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


ll = [2,3,1,4,6,5]
sel_sort(ll)
print(ll)
