class Solution(object):
    def passwordStrength(self, password):
        output = 0
        for ch in set(password):
            if 'a'<= ch <= 'z':
                output += 1
            elif 'A' <= ch <= 'Z':
                output += 2
            elif '0' <= ch <= '9':
                output += 3
            elif ch in "!@#$":
                output += 5 
        return output

