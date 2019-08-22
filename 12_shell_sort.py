
def shell_sort(alist):
    #希尔排序
    n = len(alist)
    gap = n // 2 #一开始按照长度的一半来取
    #起始值，原先是从1开始，因为原来的步长相当于1，而现在也是从步长gap开始
    #gap变化到0之前，插入算法执行的次数
    while gap >0:
        #插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap, n):
            #j = [gap, gap+1, gap+2,....n-1]
            i = j
            #这里不再是与之前的一个元素去对比了，而是与相隔gap的元素做对比
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        #缩短gap的步长
        gap //= 2


ll = [2,3,1,4,6,5]
shell_sort(ll)
print(ll)
