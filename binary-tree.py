
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

def binary_search_smallest(root):
    node = Node(0)

    def __binary_search_smallest_recursive(root, node):
        if root == None:
            return node.data
        else:
            if root.data > node.data:
                return __binary_search_smallest_recursive(root.l_child, root)
            else:
                return __binary_search_smallest_recursive(root.r_child, root)

    return __binary_search_smallest_recursive(root, node)

def binary_search_largest(root):
    node = Node(0)

    def __binary_search_smallest_recursive(root, node):
        if root == None:
            return node.data
        else:
            if root.data < node.data:
                return __binary_search_smallest_recursive(root.l_child, root)
            else:
                return __binary_search_smallest_recursive(root.r_child, root)

    return __binary_search_smallest_recursive(root, node)

r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))
binary_insert(r, Node(10))
binary_insert(r, Node(4))

print "In order:"
in_order_print(r)

print "\nPre order:"
pre_order_print(r)

print "\nFind smallest:"
print binary_search_smallest(r)

print "\nFind largest:"
print binary_search_largest(r)
