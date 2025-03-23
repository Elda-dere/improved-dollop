class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #BACTTRACK
        res=[]
        def helper(nums,path):
            if len(path)== len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                helper(nums,path)
                path.pop()
            return res


        return helper(nums,[])
       