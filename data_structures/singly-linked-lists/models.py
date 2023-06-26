"""
Node
LinkedList
"""


class Node:

    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, ) -> None:
        self.head = None

    def append(self, data: any) -> None:
        new_node = Node(data)

        # CASE 0: Empty LinkedList
        if self.head is None:
            self.head = new_node
            return

        # CASE 1: None-empty LinkedList
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key: any) -> None:

        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is not None:
            prev.next = current_node.next
            current_node = None

    def delete_node_at_pos(self, pos: int) -> None:

        if self.head:
            current_node = self.head
            if pos == 0:
                self.head = current_node.next
                current_node = Node
                return

            prev = None
            count = 0
            while current_node and count != pos:
                prev = current_node
                current_node = current_node.next
                count += 1

            if current_node is not None:
                prev.next = current_node.next
                current_node = None

    def insert_after_node(self, prev: Node, data: any) -> None:
        if not prev:
            print(f"Previous node ({prev}) does not exist")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def length(self, node: Node) -> int:
        if node is None:
            return 0
        return 1 + self.length(node.next)

    def preprend(self, data: any) -> None:
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def print_list(self, ) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse_iterative(self, ) -> None:
        prev = None
        cur = self.head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self, ) -> None:

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Original List")
llist.print_list()

llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.print_list()
