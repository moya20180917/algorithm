class Queue(object):
    def __init__(self):
        self.__list = []

    #如果出队的频率比入队的频率大得多，那就从列表的尾部弹出，头部进入队列
    #反之的话，就从头部弹出，尾部进入，与具体的应用相关
    def enqueue(self, item):
        #进队列,尾部进队列
        self.__list.append(item)
        #self.__list.insert(0, item)


    def dequeue(self):
        #出队列，头部出队列
        return self.__list.pop(0)
        #self.__list.pop()

    def is_empty(self):
        #判断是否为空
        return self.__list == []

    def size(self):
        #返回队列的大小
        return len(self.__list)



s = Queue()
s.enqueue("Hello")
s.enqueue("World")
s.enqueue("Itcast")
print(s.size())
# print(s.peek())
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())