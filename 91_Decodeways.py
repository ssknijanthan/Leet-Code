class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n==1 and s[0]=='0':
            return 0
        elif n==1:
            return 1
        dp=[0]*(n+1)
        dp[n]=1
        if 1<=int(s[n-1])<10:
            dp[n-1]=1
        for i in range(n-2,-1,-1):
            if 1<=int(s[i])<10:
                dp[i]=dp[i+1]
            if s[i]!='0' and 10<=int(s[i]+s[i+1])<=26:
                dp[i]+=dp[i+2]
        return dp[0]




