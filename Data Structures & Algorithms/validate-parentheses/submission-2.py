class Solution:
    def isValid(self, s: str) -> bool:
        lista = []
        recnik = {
        ')':'(',
        ']':'[',
        '}':'{'
        }
        for ch in s:
            if ch in recnik:
                if not lista or recnik[ch]!=lista[-1]:
                    return False
                lista.pop()
            else:
                lista.append(ch)
        return len(lista)==0