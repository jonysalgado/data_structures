class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        @cache
        def dp(i, l, n=len(nums)):
            if i == n: return 0
            
            ans = 0
            for j in range(numSlots):
                
                if l[j]<2:
                    ans = max(ans, ((j+1) & nums[i]) + dp(i+1, l[:j] + tuple([l[j]+1]) + l[j+1:]))
                    
            return ans

        return dp(0, tuple([0]*numSlots))