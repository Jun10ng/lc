from typing import List

from utils.tree import *


#  给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[str]]:
        if root is None:
            return []
        res, segRes = [],[]
        preNodeq,curNodeq = [],[]

        preNodeq.append(root)
        res.append([root.val])
        while len(preNodeq) != 0:
            t = preNodeq.pop(0)

            if t.left is not None:
                curNodeq.append(t.left)
                segRes.append(t.left.val)
            if t.right is not None:
                curNodeq.append(t.right)
                segRes.append(t.right.val)

#                 next level
            if len(preNodeq) is 0 and len(segRes) is not 0:
                res.append(segRes)
                segRes = []
                preNodeq,curNodeq = curNodeq,[]

        return res



if __name__ =='__main__':
    s = Solution()
    level = '[3,9,20,null,null,15,7]'
    r = new_tree_from_level_str(level)
    # print(level_trace(r))
    print(s.levelOrder(r))

    level = '[1,2,3,4,5]'
    r = new_tree_from_level_str(level)
    print(level_trace(r))
    print(s.levelOrder(r))