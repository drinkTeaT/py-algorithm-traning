from typing import List


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


# 739. 每日温度 https://leetcode-cn.com/problems/daily-temperatures/
class DailyTemperatures:
    def daily_temperatures(self, temps: List[int]) -> List[int]:
        if temps is None:
            return None
        length = len(temps)
        res = list(i * 0 for i in temps)
        my_stack = list()
        count = 0
        while count < length:
            if len(my_stack) == 0:
                my_stack.append(count)
            elif temps[my_stack[-1]] >= temps[count]:
                my_stack.append(count)
            else:
                while len(my_stack) > 0 and temps[count] > temps[my_stack[-1]]:
                    point = my_stack.pop(-1)
                    res[point] = count - point
                my_stack.append(count)
            count += 1
        return res
