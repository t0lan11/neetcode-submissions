# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = [[root.val]]
        depth = 0

        def helper(curr, depth):
            if not curr:
                return None
            if len(result) == depth:
                result.append([])
            result[depth].append(curr.val)
            helper(curr.left, depth + 1)
            helper(curr.right, depth + 1)

        helper(root.left, depth + 1)
        helper(root.right, depth + 1)
        return result