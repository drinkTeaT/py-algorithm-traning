# 20. 有效的括号 https://leetcode-cn.com/problems/valid-parentheses/
class ValidParentheses:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
        my_stack = list()
        for i in s:
            if i == "(" or i == "[" or i == "{":
                my_stack.append(i)
            elif len(my_stack) == 0:
                return False
            elif i == ")":
                if my_stack.pop() != "(":
                    return False
            elif i == "]":
                if my_stack.pop() != "[":
                    return False
            else:
                if my_stack.pop() != "{":
                    return False
        return len(my_stack) == 0
