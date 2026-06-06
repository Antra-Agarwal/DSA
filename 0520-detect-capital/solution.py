class Solution(object):
    def detectCapitalUse(self, word):
        
        no_capital = 0
        for ch in word :
            if 'A' <= ch <= 'Z' :
                no_capital += 1

        if (no_capital == 0 or (no_capital == 1 and 'A' <= word[0] <= 'Z') or no_capital == len(word)):
            return True
        else :
            return False
