
class Node(object):
    #节点
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    #每次定义完函数都要检测一下特殊情况，比如开始的时候是一个空链表

    #单向链表
    def __init__(self, node = None):
        #因为可以设置空的链表，所以我们设置一个默认参数node，指向头节点的位置
        #前面加双划线表示私有属性，这个类中的其他方法不需要调用这个属性
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        #判断是否是空链表
        return self.__head == None

    def length(self):
        # 遍历整个链表
        if self.is_empty():
            return 0
        else:
            # cur游标，用来移动遍历节点
            cur = self.__head
            # count用来计数
            count = 1 #循环的条件变了，所以从1开始
            #while cur != None:
            while cur.next != self.__head:#如果下一次又回到了头部，即完成遍历
                count += 1
                cur = cur.next
            return count

    def travel(self):
        if self.is_empty():
            return
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem, end = ' ')
                cur = cur.next
            #退出循环的时候cur指向尾节点，但是尾节点的元素未被打印
            print(cur.elem)
            print("")#表示换行,与print("\n")一致

    def add(self, item):
        #在链表的头部添加元素，头插法
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环的时候cur指向尾节点
            node.next = self.__head
            self.__head = node
            cur.next = node


        # node.next = self.__head
        # self.__head = node


    def append(self, item):
        #链接尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        #指定位置添加元素
        node = Node(item)
        #如果是在第一个位置之前添加，则可以直接用add方法
        if pos <= 0:
            self.add(item)
        # 如果是在最后一个位置以后添加，则可以直接用append方法
        elif pos > (self.length()-1):
            self.append(item)
        else:
            #往中间位置插入的话跟单链表是一样的
            cur = self.__head
            count = 0
            #要在第i个位置插入，实际上就是取代第i个元素，因此需要是pos-1
            while count < (pos-1):
                cur = cur.next
                count += 1
            #当循环退出后，cur停在pos-1位置
            node.next = cur.next
            cur.next = node

    # def remove(self, item):
    #     #删除节点
    #     if self.search(item):
    #         cur2 = self.__head
    #         #如果需要删除的是第一个元素
    #         if cur2.elem == item:
    #             self.__head = cur2.next
    #         else:
    #             cur = self.__head
    #             while cur.elem != item:
    #                 if cur.next.elem == item:
    #                     pre = cur
    #                 cur = cur.next
    #             pre.next = cur.next
    #     else:
    #         print(f"there is no {item} in the linklist")

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self.__head
            pre = None
            #还没到最后的None的话
            while cur.next != self.__head:
                if cur.elem == item:
                    #恰巧这个节点是头节点的时候，要去查找尾节点
                    if cur == self.__head:
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head

                        #self.__head = cur.next
                    else:
                        #中间的节点与单链表一样
                        pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # 退出循环的时候，cur指向尾节点
            if cur.elem == item:
                if cur == self.__head:
                    #如果这个链表只有一个节点，因为它没办法进入循环，所以就是self.__head
                    self.__head = None
                else:
                    pre.next = cur.next




    def search(self, item):
        #查找节点是否存在
        #检查一开始就是空列表的情况
        if self.is_empty():
            flag = 0
        else:
            cur = self.__head
            flag = 0
            #for i in range(self.length()):
            while cur.next != self.__head:
                if cur.elem == item:
                    flag = 1
                    cur = cur.next
                else:
                    cur = cur.next
            #退出循环的时候，cur指向尾节点
            if cur.elem == item:
                flag = 1

        # if flag == 1:
        #     print(f"{item} is in the linklist")
        # else:
        #     print(f"{item} is not in the linklist")
        if flag == 1:
            return True
        else:
            return False







# node1 = Node(100)
# node2 = Node(203)
# node3 = Node(213)

ll = SingleCycleLinkList()
ll.add(1)
ll.add(2)
ll.append(3)
ll.insert(2,4)
ll.insert(4,5)
ll.insert(0,6)
print(f"The length is {ll.length()}")
ll.travel()
print(ll.search(3))
print(ll.search(7))
ll.remove(1)
ll.remove(6)
print(f"The length is {ll.length()}")
ll.travel()


