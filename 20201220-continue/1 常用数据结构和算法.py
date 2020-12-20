# 242. 有效的字母异位词 https://leetcode-cn.com/problems/valid-anagram/
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        s_map = {}
        for i in s:
            count = s_map.get(i)
            if count is None:
                s_map[i] = 1
            else:
                s_map[i] = count + 1
        for i in t:
            count = s_map.get(i)
            if count is None:
                return False
            else:
                if count == 1:
                    s_map.pop(i)
                else:
                    s_map[i] = count - 1
        return len(s_map) == 0
