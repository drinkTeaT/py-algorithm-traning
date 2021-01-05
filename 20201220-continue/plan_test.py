from common.common_class import ListNode


class LianBiaoZhongDaoShuDiGe:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        p1 = head
        p2 = head.next
        while k > 1 and p2 is not None:
            k -= 1
            p2 = p2.next
        if k != 1:
            return None
        while p2 is not None:
            p1 = p1.next
            p2 = p2.next
        return p1
