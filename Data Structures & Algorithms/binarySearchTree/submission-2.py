class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left, self.right = None, None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = Node(key, val)
            return

        curr = self.root
        while True:
            if curr.key < key:
                if not curr.right:
                    curr.right = Node(key, val)
                    return
                curr = curr.right
            elif curr.key > key:
                if not curr.left:
                    curr.left = Node(key, val)
                    return
                curr = curr.left
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.left
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        def _remove(root, key: int) -> Optional[Node]:
            if not root:
                return root

            if root.key < key:
                root.right = _remove(root.right, key)
            elif root.key > key:
                root.left = _remove(root.left, key)
            else:
                ## 0 or 1 children
                if not root.left or not root.right:
                    return root.left or root.right
                
                ## 2 children
                # find min node from right subtree
                minNode = root.right
                while minNode.left:
                    minNode = minNode.left
                
                # replace root attributes
                root.key, root.val = minNode.key, minNode.val

                # remove replacement node from right subtree
                root.right = _remove(root.right, root.key)

            return root

        self.root = _remove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        keys = []
        
        def inorder_dfs(node):
            if not node: return
            inorder_dfs(node.left)
            keys.append(node.key)
            inorder_dfs(node.right)

        inorder_dfs(self.root)
        return keys
