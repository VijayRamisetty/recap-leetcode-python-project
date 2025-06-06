import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def make_linked_list(self, arr, pos=None): # if pos given, stores last node.next with pos node's address
        for x in arr:
            self.add_node(x)

        if pos is not None:
            lookup = {}
            i = 0
            cur = self.head
            lookup[0] = cur.next
            logger.info(lookup)
            while cur.next:
                i += 1
                lookup[i] = cur.next
                cur = cur.next

                if i == 10:
                    break
                logger.info(lookup)
            cur.next = lookup[pos]

    def add_node(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return

        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            return

    def display(self):
        dummy = self.head
        i = 0
        while dummy:
            logger.info(f'{dummy.val} >')
            dummy = dummy.next
            i += 1
            if i == 10:  # just added to break for looped linked lists
                break
        return


if __name__ == '__main__':
    ll = LinkedList()
    ll.make_linked_list([3, 2, 0, -4], pos=1)
    ll.display()
