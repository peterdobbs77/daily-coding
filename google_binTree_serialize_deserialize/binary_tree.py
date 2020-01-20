import string


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    global s
    if(root != None):
        s.append(root.val)
        serialize(root.left)
        serialize(root.right)
    else:
        s.append('None')
    return str(s).strip('[]')


# def deserialize(s):
#     l = list(s.split(', ')


s = []
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))


# ultimate test
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
