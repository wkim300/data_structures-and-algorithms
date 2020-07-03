"""
Implement using linked-list, with tail pointer:
- enqueue(value) - adds value at position at tail
- dequeue() - returns value and removes least recently added element (front)
- empty()

Implement using fixed-sized array:
If implemented this way, "read" and "write" pointers needs to be pointing at the next dequeue and enqueue locations, respectively (in a circular manner).
If the pointers match (read==write), then the queue is empty
- enqueue(value) - adds item at end of available storage
- dequeue() - returns value and removes least recently added element
- empty()
- full()

Cost:
- a bad implementation using linked list where you enqueue at head 
  and dequeue at tail would be O(n) because you'd need the next to last element, 
  causing a full traversal each dequeue
- enqueue: O(1) (amortized, linked list and array [probing])
- dequeue: O(1) (linked list and array)
- empty: O(1) (linked list and array)

In Python, queue can be implemented by following ways:
- list
- collections.deque (reference: https://stackoverflow.com/questions/45688871/implementing-an-efficient-queue-in-python)
- queue.Queue
- custom linked list

From Python deque documentation:
Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). 
Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.
If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end.
"""

############## Linked-list Queue ################
class Node(object):
    """
    For linked-list impementation
    """
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
class queueL(object):
    """
    Queue using linked list and tail pointer
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        """[summary]
        Returns the string representation of the queue

        """
        string = "head"
        temp = self.head
        while temp is not None:
            string += f" -> {temp.val}"
            temp = temp.next
        string += " <- tail"
        return string

    def is_empty(self):
        """[summary]
        Returns boolean to indicate whether the queue is empty or not
        """
        return (self.head is None) and (self.tail is None)

    def enqueue(self, item):
        """[summary]
        Adds value at position at tail
        Args:
            item: new item to be added to the queueitem
        """
        new_node = Node(item)  # initialize item
        # Check if the queue is empty
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        # Else,
        last_node = self.tail
        last_node.next = new_node
        self.tail = new_node
    
    def dequeue(self):
        """[summary]
        Returns value and removes least recently added element (front)
        """
        # Check if the queue is empty
        if self.is_empty():
            print("Error; queue is empty")
            return
        # Else,
        temp_node = self.head # node to be deleted
        # check if there is only one item
        if temp_node.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = temp_node.next
            del temp_node

############## Array Queue ################
class queueA(object):
    """[summary]
    Implementation using collections.deque
    Reference: https://stackoverflow.com/questions/45688871/implementing-an-efficient-queue-in-python
    
    Thread-safe, memory-efficient, maximally-sized queue supporting queueing and
    dequeueing in worst-case O(1) time.
    """
    def __init__(self, max_size = 10):
        '''
        Initialize this queue to the empty queue.

        Parameters
        ----------
        max_size : int
            Maximum number of items contained in this queue. Defaults to 10.
        '''
        from collections import deque
        self._queue = deque(maxlen=max_size)
    
    def __str__ (self):
        """[summary]
        Returns string representation
        """
        return str(self._queue)

    def enqueue(self, item):
        '''
        Queues the passed item (i.e., pushes this item onto the tail of this
        queue).

        If this queue is already full, the item at the head of this queue
        is silently removed from this queue *before* the passed item is
        queued.
        '''
        self._queue.append(item)

    def dequeue(self):
        '''
        Dequeues (i.e., removes) the item at the head of this queue *and*
        returns this item.

        Raises
        ----------
        IndexError
            If this queue is empty.
        '''
        return self._queue.pop()

if __name__ == "__main__":
    ############## Testing Linked-list Queue ################
    lq = queueL()  # instantiate linked-list queue
    print("Testing linked-list queue...")
    # enqueue
    for i in range(4):
        lq.enqueue(i)
    print(lq)
    # dequeue
    print("\nDequeuing")
    for i in range(3, 0,-1):
        lq.dequeue()
        print(lq)

    # dequeue
    lq.dequeue()
    print(lq)
    print(f"Is queue empty? {lq.is_empty()}")

    ############## Testing Array Queue ################
    aq = queueA()  # instantiate linked-list queue
    print("Testing linked-list queue...")
    # enqueue
    for i in range(4):
        aq.enqueue(i)
    print(aq)
    # dequeue
    print("\nDequeuing")
    for i in range(3, 0,-1):
        aq.dequeue()
        print(aq)

    # dequeue
    aq.dequeue()
    print(aq)

