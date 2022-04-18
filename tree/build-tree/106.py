from typing import Optional
from typing import List


import utils.tree
from utils.tree import TreeNode
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并
# 返回这颗 二叉树 。

# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) is 0 or len(postorder) is 0:
            return None

        pLastIdx = len(postorder)-1
        root = TreeNode(postorder[pLastIdx])
        rootIdxAtInOrder = inorder.index(postorder[pLastIdx])
        root.left = self.buildTree(inorder[:rootIdxAtInOrder],postorder[:rootIdxAtInOrder])
        root.right = self.buildTree(inorder[rootIdxAtInOrder+1:],postorder[rootIdxAtInOrder:len(postorder)-1])
        return root

if __name__ == '__main__':
        s = Solution()
        r = s.buildTree([9,3,15,20,7],[9,15,7,20,3])
        print(utils.tree.level_trace(r))
        # root = utils.tree.new_tree_from_level_str(str)
        # print(s.maxDepth(root))
