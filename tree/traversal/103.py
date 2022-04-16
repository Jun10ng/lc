# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
from typing import List

from utils.tree import TreeNode, new_tree_from_level_str


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res, level = [],[]
        preNodeQ, curNodeQ = [],[]

        preNodeQ.append(root)
        # 第几层的节点
        levelNum = 1
        while len(preNodeQ) != 0:
            t = preNodeQ.pop(0)
            if levelNum%2 == 1:
                level.append(t.val)
            else:
                level.insert(0,t.val)

            if t.left is not None:
                curNodeQ.append(t.left)
            if t.right is not None:
                curNodeQ.append(t.right)

            if len(preNodeQ) == 0:
                res.append(level)
                level,levelNum = [], levelNum+1
                preNodeQ,curNodeQ = curNodeQ,[]

        return res

if __name__ == '__main__':
    s = Solution()
    root = new_tree_from_level_str("[3,9,20,null,null,15,7]")
    x = s.zigzagLevelOrder(root)
    print(x)