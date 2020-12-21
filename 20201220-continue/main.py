from common.common_class import ListNode, Generate


class SwapNodesInPairs:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        k = 2
        prev = None
        p1 = head
        p2 = head.next
        res = None
        while p2 is not None:
            c = k
            while c > 2:
                c -= 1
                p2 = p2.next
                if p2 is None:
                    return res if res is not None else p1
            # 开始翻转
            self.__do_reverse(prev, p1, p2)
            prev = p1
            res = p2 if res is None else res
            p1 = p1.next
            if p1 is None:
                return res
            p2 = p1.next
        return res if res is not None else p1

    def __do_reverse(self, last: ListNode, start: ListNode, end: ListNode):
        prev = None
        p1 = start
        p2 = start.next
        tail = p1
        while p2 is not end.next:
            p1.next = prev
            prev = p1
            p1 = p2
            p2 = p2.next
        p1.next = prev
        if last is not None:
            last.next = p1
        tail.next = p2


node = Generate.create_nodes([1])
s = SwapNodesInPairs()
node = s.swapPairs(node)
while node is not None:
    print(node.val)
    node = node.next
