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
# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用0 来代替。
# 例如，给定一个列表temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是[1, 1, 4, 2, 1, 1, 0, 0]。
# 提示：气温 列表长度的范围是[1, 30000]。每个气温的值的均为华氏度，都是在[30, 100]范围内的整数。
# 向右遍历，如果遇到大于目前值则计算天数，小于或等于则记录至queue
class DailyTemperatures:
    def daily_temperatures(self, temps: List[int]) -> List[int]:
        if temps is None:
            return temps
        res = [0 for i in range(len(temps))]
        queue = []
        for i in range(len(temps)):
            while len(queue) != 0 and temps[i] > temps[queue[-1]]:
                res[queue.pop()] = i - queue[-1]
            queue.append(i)
        return res


# 84. 柱状图中最大的矩形 https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
# 输入: [2,1,5,6,2,3]
# 输出: 10
class LargestRectangle:
    def solve(self, heights: list[int]) -> int:
        return 0
