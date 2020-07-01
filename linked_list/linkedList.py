"""
Theory Video Reference: https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK 

Linked List Definition: 

Key Attributes:
- Dynamic size
- Ease of insertion/deletion
- Random access is not allowed
- Extra memory space is required with each element of the list
- Arrays have better cache locality

implement (I did with tail pointer & without):
 -size() - returns number of data elements in list
 -empty() - bool returns true if empty
 -value_at(index) - returns the value of the nth item (starting at 0 for first)
 -push_front(value) - adds an item to the front of the list
 -pop_front() - remove front item and return its value
 -push_back(value) - adds an item at the end
 -pop_back() - removes end item and returns its value
 -front() - get value of front item
 -back() - get value of end item
 -insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
 -erase(index) - removes node at given index
 -value_n_from_end(n) - returns the value of the node at nth position from the end of the list
 -reverse() - reverses the list
 -remove_value(value) - removes the first item in the list with this value
"""
class Node:
    """
    Node class for linked list w/ value(key) and next pointer (next)
    val = key value
    next = pointer to the next node
    """
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SLinkedList:
    """
    Singly Linked List in Python
    """
    def __init__(self):
        self.head = None
        self.n = 0  # initialize with zero size

    def __len__(self):
        """
        Return the number of elements in the list
        """
        return self.n

    def __str__(self):
        """
        Print items in the linked list
        """
        temp = "head"
        temp_node = self.head
        while temp_node is not None:
            temp += f' -> {temp_node.val}'
            temp_node = temp_node.next
        temp += f'-> None'
        return temp

    def push_back(self, item):
        """
        Adds an item at the end of the list.
        """
        new_node = Node(item)  # first create a node
        # if the list is empty, make it head
        if self.head is None:
            self.head = new_node
        else:
            # else, travel till the end 
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            # make last node to point to new_node
            temp_node.next = new_node
        self.n += 1  # increment no. of items

    def push_front(self, item):
        """
        Adds an item at the front of the list.
        """
        new_node = Node(item)
        # if the list is empty, make it head
        if self.head is None:
            self.head = new_node
        # else, 
        else:
            new_node.next = self.head  # new node points to current head
            self.head = new_node  # current head points to new_node
        self.n += 1

    def pop_front(self):
        """
        Remove front item and return its value
        """
        if self.n==0:
            print("Error; empty list")
            return
        else:
            temp = self.head  # retrieve front node
            self.head = temp.next.next # assign head to the second node
            self.n -= 1
        return temp.val
    
    def pop_back(self):
        """
        Remove item from the back and return its value
        """
        if self.n==0:
            print("Error; empty list")
            return
        else:
            temp_node = self.head
            # until temp_node is final-1 node
            while temp_node.next.next is not None:
                temp_node = temp_node.next
            temp_node = None
            self.n -= 1 # decrement
            return temp_node.next.val

    def is_empty(self):
        """
        Returns true if the list is empty
        """
        return self.n==0

    def value_at(self, index):
        """
        returns the value of the nth item (starting at 0)
        """
        if index==0:
            return self.head.val

        temp_node = self.head
        for _ in range(self.n):
            temp_node = temp_node.next
        return temp_node.val
        

if __name__=="__main__":
    llist = SLinkedList()
    llist.push_back("Mon")  # llist.head = Node("mon")

    # Create more nodes
    # e2 = Node("Tue")
    # e3 = Node("Wed")

    # Link them
    llist.push_back("Tue")  # llist.head.next = e2
    llist.push_back("Wed")  # e2.next = e3

    # Display linked list
    print(llist)

    # push_back
    llist.push_back("Thurs")
    print(f"\nNo. of items = {llist.n}")
    print(llist)

    # push front
    llist.push_front("Sun")
    print(f"\nNo. of items = {llist.n}")
    print(llist)

    # pop front
    temp = llist.pop_front()
    print(f"\nNo. of items = {llist.n}")
    print(f"poped item = {temp}")
    print(llist)

    # pop back
    temp = llist.pop_front()
    print(f"\nNo. of items = {llist.n}")
    print(f"poped item = {temp}")
    print(llist)