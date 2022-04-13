# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
from typing import List

from utils.tree import TreeNode, new_tree_from_level_str, level_trace


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        rootIndexAtInorder = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:rootIndexAtInorder+1],inorder[:rootIndexAtInorder])
        root.right = self.buildTree(preorder[rootIndexAtInorder+1:],inorder[rootIndexAtInorder+1:])
        return root

if __name__ =='__main__':
    s = Solution()
    level = '[3,9,20,null,null,15,7]'
    r = s.buildTree([3,9,20,15,7],[9,3,15,20,7])
    print(level_trace(r))
