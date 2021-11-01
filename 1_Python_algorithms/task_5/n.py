

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)


def print_linked_list(n):
    while n:
        print(n.value, end='->')
        n = n.next
    print('None')

def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node

def insert_node(header, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = header
        return new_node
    prev = get_node_by_index(header, index-1)
    new_node.next = prev.next
    prev.next = new_node
    return header




#n3 = Node('third')
#n2 = Node('second', n3)
#n1 = Node('first', n2)

list_node = Node(1)
for i in range(1, 10):
    list_node = insert_node(list_node, i, 10*i)


print_linked_list(list_node)