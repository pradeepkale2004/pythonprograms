class Solution:
    def getDivisors(self, n):
        for i in range (1,n+1):
            if n % i ==0:
                print(i,end =' ')

s1 = Solution()
s1.getDivisors(20)