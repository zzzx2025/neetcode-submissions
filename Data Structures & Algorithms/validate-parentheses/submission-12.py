class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        num = len(s)%2
        if num == 1:
            return False
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                arr.append(ch)
                #print(arr)
            elif ch == "}":
                if len(arr) != 0 and arr[-1] == "{":
                    arr.pop()
                else:
                    return False
                #print(arr)
            elif ch == "]":
                if len(arr) != 0 and arr[-1] == "[":
                    arr.pop()
                else:
                    return False
                #print(arr)
            elif ch == ")":
                if len(arr) != 0 and arr[-1] == "(":
                    arr.pop()
                else:
                    return False
            else: 
                #print(arr)
                return False
        if not arr:
            return True
        else:
            return False

        """
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack"""