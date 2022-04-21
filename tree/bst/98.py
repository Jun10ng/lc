# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 输入：root = [2,1,3]
# 输出：true
import sys

import utils.tree
from utils.tree import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = -sys.maxsize -1
        def trace(root) -> bool:
            nonlocal pre
            if not root:
                return True
            if not trace(root.left): return False
            if pre >= int(root.val): # 但是整数变量却不行呢？
                return False
            else:
                pre = int(root.val)
            if not trace(root.right):return False
            return True

        return trace(root)


if __name__ == '__main__':
    s = Solution()
    r = utils.tree.new_tree_from_level_str("[5,4,6,null,null,3,7]")
    print(s.isValidBST(r))