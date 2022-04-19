# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
#  叶子节点 是指没有子节点的节点。

# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#
from typing import Optional,List

import utils.tree
from utils.tree import TreeNode
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dive(tn: TreeNode, t: int, rcd: List[int]):
            if not tn:
                return
            t = t - int(tn.val)
            rcd.append(tn.val)
            if not tn.right and not tn.left and t is 0:
                cpy = rcd.copy()
                res.append(cpy)
            #   这里不要return 否则第一条路径之后
            #   否则逻辑走不到30行去处理rcd

            dive(tn.left,t,rcd)
            dive(tn.right,t,rcd)
            rcd.pop(len(rcd)-1)

        dive(root,targetSum,[])
        return res


if __name__ == '__main__':
    s = Solution()
    r = utils.tree.new_tree_from_level_str("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    print(s.pathSum(r,22))