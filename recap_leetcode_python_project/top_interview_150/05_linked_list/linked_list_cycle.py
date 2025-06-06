from ll_util.ll_util import LinkedList
class Solution(object):
    """
    >>> Solution.hasCycle(Solution,[3,2,0,-4],1)
    True
    >>> Solution.hasCycle(Solution,[1,2],0)
    True
    >>> Solution.hasCycle(Solution,[1,2,4,5,6,7], None)
    False
    """

    def hasCycle(self, head, pos=None):
        ll = LinkedList()
        ll.make_linked_list(head, pos)
        ll.display()
        head = ll.head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

