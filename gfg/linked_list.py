class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print("")

    def add_node(self, val):
        print("adding a node at start")
        n = Node(val)

        if self.head is None:
            self.head = n

        else:
            n.next = self.head
            self.head = n

    def add_at_pos(self, val, pos):
        print("adding a node at position")
        n = Node(val)

        if self.head is None:
            self.head = n
            return

        if pos == 0:
            n.next = self.head
            self.head = n

        if self.head.next is None:
            self.head = n
            return

        count = 1
        nod = self.head
        while nod.next:
            if count == pos-1:
                temp = nod.next # 8
                nod.next = n
                n.next = temp
                return

            count += 1
            nod = nod.next

        if count == pos:
            nod.next = n

    def add_after_a_node(self, val, prev):
        print("adding a node after a node")
        n = Node(val)

        n.next = prev.next
        prev.next = n

    def add_at_end(self, val):
        print("adding a node at end")
        n = Node(val)

        if self.head is None:
            self.head = n
            return

        nod = self.head
        while nod.next:
            nod = nod.next

        nod.next = n

    def del_from_start(self):
        print("delete a node at start")
        temp = self.head
        self.head = self.head.next
        del temp

    def del_from_end(self):
        print("delete a node at end")
        temp = None
        end = self.head
        while end.next:
            temp = end
            end = end.next

        temp.next = None
        del end

    def del_from_pos(self, pos):
        print("delete a node at position")

        if pos == 0:
            temp = self.head
            self.head = self.head.next
            del temp
            return

        count = 1
        nod = self.head
        while nod.next:
            if count == pos - 1:
                temp = nod.next
                nod.next = temp.next
                del temp
                return
            nod = nod.next
            count += 1

        if count == pos:
            temp = nod.next.next
            nod.next = nod.next.next
            del temp



# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.add_at_end(6)
    llist.printList()

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.add_node(7)
    llist.printList()

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.add_node(1)
    llist.printList()

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.add_at_end(4)
    llist.printList()

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.add_after_a_node(8, llist.head.next)
    llist.printList()

    # Insert 5, at position 2. So linked list becomes 1 -> 5 -> 7-> 8-> 6-> 4-> None
    llist.add_at_pos(5, 2)
    llist.printList()

    llist.del_from_start()
    llist.printList()

    llist.del_from_end()
    llist.printList()

    llist.del_from_pos(2)
    llist.printList()
