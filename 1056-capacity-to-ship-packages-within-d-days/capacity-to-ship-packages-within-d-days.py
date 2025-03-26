class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def yigreme(mid):
            sum_va=0
            day=1
            for i in range(len(weights)):
               
                if sum_va+weights[i] > mid:
                    day+=1
                    sum_va=weights[i]
                else:
                    sum_va+=weights[i]
            return day <= days
        low=max(weights)
        high=sum(weights)
        while low <= high:
            mid=(low+high)//2
            print(yigreme(mid))
            if yigreme(mid):
                print("h",yigreme(mid))
                high=mid-1
            else:
                low=mid+1
        return low                