import sys
sys.path.append('..')
from utils.LinkedList import Node, LinkedList

### Merge sorted linked lists

def merge_lists(L1, L2):
    head = tail = Node(0)
    
    while L1 and L2:
        if L1.value < L2.value:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

    # the remaining node
    tail.next = L1 or L2
    return head.next


