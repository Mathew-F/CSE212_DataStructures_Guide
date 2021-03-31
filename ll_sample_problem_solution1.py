'''
This program goes over some of the basic functions used in a linked list
data structure just to make sure that we got the bascis down. The next sample problem
will implement our linked lists into a more real world example.

The __iter__ and __str__ functions were borrowed from another assignment previously completed.
'''
class LinkedList:
    class Node:
        def __init__(self, value):
            self.next = None
            self.previous = None
            self.data = value

    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_head(self, value):
        new_node = LinkedList.Node(value)

        if self.head == None: #Meaning if there is no head node. Usually because the list is empty.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.next.previous = new_node
            self.head = new_node

    def remove_head(self):
        self.head.next.previous = None
        self.head = self.head.next

    def insert_tail(self, value):
        new_node = LinkedList.Node(value)

        if self.tail == None: #There is no tail and so probably no head/Empty list.
            self.tail = new_node
            self.head = new_node
        else:
            new_node.previous = self.tail
            new_node.previous.next = new_node
            self.tail = new_node

    def insert_middle(self, value, value2):
        '''
        This will insert the new node after the first node with the value2
        '''
        current = self.head
        while current != None:
            if current == self.tail:
                self.insert_tail(value)
            elif (current.data == value2):
                new_node = LinkedList.Node(value)
                new_node.previous = current
                new_node.next = current.next
                current.next.previous = new_node
                current.next = new_node
                return
            else:
                current = current.next

    def delete_node(self, value):
        '''
        Deletes the node with the matching value.
        '''
        current = self.head
        while current != None:
            if current.data == value:
                current.previous.next = current.next
                current.next.previous = current.previous
                current.next = None
                current.previous = None
                return
            else:
                current = current.next

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        current = self.head  # Start at the begining since this is a forward iteration.
        while current is not None:
            yield current.data 
            current = current.next

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

print('\n----------Test Case #1-------------')
ll = LinkedList()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
print(ll)
#linkedlist[4,3,2,1]
print('\n----------Test Case #2-------------')
ll = LinkedList()
ll.insert_tail(1)
ll.insert_tail(2)
ll.insert_tail(3)
ll.insert_tail(4)
print(ll)
#linkedlist[1,2,3,4]
print('\n----------Test Case #3-------------')
ll.insert_middle(5,3)
ll.insert_middle(6,2)
print(ll)
#linkedlist[1,2,6,3,5,4]
print('\n----------Test Case #4-------------')
ll.delete_node(5)
ll.delete_node(6)
print(ll)
#linkedlist[1,2,3,4]