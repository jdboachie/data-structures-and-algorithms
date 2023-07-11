class Node(object):
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.left: Node = None
        self.right: Node = None


class BST(object):
    def __init__(self, root):
        self.root: Node = Node(root)

    def insert(self, val: any):

        def insert_helper(self, current: Node, val: any):
            if current.data < val:
                if current.right:
                    self.insert_helper(current.right, val)
                else:
                    current.right = Node(val)
            else:
                if current.left:
                    self.insert_helper(current.left, val)
                else:
                    current.left = Node(val)

        insert_helper(self.root, val)
