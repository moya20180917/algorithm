def quick_sort(alist, first, last):

    # 传进来的first和last如果是相等的话，要操作的只有一个元素，那么我们直接返回
    if first >= last:
        return

    low = first
    high = last
    mid_value = alist[first]

    while low < high:
        #碰到与mid_value相等的元素还是继续往左走，也就是相同的元素都放在右边high那里
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    #利用递归的思想
    # quick_sort(alist[:low-1])
    # quick_sort(alist[low+1:])
    #对low左边的列表进行快速排序
    quick_sort(alist, first, low-1)
    #对low右边的列表进行快速排序
    quick_sort(alist, low+1, last)


ll = [2,3,1,4,6,5]
quick_sort(ll, 0, len(ll)-1)
print(ll)

