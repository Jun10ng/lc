import re
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = int(val)
        self.left = left
        self.right = right

# ldr_str and pre_str are strings like "[1,null,2,3]" with ldr/中序 and pre/先序
def new_tree_from_str_ldr_and_pre(ldr_str,pre_str):
    str_len = len(ldr_str)
    ldr_str = ldr_str[1:str_len-1]
    pre_str = pre_str[1:str_len-1]
    return new_tree_from_array_ldr_and_pre(ldr_str.split(','),pre_str.split(','))

# ldr_str and pre_str are strings array like ["1","null","2","3"] with ldr/中序 and pre/先序
def new_tree_from_array_ldr_and_pre(ldr,pre):
    # traceback exit condition
    if len(pre)==0 or len(ldr) == 0:
        return
    # print("pre: %v \n",pre)
    # print("ldr: %v \n",ldr)
    root_val,root_node =pre[0],TreeNode(pre[0])
    root_index_on_ldr = ldr.index(root_val)

    # build
    root_node.left = new_tree_from_array_ldr_and_pre(ldr[0:root_index_on_ldr], pre[1:])
    root_node.right = new_tree_from_array_ldr_and_pre(ldr[root_index_on_ldr+1:], pre[root_index_on_ldr+1:])

    return root_node

# print tree node in level trace
def level_trace(tree_node):
    node_queue = []
    result = []
    node_queue.append(tree_node)

    while len(node_queue)!=0:
        node = node_queue.pop(0)
        result.append(node.val)
        if node.left != None:
            node_queue.append(node.left)
        if node.right != None:
            node_queue.append(node.right) 

    return result

# build a tree from level str likes '[1,null,2,3]'
def new_tree_from_level_str(level_str):
    level_array = level_str[1:len(level_str)-1].split(',')
    pre_node_q = []
    pre_node_q.append(TreeNode(level_array.pop(0)))
    return_root = pre_node_q[0]

    while len(level_array) != 0:
        # left
        elem = level_array.pop(0)
        if elem != 'null':
            t = TreeNode(elem)
            pre_node_q.append(t)
            # print("l is ",elem)
            pre_node_q[0].left = t
         
        if len(level_array)==0:
            break
        
        # right 
        elem = level_array.pop(0)
        if elem != 'null':
            t = TreeNode(elem)
            pre_node_q.append(t)
            # print("r is ",elem)

            pre_node_q[0].right = t

        # next pre_node
        pre_node_q.pop(0)   

    return return_root    




# ldr 1 null 2 3 
# pre 1 null 3 2

if __name__ == '__main__':

    # run with `python3 tree.py 1`
    test_case = sys.argv[1]

    # `python3 tree.py 1` build tree with ldr and pre
    # and print it in level
    if test_case == '1':
        ldr = '[2,6,4,1,5,7,3]'
        pre = '[1,2,4,6,3,5,7]'
        r = new_tree_from_str_ldr_and_pre(ldr,pre)
        print(level_trace(r))

    # `python3 tree.py 2` build tree with level
    # and print it in level
    if test_case == '2':
        level_str = '[1,null,2,3]'
        r = new_tree_from_level_str(level_str)
        print(level_trace(r))
        