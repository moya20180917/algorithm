class Deque(object):
    #双端队列
    def __init__(self):
        self.__list = []#创建一个私有容器

        # 如果出队的频率比入队的频率大得多，那就从列表的尾部弹出，头部进入队列
        # 反之的话，就从头部弹出，尾部进入，与具体的应用相关
    def add_front(self, item):
        # 头部进队列
        # self.__list.append(item)
        self.__list.insert(0, item)

    def add_rear(self, item):
        # 尾部进队列
        self.__list.append(item)
        #self.__list.insert(0, item)

    def remove_front(self):
        # 出队列，头部出队列
        return self.__list.pop(0)
        # self.__list.pop()

    def remove_rear(self):
        return self.__list.pop()

    def is_empty(self):
        # 判断是否为空
        return self.__list == []

    def size(self):
        # 返回队列的大小
        return len(self.__list)

s = Deque()
s.add_front(1)
s.add_front(2)
s.add_rear(3)
s.add_rear(4)
print(s.size())
 
# print(s.peek())
print(s.remove_front())
print(s.remove_front())
print(s.remove_rear())
print(s.remove_rear())