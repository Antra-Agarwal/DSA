class Solution(object):
    def balancedStringSplit(self, s):
        s_lst = list(s)
        output = 0
        balance_count = 0
       

        for a in s_lst :
            if a == "L":
                balance_count += 1
            else :
                balance_count -= 1
            
            if balance_count == 0:
                output += 1
        return output

      
