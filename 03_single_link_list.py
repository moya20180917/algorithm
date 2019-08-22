
class Node(object):
    #节点
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    #每次定义完函数都要检测一下特殊情况，比如开始的时候是一个空链表

    #单向链表
    def __init__(self, node = None):
        #因为可以设置空的链表，所以我们设置一个默认参数node，指向头节点的位置
        #前面加双划线表示私有属性，这个类中的其他方法不需要调用这个属性
        self.__head = node

    def is_empty(self):
        #判断是否是空链表
        return self.__head == None

    def length(self):
        # 遍历整个链表
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count用来计数
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end = ' ')
            cur = cur.next
        print("")#表示换行

    def add(self, item):
        #在链表的头部添加元素，头插法
        node = Node(item)
        node.next = self.__head
        self.__head = node


    def append(self, item):
        #链接尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

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
        cur = self.__head
        pre = None
        #还没到最后的None的话
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next




    def search(self, item):
        #查找节点是否存在
        #检查一开始就是空列表的情况
        cur = self.__head
        flag = 0
        #for i in range(self.length()):
        while cur != None:
            if cur.elem == item:
                flag = 1
                cur = cur.next
            else:
                cur = cur.next
        # if flag == 1:
        #     print(f"{item} is in the linklist")
        # else:
        #     print(f"{item} is not in the linklist")
        if flag == 1:
            return True
        else:
            return False







node1 = Node(100)
node2 = Node(203)
node3 = Node(213)

ll = SingleLinkList()
print(ll.is_empty())
print(ll.length())
ll.append(1)
print(ll.is_empty())
print(ll.length())
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

ll.add(8)
ll.insert(9,90)


ll.travel()
print("")
print(ll.length())
ll.remove(2)

ll.travel()
print("")
print(ll.search(4))
ll.remove(8)
ll.travel()

ll.remove(1)
ll.travel()
ll.remove(90)
ll.travel()

