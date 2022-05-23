# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
#  路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#
#
from typing import Optional

import utils.tree
from utils.tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        if not root:return cnt

        def track(tn:TreeNode) -> []:
            nonlocal cnt
            if not tn.right and not tn.left:
                if tn.val == targetSum:cnt+=1
                return [tn.val]
            ret = []

            if tn.left:
                ret = ret + track(tn.left)
            if tn.right:
                ret = ret + track(tn.right)

            i = 0

            for e in ret:
                x= e+tn.val
                if x == targetSum:cnt+=1
                ret[i],i=x,i+1

            ret.append(tn.val)
            if tn.val == targetSum:cnt+=1
            return ret

        track(root)

        return cnt
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    # 3
    x = s.pathSum(utils.tree.new_tree_from_level_str("[5,4,8,11,null,13,4,7,2,null,null,5,1]"),22)
    print(x)
    # 1
    x = s.pathSum(utils.tree.new_tree_from_level_str("[1]"),1)
    print(x)
    # 1
    x = s.pathSum(utils.tree.new_tree_from_level_str("[1,2]"),1)
    print(x)
