class Node(object):
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.left: Node = None
        self.right: Node = None


class BST(object):
    def __init__(self, root):
        self.root: Node = Node(root)

    def insert(self, val: any) -> None:

        def insert_helper(current: Node, val: any):
            if current.data < val:
                if current.right:
                    insert_helper(current.right, val)
                else:
                    current.right = Node(val)
            else:
                if current.left:
                    insert_helper(current.left, val)
                else:
                    current.left = Node(val)

        return insert_helper(self.root, val)

    def search(self, val: any) -> bool:

        def search_helper(current, val):
            if current:
                if current.data == val:
                    return True
                elif current.data < val:
                    return search_helper(current.right, val)
                else:
                    return search_helper(current.left, val)

        return search_helper(self.root, val)

    def is_bst_satisfied(self) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            if node.data < min_val or node.data > max_val:
                return False
            return helper(node.left, min_val, node.data - 1) and helper(node.right, node.data + 1, max_val)
        return helper(self.root, float('-inf'), float('inf'))


bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))
