class Node:
    def __init__(self,value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value 

class Tree:
    def __init__(self):
        self.head = None
    
    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            now_node = self.head
            while True:
                if now_node.value >= node.value:
                    if now_node.left is None:
                        now_node.left = node
                        break
                    now_node = now_node.left
                else:
                    if now_node.right is None:
                        now_node.right = node
                        break
                    now_node = now_node.right
            
def print_tree(node, path=True):
    print(node.value)
    if node.left:
        if node.value > node.left.value:
            path = print_tree(node.left, path)
        else:
            return False
    if node.right:
        if node.value < node.right.value:
            path = print_tree(node.right, path)
        else:
            return False
    return path
        
root = Tree()

n_list = [
    Node(15),
    Node(13),
    Node(14),
    Node(11),
    Node(7),
    Node(17),
]

for i in range(len(n_list)):
    root.add_node(n_list[i])

print_tree(root.head)