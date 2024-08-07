class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        col_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                # pop = stack.pop()
                # print(pop)
                if len(stack) == 0:
                    return False
                if  stack.pop() != col_map[c]:
                    return False
        if len(stack):
            return False
        return True 