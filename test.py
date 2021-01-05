from common.common_class import Generate, PrintUtil

nodes = Generate.create_nodes([1, 2, 3, 4, 5])


def do_solve(head):
    prev = None
    curr = head
    next_one = head.next
    while next_one is not None:
        curr.next = prev
        prev = curr
        curr = next_one
        next_one = next_one.next
    curr.next = prev
    PrintUtil.print_nodes(curr)


do_solve(nodes)
