from collections import Counter


class Node:
    def __init__(self,value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value 


def get_code(head, codes=dict(), code=''):
    if head is None:
        return
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    
    get_code(head.left, codes, code+'0')
    get_code(head.right, codes, code+'1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)
    
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        
        string_count = {node: 1}
    
    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]

        string_count[node] = spam[0][1] + spam[1][1]
    
    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for el in string:
        res += codes[el]
        #res += ' '
    
    return res

def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for j in codes:
            if string[i:].find(codes[j]) == 0:
                res += j
                i += len(codes[j])
    
    return res



string = input()

tree = get_tree(string)

codes = get_code(tree)

print(codes)

coding_str = coding(string, codes)

print(coding_str)


# decoding_str = decoding(coding_str, codes)
#
# print(decoding_str)


