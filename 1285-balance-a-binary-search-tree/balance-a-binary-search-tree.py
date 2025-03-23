# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        nums=[]
        def funct(root):
            if root is None:
                return 
            funct(root.left)
            nums.append(root.val)
            funct(root.right)
            return nums
            
        list_t=funct(root)
        n=len(list_t)-1
        def sec(start,end,nums):
            if start > end:
                return None 
            mid=(start+end)//2
            root=TreeNode(nums[mid])
            root.left=sec(start,mid-1,nums)
            root.right=sec(mid+1,end,nums)
            return root
        return sec(0,n,nums)
