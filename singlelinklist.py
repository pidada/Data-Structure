#!/user/bin/env python
#- *- coding:utf-8 -*-
# user:peter

# 定义节点类
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
    
    def is_empty(self):
        return self.__head == None
    
    def length(self):
        # 遍历整个链表
        # cur游标，用来移动遍历节点；初始值设为头部的值
        cur = self.__head
        # count记录数量
        # 特殊情形：若链表是空的，cur = self._head = None，不进入while循环，count=0直接返回
        count = 0
        while cur != None:
            count += 1
            # 移动
            cur = cur.next
        return count
    
    def travel(self):
        # 遍历：打印每个节点的数据
        cur = self.__head
        while cur != None:
            # 游标所指的当前节点的数据
            # end属性：使用空格不换行，默认是换行\n
            print(cur.elem, end=" ")
            # 移动
            cur = cur.next
        print("")
    
    def add(self, item):
        # 头部插入元素
        # 实例构造节点
        node = Node(item)
        # 将节点的next值指向最初__head的值
        node.next = self.__head
        # 将创建的节点的值node赋给self.__head
        self.__head = node
    
    def append(self, item):
        # 尾部插入元素
        # item是传入的具体元素，通过实例存入节点中
        node = Node(item)
        # 考虑空列表的情况
        if self.is_empty():
            # 如果为空，直接指向节点node
            self.__head = node
        else:
            cur = self.__head
            # 只要cur的next区域不是None，则一直进行
            while cur.next != None:
                cur = cur.next
            # 添加节点
            cur.next = node
    
    def insert(self, pos, item):
        """
        指定位置添加：指定位置pos的前一个位置添加
        pos：从0开始

        """
        # 如果pos <= 0，相当于是pos=0，看做是在头部插入add方法
        if pos <= 0:
            self.add(item)
        # 如果pos比链表最后一个元素的位置还大，默认看做是在尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node
    
    def remove(self, item):
        """
        删除节点
        使用两个游标：pre和cur；最开始pre指向None，cur指向head
        """
        cur = self.__head
        pre = None
        # 终止条件：走到最后，直至每个元素都有被遍历
        # 空链表为None，不执行任何操作
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 如果是头节点：pre == None或者cur == self.__head
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    
    def search(self, item):
        #  判断是否存在某个数据item：存在返回T，否则F
        # 如果直接是空链表，也可以进行处理，直接返回F
        cur = self.__head
        # while cur.next != None：如果这样写，最后一个元素的next为空，那么最后的元素将不能进入while循环，导致最后的元素没有进行遍历
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    li = SingleLinkList()
    print(li.is_empty())
    print(li.length())
    
    li.append(1)
    print(li.is_empty())
    print(li.length())
    
    li.append(2)
    li.append(3)
    li.append(4)
    # 插入在头部
    li.add(8)
    li.append(5)
    li.append(6)
    li.insert(-1, 9)
    li.travel()
    li.insert(4, 11)
    li.travel()
    li.insert(15, 12)
    li.travel()
    li.remove(9)
    li.travel()
    li.remove(4)
    li.travel()
    li.remove(12)