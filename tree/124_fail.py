# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不
# 一定经过根节点。
#
#  路径和 是路径中各节点值的总和。
#
#  给你一个二叉树的根节点 root ，返回其 最大路径和 。

# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
import sys
from typing import Optional

import utils.tree
from utils.tree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = - sys.maxsize
        def track(tn: Optional[TreeNode]) -> int:
            nonlocal ret
            leftRet,rightRet = -sys.maxsize,-sys.maxsize
            maxNonIncluTn = tn.val

            if tn.left :
                leftRet = track(tn.left)
                if leftRet>0: maxNonIncluTn+= leftRet
            if tn.right:
                rightRet = track(tn.right)
                if rightRet >0: maxNonIncluTn += rightRet

            ret = max(ret,maxNonIncluTn)
            return max(max(0,rightRet), max(0,leftRet)) + tn.val


        track(root)
        return ret

if __name__ == '__main__':
    s = Solution()
    r = utils.tree.new_tree_from_level_str("[-10,9,20,null,null,15,7]")
    x = s.maxPathSum(r)
    print(x)

