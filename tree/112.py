# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和
#  targetSum 。如果存在，返回 true ；否则，返回 false 。
#
#  叶子节点 是指没有子节点的节点。
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。
#
from collections import defaultdict
from typing import Optional, List

import utils.tree
from utils.tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum = targetSum - int(root.val)
        if targetSum == 0 and not root.right and not root.left:
            return True


        if root.left:
            if self.hasPathSum(root.left, targetSum):
                return True

        if root.right:
            if self.hasPathSum(root.right, targetSum):
                return True

        return False


if __name__ == '__main__':
    # s = Solution()
    # level = '[5,4,8,11,null,13,4,7,2,null,null,null,1]'
    # r = utils.tree.new_tree_from_level_str(level)
    # print(s.hasPathSum(r, 22))

    s = Solution()
    level = '[-2,null,-3]'
    r = utils.tree.new_tree_from_level_str(level)
    print(s.hasPathSum(r, -5))