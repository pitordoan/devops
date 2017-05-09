
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

def binary_search_smallest(root):
    node = Node(0)

    def binary_search_smallest_recursive(root, node):
        if root == None:
            return node.data
        else:
            if root.data > node.data:
                return binary_search_smallest_recursive(root.l_child, root)
            else:
                return binary_search_smallest_recursive(root.r_child, root)

    return binary_search_smallest_recursive(root, node)

def binary_search_largest(root):
    node = Node(0)
    node.root = root

    def binary_search_largest_recursive(root, node):
        if root == None:
            return node.data
        else:
            if root.data < node.data:

                return binary_search_largest_recursive(root.l_child, root)
            else:
                return binary_search_largest_recursive(root.r_child, root)

    return binary_search_largest_recursive(root, node)


def binary_search_second_largest(root):
    parent_node = None

    def binary_search_largest_recursive(node, parent_node):
        if node == None:
            return parent_node
        else:
            if parent_node == None or node.data > parent_node.data:
                node.parent = parent_node
                return binary_search_largest_recursive(node.r_child, node)
            else:
                node.parent = parent_node
                return binary_search_largest_recursive(node.l_child, node)

    max_node = binary_search_largest_recursive(root, parent_node)
    if max_node == root or max_node.l_child != None:
        return binary_search_largest_recursive(max_node.l_child, max_node).data
    else:
        return max_node.parent.data

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

print "\nFind second largest:"
print binary_search_second_largest(r)