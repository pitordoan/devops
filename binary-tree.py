
class Node:
    def __init__(self, val):
        self.parent = None
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

def get_min_node(root):
    def get_min_node_recurse(node):
        if node == None or node.r_child == None:
            return node

        next_node = node.l_child
        next_node.parent = node
        return get_min_node_recurse(next_node)

    return get_min_node_recurse(root)

def get_max_node(root):
    def get_max_node_recurse(node):
        if node == None or node.r_child == None:
            return node

        next_node = node.r_child
        next_node.parent = node
        return get_max_node_recurse(next_node)

    return get_max_node_recurse(root)

def get_second_max_node(root):
    max_node = get_max_node(root)

    if max_node == root and max_node.l_child == None:
        return max_node
    elif max_node.l_child != None:
        return get_second_max_node(max_node.l_child)

    return max_node.parent

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
print get_min_node(r).data

print "\nFind largest:"
print get_max_node(r).data

print "\nFind second largest:"
print get_second_max_node(r).data