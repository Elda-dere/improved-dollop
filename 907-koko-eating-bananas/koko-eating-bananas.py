class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        def yigreme(middle):
            sum_value=0
            hours=0
            for i in range(len(piles)):
                 
              
                hours+=ceil(piles[i]/middle)
               
            return hours <=h
                
                
                
        weights=piles
        low=1
        high=max(weights)
        while low <= high:
            mid=(low+high)//2
           
            if yigreme(mid):
             
                high=mid-1
            else:
                low=mid+1
        return low            