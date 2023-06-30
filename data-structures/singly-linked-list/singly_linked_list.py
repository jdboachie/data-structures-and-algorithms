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

    def count_occurences_iterative(self, key: any) -> None:
        cur = self.head
        occurrences = 0

        while cur:
            if cur.data == key:
                occurrences += 1
            cur = cur.next

        return occurrences

    def count_occurences_recursive(self, node: Node, key: any) -> None:
        if not node:
            return 0
        if node.data == key:
            return 1 + self.count_occurences_recursive(node.next, key)
        else:
            return self.count_occurences_recursive(node.next, key)

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

    def is_palindrome(self, ) -> None:
        # STRING METHOD
        # s = ""
        # p = self.head
        # while p:
        #     s += p.data
        #     p = p.next
        # return s == s[::-1]

        # TWO POINTERS METHOD
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1

            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

    def length(self, node: Node) -> int:
        if node is None:
            return 0
        return 1 + self.length(node.next)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def move_tail_to_head(self) -> None:
        if self.head and self.head.next:
            last = self.head
            second_to_last = None

            while last.next:
                second_to_last = last
                last = last.next

            last.next = self.head
            second_to_last.next = None
            self.head = last

    def print_nth_from_last(self, n: int) -> any:
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if (count >= n):
                    break
                q = q.next

            if not q:
                print(f"{n} > length of LinkedList")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None

    def prepend(self, data: any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self, ) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_duplicates(self, ) -> None:
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

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

    def reverse_iterative(self, ):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def reverse_recursive(self, ):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        result = LinkedList()

        while p or q or carry:
            sum = carry

            if p:
                sum += p.data
                p = p.next

            if q:
                sum += q.data
                q = q.next

            carry = sum // 10
            digit = sum % 10
            result.append(digit)

        return result

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
