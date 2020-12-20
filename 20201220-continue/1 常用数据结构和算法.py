from common.common_class import ListNode


# 242. 有效的字母异位词 https://leetcode-cn.com/problems/valid-anagram/
class ValidAnagram:
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


# 剑指 Offer 24. 反转链表 https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
class FanZhuanLianBiao:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        prev = None
        p1 = head
        p2 = p1.next
        while p2 is not None:
            p1.next = prev
            prev = p1
            p1 = p2
            p2 = p2.next
        p1.next = prev
        return p1
