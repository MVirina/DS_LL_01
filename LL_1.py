class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def middle(self):
        slow = self.head     # INITIALIZE slow and fast pointers to head of the linked list
        fast = self.head
        while fast and fast.next:    # WHILE fast is not None and fast.next is not None:
            slow = slow.next         # MOVE slow pointer one step (slow = slow.next)
            fast = fast.next.next    # MOVE fast pointer two steps (fast = fast.next.next)
        return slow    # RETURN slow pointer (middle node of the linked list)   
    

    # WRITE FIND_MIDDLE_NODE METHOD HERE # 
    #                                    #
    #                                    #
    #                                    #
    ######################################



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )

