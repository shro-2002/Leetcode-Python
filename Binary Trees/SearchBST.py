# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search(node):
            if node is None:
                return None
            
            if val==node.val:
                return node
            elif(val<node.val):
                return search(node.left)
            elif (val>node.val):
                return search(node.right)
            else:
                return None
            
            

        ans=search(root)
        return ans


        