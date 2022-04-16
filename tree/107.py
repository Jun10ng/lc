# 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
from typing import List

from utils.tree import TreeNode, new_tree_from_level_str, level_trace


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        result = []
        preLevel, curLevel = [],[]

        # push root node
        preLevel.append(root)
        # result.append([root.val])
        level = []
        while len(preLevel) != 0:
            tn = preLevel.pop(0)
            level.append(tn.val)

            if tn.left is not None:
                curLevel.append(tn.left)
            if tn.right is not None:
                curLevel.append(tn.right)

            # replace preLevel when end of preLevel
            if len(preLevel) == 0:
                result.insert(0,level)
                preLevel,curLevel,level = curLevel,[],[]

        return result


if __name__ =='__main__':
    s = Solution()
    level = '[3,9,20,null,null,15,7]'
    r = new_tree_from_level_str(level)
    # print(level_trace(r))
    print(s.levelOrderBottom(r))

    level = '[1,2,3,4,5]'
    r = new_tree_from_level_str(level)
    # print(level_trace(r))
    print(s.levelOrderBottom(r))