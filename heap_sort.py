# !/user/bin/env python
# - *- coding:utf-8 -*-
# user:peter


def heapify(alist, n, i):
    # 单个子树的堆化过程
    
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max = i
    if c1 < n and alist[c1] > alist[max]:
        max = c1
    if c2 < n and alist[c2] > alist[max]:
        max = c2
    if max != i:
        alist[max], alist[i] = alist[i], alist[max]
        heapify(alist, n, max)


def build_heap(alist, n):
    # 整个堆的建立
    last_node = n - 1  # 最后一个节点的下标
    parent = int((last_node - 1) / 2)  # 父节点下标
    for i in range(parent + 1, -1, -1):  # 构建节点的下标递减1
        heapify(alist, n, i)  # 递归构建堆


def heap_sort(alist, n):
    # 堆排序
    # 将根节点和最后的节点的值进行交换，取出根节点的值（大）
    # 此时破坏了堆的结构，重新构建堆，调用heapify()
    build_heap(alist, n)
    for i in range(n - 1, -1, -1):
        alist[i], alist[0] = alist[0], alist[i]
        heapify(alist, i, 0)
    
    return alist


alist = [3, 9, 2, 8, 7, 4, 6, 1, 5, 10]
res = heap_sort(alist, 10)
print(res)