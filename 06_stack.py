class Stack(object):
    def __init__(self):
        #封装成私有的一个容器
        self.__list = []

    def push(self, item):
        #添加一个新的元素item到栈顶
        #我们既可以用列表的第一个元素进行操作，也可以用最后一个元素操作
        #但是对于顺序表来说，操作最后一个元素的时间复杂度是O(1)，第一个元素是O(n)
        #如果使用单链表的话，操作头元素的时间复杂度更低
        self.__list.append(item)
        #self.__list.insert(0, item)

    def pop(self):
        #弹出栈顶的元素
        return self.__list.pop()#默认是从队尾弹出
        #self.__list.pop(0)

    def peek(self):
        #返回栈顶元素
        #判断是不是一个空列表
        if self.__list:
            return self.__list[-1]
        else:
            return None


    def is_empty(self):
        return self.__list == []


    def size(self):
        return len(self.__list)


s = Stack()
s.push("Hello")
s.push("World")
s.push("Itcast")
print(s.size())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())