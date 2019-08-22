
def merge_sort(alist):
    #归并排序
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    #merge left_li and right_li
    left_pointer, right_pointer =0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        #如果是小于等于则是稳定的，如果是小于则不是稳定的
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result



ll = [2,3,1,4,6,5]
#接受返回值，返回排序好的新列表
sorted = merge_sort(ll)
print(sorted)