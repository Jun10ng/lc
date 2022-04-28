import utils.tree
from utils.tree import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        retSum = 0
        def dfs(rn:TreeNode,cur:int):
            if rn:
                cur = cur*10 + int(rn.val)

            if not rn.left and not rn.right:
                nonlocal retSum
                retSum = retSum+cur
                return

            if rn.left:
                dfs(rn.left,cur)
            if rn.right:
                dfs(rn.right,cur)

        dfs(root,0)
        return retSum

if __name__ == '__main__':
    s = Solution()
    r = utils.tree.new_tree_from_level_str("[1,2,3]")
    x = s.sumNumbers(r)
    print(x)


