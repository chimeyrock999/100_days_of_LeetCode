# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinVal(self, root: TreeNode) -> int:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # if not root.val:
        #     return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                minRightVal = self.findMinVal(root.right)
                root.val = minRightVal
                root.right = self.deleteNode(root.right, minRightVal)
        return root
