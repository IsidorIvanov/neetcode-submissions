class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        recnik = {}
        for ch in s:
            recnik[ch] = recnik.get(ch,0) + 1
        for ch in t:
            if ch not in recnik or recnik[ch]==0:
                return False
            recnik[ch]-=1
        return True