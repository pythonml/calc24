import math
import itertools

class Node(object):
    def __init__(self, result=None):
        self._left = None
        self._right = None
        self._operator = None
        self._result = result

    def set_expression(self, left_node, right_node, operator):
        self._left = left_node
        self._right = right_node
        self._operator = operator
        expression = "{} {} {}".format(left_node._result, operator, right_node._result)
        self._result = eval(expression)

    def __repr__(self):
        if self._operator:
            return '<Node operator="{}">'.format(self._operator)
        else:
            return '<Node value="{}">'.format(self._result)

def get_expression(tree):
    if tree._operator == None:
        return str(tree._result)
    left_expression = get_expression(tree._left)
    right_expression = get_expression(tree._right)
    expression = "({} {} {})".format(left_expression, tree._operator, right_expression)
    return expression

def build_tree(left_tree, right_tree):
    treelist = []
    tree1 = Node()
    tree1.set_expression(left_tree, right_tree, "+")
    treelist.append(tree1)
    tree2 = Node()
    tree2.set_expression(left_tree, right_tree, "-")
    treelist.append(tree2)
    tree4 = Node()
    tree4.set_expression(left_tree, right_tree, "*")
    treelist.append(tree4)
    if right_tree._result != 0:
        tree5 = Node()
        tree5.set_expression(left_tree, right_tree, "/")
        treelist.append(tree5)
    return treelist

def build_all_trees(array):
    if len(array) == 1:
        tree = Node(array[0])
        return [tree]

    treelist = []
    for i in range(1, len(array)):
        left_array = array[:i]
        right_array = array[i:]
        left_trees = build_all_trees(left_array)
        right_trees = build_all_trees(right_array)
        for left_tree in left_trees:
            for right_tree in right_trees:
                combined_trees = build_tree(left_tree, right_tree)
                treelist.extend(combined_trees)
    return treelist

if __name__ == "__main__":
    questions = [
        [7,7,3,3],
        [8,3,8,3],
        [5,1,5,5],
        [10,10,4,4],
        [1,5,7,10],
        [4,7,8,10],
        [2,2,3,10],
        [2,4,10,10],
        [9,10,6,9],
        [4,4,7,7],
        [1,4,5,6],
        [2,5,5,10]
    ]

    for question in questions:
        perms = itertools.permutations(question)
        found = False
        for perm in perms:
            treelist = build_all_trees(perm)
            for tree in treelist:
                if math.isclose(tree._result, 24, rel_tol=1e-10):
                    expression = get_expression(tree)
                    print(expression)
                    found = True
                    break
            if found:
                break
