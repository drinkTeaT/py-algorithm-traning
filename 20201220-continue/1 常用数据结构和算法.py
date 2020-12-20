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


# 剑指 Offer 22. 链表中倒数第k个节点 https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
class LianBiaoZhongDaoShuDiGe:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        p1 = head
        p2 = head
        while k > 1:
            p2 = p2.next
            if p2 is None:
                return None
            k -= 1
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        return p1


# 141. 环形链表 https://leetcode-cn.com/problems/linked-list-cycle/
class LinkedListCycle:
    def hasCycle(self, head: ListNode) -> bool:
        node_set = set()
        while head is not None:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False


# 24. 两两交换链表中的节点 https://leetcode-cn.com/problems/swap-nodes-in-pairs/
class SwapNodesInPairs:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        prev = None
        res = p2
        while p2 is not None:
            temp = p2.next
            p2.next = p1
            if prev is not None:
                prev.next = p2
            prev = p1
            p1 = temp
            if p1 is None:
                prev.next = p1
                return res
            p2 = p1.next
        prev.next = p1
        return res
