class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        total=[]
      
        def backtrack(starting_index,part):
            
           
            if len(part)==4:
                if len(s)==starting_index:
                    total.append(".".join(part))
                return 
            
            for i in range(1,4):
                if starting_index + i >len(s):
                    break

                   
                string=s[starting_index:i+starting_index]
                

                if int(string) > 255 or (len(string) >1 and string[0]=="0"):
                    continue
                part.append(string)
                backtrack(starting_index+i,part)
                part.pop()
            
            
            
        if len(s)>=4 and len(s)<=12:

            backtrack(0,[])
            return total
        else:
            return []


                    
                    


         