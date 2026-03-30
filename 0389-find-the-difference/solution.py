class Solution(object):
   def findTheDifference(self,s, t):
    result = 0

    for ch in s + t:
        result ^= ord(ch)

    return chr(result)

s = "abcd"
t = "abcde"
obj = Solution()
print(obj.findTheDifference(s,t))

