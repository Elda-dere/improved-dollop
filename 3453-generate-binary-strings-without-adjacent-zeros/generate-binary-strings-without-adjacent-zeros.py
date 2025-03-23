class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def generate(idx,string):
            if len(string)==n:
             
                res.append(''.join(string))
                return
            string.append("1")
            generate(idx+1,string)
            string.pop()
            if not string or string[-1]=="1":
              
                string.append("0")
                generate(idx+1,string)
                string.pop()

            
              
            return res
        return generate(0,[])