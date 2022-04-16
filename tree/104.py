
# 给定一个二叉树，找出其最大深度。
#
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最大深度 3 。
from typing import Optional

import utils.tree
from utils.tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.dive(root,0)

    def dive(self,root,h) -> int:
        if root is None:
            return h
        rh = self.dive(root.right,h+1)
        lh = self.dive(root.left,h+1)
        return rh if rh > lh else lh

if __name__ == '__main__':
    s = Solution()
    str = "[3,9,20,null,null,15,7]"
    root = utils.tree.new_tree_from_level_str(str)
    print(s.maxDepth(root))