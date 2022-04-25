# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
import sys
from typing import Optional

import utils.tree
from utils.tree import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        lq = []
        wrongIdx = []
        first = True

        def findWrong(tn):
            if not tn:
                return

            findWrong(tn.left)
            lq.append(tn)
            findWrong(tn.right)

        findWrong(root)
        for i in range(len(lq)-1):
            if lq[i].val > lq[i+1].val:
                if first:
                    wrongIdx.append(i)
                    first = False
                else:
                    wrongIdx.append(i+1)


        if len(wrongIdx) == 1:
            lq[wrongIdx[0]+1].val,lq[wrongIdx[0]].val = lq[wrongIdx[0]].val,lq[wrongIdx[0]+1].val
        else:
            lq[wrongIdx[0]].val,lq[wrongIdx[1]].val = lq[wrongIdx[1]].val,lq[wrongIdx[0]].val

if __name__ == '__main__':
    s = Solution()
    r = utils.tree.new_tree_from_level_str("[3,1,4,null,null,2]")
    s.recoverTree(r)
    print(utils.tree.level_trace(r))
