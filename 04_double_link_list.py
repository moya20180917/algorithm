class Node(object):
    #节点
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None

#其实前四个方法都是和单链接是一样的，因此可以直接可以继承，利用面向对象的思想
class DoubleLinkList(object):
    #双链表
    def __init__(self, node = None):
        #因为可以设置空的链表，所以我们设置一个默认参数node，指向头节点的位置
        #前面加双划线表示私有属性，这个类中的其他方法不需要调用这个属性
        self.__head = node

    def is_empty(self):
        #判断是否是空链表
        return self.__head == None

    def length(self):
        # 遍历整个链表,与单链表一样
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count用来计数
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 与单链表一样
        if self.is_empty():
            return
        else:
            cur = self.__head
            while cur != None:
                print(cur.elem, end=' ')
                cur = cur.next
            print("")  # 表示换行

    def add(self, item):
        #在链表的头部添加元素，头插法
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:

            node.next = self.__head
            self.__head = node
            node.next.prev = node



    def append(self, item):
        #链接尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
            #node.prev = None
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

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
            #要在第i个位置插入
            while count < (pos):
                cur = cur.next
                count += 1
            #当循环退出后，cur停在pos位置
            node.next = cur
            node.prev = cur.prev
            cur.prev = node
            node.prev.next = node

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
        #还没到最后的None的话
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    #位于首节点的特殊情况
                    self.__head = cur.next
                    if cur.next:#判断链表是否只有一个节点的情况
                        cur.next.prev = None#前继节点要设置为None

                else:
                    cur.prev.next = cur.next
                    if cur.next:#判断是否是删除链表中的最后一个节点，因为如果是最后的节点就没有cur.next
                        cur.next.prev = cur.prev
                break
            else:
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



ll = DoubleLinkList()

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