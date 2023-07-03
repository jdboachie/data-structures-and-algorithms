"""
Doubly-linked List
"""


class Node:
    def __init__(self, data: any) -> None:
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                node = Node(data)
                nxt = cur.next
                node.next = nxt
                node.prev = cur
                nxt.prev = node
                return
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                node = Node(data)
                prev = cur.prev
                cur.prev = node
                node.next = cur
                node.prev = prev
                return
            cur = cur.next

    def append(self, data: any) -> None:
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def delete(self, key: any):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # CASE 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # CASE 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # CASE 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                
                # CASE 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def prepend(self, data: any) -> None:
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def print_list(self) -> None:
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.reverse()
dllist.print_list()