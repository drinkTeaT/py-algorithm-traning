from common.common_class import ListNode, Generate, PrintUtil

root = ListNode(0)
root1 = ListNode(1)
root2 = ListNode(2)
root3 = ListNode(3)
root4 = ListNode(4)
root5 = ListNode(5)
root6 = ListNode(6)
root7 = ListNode(7)

root.next = root1
root1.next = root2
root2.next = root3
root3.next = root4
root4.next = root5
root5.next = root6
root6.next = root7


def do_reverse(last: ListNode, start: ListNode, end: ListNode):
    prev = None
    curr = start
    next_one = start.next
    p1 = end.next
    while next_one != end.next:
        curr.next = prev
        prev = curr
        curr = next_one
        next_one = next_one.next
    curr.next = prev
    last.next = curr
    start.next = p1


do_reverse(root1, root2, root5)
PrintUtil.print_nodes(root)
