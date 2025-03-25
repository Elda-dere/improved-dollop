class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        total=[]
        nums=['(',')']
        stack=[]
        def backtrack(res,opening_count,closing_count):
            if len(res)==2*n and not stack:
                total.append(''.join(res))
                return

            if opening_count < n:
                res.append('(')
                backtrack(res,opening_count+1,closing_count)
                res.pop()
            if closing_count < opening_count:
                res.append(')')
                backtrack(res,opening_count,closing_count+1)
                res.pop()

        backtrack([],0,0)
        return total
                
            