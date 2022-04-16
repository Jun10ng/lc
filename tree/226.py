# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
import utils.tree
from utils.tree import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

if __name__ == '__main__':
    s = Solution()
    r = utils.tree.new_tree_from_level_str("[4,2,7,1,3,6,9]")
    res = s.invertTree(r)
    print(utils.tree.level_trace(res))
