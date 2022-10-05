class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:

        seen = dict()
        ans = []
        
        for start, end in paint:
            amount = 0
            while start < end:
                
                if start in seen:
                    tmp = seen[start]
                    seen[start] = max(seen[start], end)
                    start = tmp
                else:
                    amount += 1
                    seen[start] = end
                    start += 1
                    
            ans.append(amount)
        return ans