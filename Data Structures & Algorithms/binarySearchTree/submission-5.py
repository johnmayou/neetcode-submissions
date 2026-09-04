class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class TreeMap:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, key: int, val: int) -> None:
        def insert(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return Node(key, val)
            
            if key < node.key:
                node.left = insert(node.left)
            elif key > node.key:
                node.right = insert(node.right)
            else:
                node.val = val

            return node

        self.root = insert(self.root)

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        def remove(node: Optional[Node], k: int) -> None:
            if not node:
                return

            if k < node.key:
                node.left = remove(node.left, k)
            elif k > node.key:
                node.right = remove(node.right, k)
            else:
                if not node.left or not node.right:
                    return node.left or node.right

                min_node = node.right
                while min_node.left:
                    min_node = min_node.left

                node.key = min_node.key
                node.val = min_node.val
                node.right = remove(node.right, min_node.key)

            return node

        self.root = remove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        result: list[int] = []

        def dfs(node: Optional[Node]) -> None:
            if not node:
                return

            dfs(node.left)
            result.append(node.key)
            dfs(node.right)

        dfs(self.root)
        return result