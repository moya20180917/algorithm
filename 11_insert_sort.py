
def insert_sort(alist):
    n = len(alist)
    #因为我们假设前面的序列是有序的，那实际上我们排序是从index=1也就是第二个元素开始
    #外层循环表示从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1,n):#1<=j<=n-1
        # i代表内层循环的起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素， 即i'位置的元素，然后将其插入到前面的正确位置当中
        while i > 0:
            if alist[i] <  alist[i-1]:
                alist[i-1], alist[i] = alist[i], alist[i-1]
                i -= 1
            else:
                break


ll = [2,3,1,4,6,5]
insert_sort(ll)
print(ll)
