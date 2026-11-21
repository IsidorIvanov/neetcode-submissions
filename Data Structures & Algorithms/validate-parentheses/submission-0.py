class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in pairs:  # ako je zatvorena zagrada
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:            # ako je otvorena zagrada
                stack.append(ch)
                
        return len(stack) == 0