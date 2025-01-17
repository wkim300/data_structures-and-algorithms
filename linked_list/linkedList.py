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
            self.head = temp.next # assign head to the second node
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
            temp = temp_node.next
            temp_node.next = None  # reset the tail node
            self.n -= 1 # decrement
            return temp.val

    def front(self):
        """
        Returns front item
        """
        if self.head is None:
            print("Error: empty list!")
            return
        return self.head.val

    def back(self):
        """
        Returns back item
        """
        if self.head is None:
            print("Error: empty list!")
            return
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
        return temp_node.val
        
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
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node.val

    def insert(self, index, value):
        """
        insert value at index, 
        so current item at that index is pointed to by new item at index
        """
        # check the validity of index
        if index < 0 or index > self.n:  # larger than no. of items
            print("Index Error; please input valid index")
            return
        # if index==0, same as push_front
        if index==0:
            self.push_front(value)
            return
        # else,
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index-1):
            temp_node = temp_node.next  # traverse the list
        new_node.next = temp_node.next  # temp_node is index-1 node
        temp_node.next =  new_node
        self.n += 1
    
    def delete(self, index):
        """
        removes node at given index
        """
        # check validity of index:
        if index < 0 or index > self.n:
            print("Index Error; please input valid index")
            return
        # if head element is to be removed,
        if index == 0:
            _ = self.pop_front()
            return
        # else,
        temp_node = self.head
        for _ in range(index-1):
            temp_node = temp_node.next  # traverse the list
        index_node = temp_node.next
        # unlink
        temp_node.next = temp_node.next.next
        index_node = None
        self.n -= 1
    
    def remove_value(self, value):
        """
        removes the first item in the list with this value
        """
        # check the head's key
        temp_node = self.head
        if temp_node.val==value:
            self.head = temp_node.next
            temp_node = None
            self.n -= 1
            return

        # search for the key value
        while temp_node.val != value:  # check the next node's key
            prev_node = temp_node  # store prev node to change prev.next
            temp_node = temp_node.next
        # if the key is not found
        if temp_node == None:
            print("Error; key value is not found")
            return
        else:
            # reconfigure; unlink the current node
            prev_node.next = temp_node.next
            temp_node = None
            self.n -= 1

    def value_n_from_end(self, n):
        """
        returns the value of the node at nth position from the end of the list
        """
        # check the validity of the input
        if n > self.n-1:
            print(f"Error; n is greater than the length of the list = {self.n-1}") 
            return
        
        temp_node = self.head  # store head
        for _ in range((self.n-1) - n):
            temp_node = temp_node.next  # traverse the list
        return temp_node.val

    def reverse(self):
        """
        reverse the list
        """ 
        # check if the list is empty
        if self.head is None:
            print("Error; the list is empty")
            return
        # if there is only one entry, do nothing
        if self.n==1:
            return
        # else,
        prev_node = None  # tail should be none
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def delete_list(self):
        """
        Delete the entire linked list
        """ 
        temp_node = self.head
        while temp_node is not None:
            prev_node = temp_node
            temp_node = temp_node.next
            # prev_node.val += ": deleted"  # for sanity check
            # reset data
            prev_node.val = None
            prev_node.next = None

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
    print("\npop_front")
    print(f"No. of items = {llist.n}")
    print(f"poped item = {temp}")
    print(llist)

    # pop back
    temp = llist.pop_back()
    print("\npop_back")
    print(f"No. of items = {llist.n}")
    print(f"poped item = {temp}")
    print(llist)

    # get front
    temp = llist.front()
    print("\nget front()")
    print(f"No. of items = {llist.n}")
    print(f"poped item = {temp}")
    print(llist)

    # back
    temp = llist.back()
    print("\nget back()")
    print(f"No. of items = {llist.n}")
    print(f"poped item = {temp}")
    print(llist)

    # value_at
    temp = llist.value_at(1)
    print("\nvalue_at(1)")
    print(f"No. of items = {llist.n}")
    print(f"poped item = {temp}")
    print(llist)

    # insert
    llist.insert(0, "Holiday")
    print("\ninsert at index=0")
    print(f"No. of items = {llist.n}")
    print(llist)

    # insert
    llist.insert(1, "Sun")
    print("\ninsert at index=1")
    print(f"No. of items = {llist.n}")
    print(llist)

    # insert
    llist.insert(4, "Holiday")
    print("\ninsert at index=4")
    print(f"No. of items = {llist.n}")
    print(llist)

    # insert
    llist.insert(6, "Thurs")
    print("\ninsert at index=6(end)")
    print(f"No. of items = {llist.n}")
    print(llist)

    # remove
    llist.delete(1)
    print("\ndelete at index=1")
    print(f"No. of items = {llist.n}")
    print(llist)

    # remove
    llist.delete(0)
    print("\ndelete at index=0")
    print(f"No. of items = {llist.n}")
    print(llist)

    # remove key
    llist.remove_value("Holiday")
    print("\nremove key = Holiday")
    print(f"No. of items = {llist.n}")
    print(llist)

    # remove key
    llist.remove_value("Thurs")
    print("\nremove key = Thurs")
    print(f"No. of items = {llist.n}")
    print(llist)

    # search nth from the end
    temp = llist.value_n_from_end(0)
    print("\nvalue n = 0 from the end")
    print(f"item = {temp}")
    print(llist)

    # search nth from the end
    temp = llist.value_n_from_end(2)
    print("\nvalue n = 2 from the end")
    print(f"item = {temp}")
    print(llist)

    # insert new item
    llist.insert(0, "Holiday")
    print("\ninsert new item")
    print(f"No. of items = {llist.n}")
    print(llist)

    # reverse list
    llist.reverse()
    print("\nreverse list!")
    print(f"No. of items = {llist.n}")
    print(f"reversed list = {llist}")

    # reverse list
    llist.delete_list()
    print("\nDelete the list!")
    print(f"No. of items = {llist.n}")
    print(f"Linked list = {llist}")