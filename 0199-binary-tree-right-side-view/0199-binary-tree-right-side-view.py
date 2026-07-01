# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def rev_postorder(root,level,ans):
            if root is None:
                return 
            if len(ans)==level:
                ans.append(root.val)
            rev_postorder(root.right,level+1,ans)
            rev_postorder(root.left,level+1,ans)
        rev_postorder(root,0,ans)
        return(ans)

        