class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        track=[]
        nums=["a","b","c"]
        
        def backtrack(res):
            if len(res)==n:
                
                track.append(''.join(res[:]))
                return
            
            for i in range(len(nums)):
                if not res or nums[i] != res[-1] :
                    res.append(nums[i])
                 
                    backtrack(res)
                    res.pop()
             
        backtrack([])
        
        if k<=len(track):
            return track[k-1]
        else:
            return ""