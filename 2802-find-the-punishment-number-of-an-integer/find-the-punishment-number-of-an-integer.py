class Solution:
    def punishmentNumber(self, n: int) -> int:
        def punshiment(start_index,current_sum,string,target):
            if start_index==len(string) :
                return target==current_sum
            if current_sum > target:
                return False

            for i in range(start_index,len(string)):

                appened=string[start_index:i+1]
                app_int=int(appened)

                if punshiment(i+1,current_sum+app_int,string,target):
                    return True
            return False


        res=0
        for i in range(1,n+1):
            string=str(i**2)

            if punshiment(0,0,string,i):
                res+=i**2
        return res
        


