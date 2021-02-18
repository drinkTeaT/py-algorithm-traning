# 给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 向右移动，遇到大于的加入，移除左侧值，遇到等于的加入，移除左侧值，遇到小于的
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
import collections
from typing import List


# 单调队列 向右走，如果队列空则加入，如果右边数大于等于队列中某个值，则移除该值及左侧的所有值，并加入，如果小于队列所有值直接加入，判断头是否有效，无效移除头，再选择头
class SlidingWindowMaximum:
    @staticmethod
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        queue = collections.deque()  # type : deque
        result = list()
        for i in range(0, len(nums)):
            while len(queue) != 0 and nums[queue[0]] <= nums[i]:
                queue.popleft()
            queue.appendleft(i)
            if queue[-1] <= i - k:
                queue.pop()
            if i + 1 >= k:
                result.append(nums[queue[-1]])
        return result


print(SlidingWindowMaximum.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
