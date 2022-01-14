
# class Solution(object):
#         def integerBreak(self, n):
#             if n <= 2:
#                 return 1
#             if n == 3:
#                 return 2 + 1
        
#             numThree = n // 3
#             numTwos = 9

#             if n % 3 == 1:
#                 numThree -= 1
#                 numTwos = 2
#             elif n % 3 == 2:
#                 numTwos = 1

#             return (2**numTwos) * (3**numThree) 


class Solution(object):
    def __init__(self):
        self.memoize = {}
    
    def integerBreak(self, n):
        if n <= 2:
            return 1
        
        if n in self.memoize:
            return self.memoize[n]
        
        ans = 1 * (n - 1)
        for i in range(2, n):
            firstNum = i + 1
            secondNum = n - i
            product = firstNum * max(secondNum, self.integerBreak(secondNum))
            if product > ans:
                ans = product
            
        self.memoize[n] = ans
        
        return ans