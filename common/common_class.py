class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Generate:
    @staticmethod
    def create_nodes(nodes: list) -> ListNode:
        if nodes is None or len(nodes) == 0:
            return None
        root = ListNode(nodes[0])
        node = root
        i = 1
        while i < len(nodes):
            node.next = ListNode(nodes[i])
            node = node.next
            i += 1
        return root


class PrintUtil:
    @staticmethod
    def print_nodes(head: ListNode):
        while head is not None:
            print(head.val)
            head = head.next
