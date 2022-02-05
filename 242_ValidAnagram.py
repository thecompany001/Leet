class Solution(object):
    def isAnagram(self, s, t):
        if len(S) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)   
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True