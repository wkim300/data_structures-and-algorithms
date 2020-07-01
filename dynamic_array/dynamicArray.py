"""
Theory Video Reference: https://www.coursera.org/lecture/data-structures/arrays-OsBSF

Array Definition: Contiguous area of memory consisting of 
equal-size elements indexed by contiguous integers

Key Attributes:
- Constant time access to read/write
- Allows random access of elements
- Expensive insertion/deletion due to copy & paste operation

Implement a vector (mutable array with automatic resizing):
 Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
 new raw data array with allocated memory
can allocate int array under the hood, just not use its features
start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
 - size() - number of items
 - capacity() - number of items it can hold
 - is_empty()
 - at(index) - returns item at given index, blows up if index out of bounds
 - push(item)
 - insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
 - prepend(item) - can use insert above at index 0
 - pop() - remove from end, return value
 - delete(index) - delete item at index, shifting all trailing elements left
 - remove(item) - looks for value and removes index holding it (even if in multiple places)
 - find(item) - looks for value and returns first index with that value, -1 if not found
 - resize(new_capacity) // private function
    when you reach capacity, resize to double the size
    when popping an item, if size is 1/4 of capacity, resize to half
Time
O(1) to add/remove at end (amortized for allocations for more space), index, or update
O(n) to insert/remove elsewhere

Space
contiguous in memory, so proximity helps performance
space needed = (array capacity, which is >= n) * size of item, but even if 2n, still O(n)


Or in Python, "list" is really a dynamic array. See ref:https://wiki.python.org/moin/TimeComplexity

"""
import ctypes 
  
class DynamicArray(object): 
    ''' 
    DYNAMIC ARRAY CLASS (Similar to Python List) 
    '''
    def __init__(self):
        self.n = 0 # acctual number of elements
        self.capacity = 1 # default capacity
        self.arr = self.make_array(self.capacity)
          
    def __len__(self): 
        """ 
        Return number of elements sorted in array 
        """
        return self.n

    def __getitem__(self, k): 
        """ 
        Return element at index k 
        """ 
        # check if k is valid
        if k > self.n or k < 0:
            return IndexError("k is out of bounds")
        return self.arr[k] # otherwise, return the item
    
    def __str__(self):
        temp = ""
        if 0 < self.n:
            for i in range(self.n):
                # print(self.arr[i], end=', ')
                temp+=f'{self.arr[i]}, '
        return temp
          
    def append(self, ele): 
        """ 
        Add element to end of the array 
        """
        # if the array is full, double the capacity
        if self.n==self.capacity:
            self._resize(2*self.capacity)
        # set index n entry to element and increment n
        self.arr[self.n] = ele
        self.n+=1  
  
    def insert_at(self,item,index):
        """ 
         This function inserts the item at any specified index. 
        """
        # check if the index is valid
        if self.n<index or index<0:
            print("index is out of bounds")
            return

        # if the array is full, resize
        if self.n==self.capacity:
            self._resize(2*self.capacity)
        # copy elements after the index into the new array
        for i in range(self.n-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        # then insert the item at index
        self.arr[index] = item
        self.n+=1
    
    def prepend(self, item):
        """
        This function inserts the item in front of the array
        """
        self.insert_at(item, 0)
          
    def delete(self): 
        """ 
        This function deletes item from the end of array 
        """
        if self.n==0:
            print("Empty array, deletion is not possible")
            return
        self.arr[self.n-1]=0 # zero-out
        self.n-=1 # decrement

    def pop(self):
        """
        Remove from end, return value
        """
        if self.n==0:
            print("Empty array, pop is not possible")
            return
        # when popping an item, if size is 1/4 of capacity, resize to half
        if self.n <= self.capacity/4:
            self._resize(int(self.capacity/2))
        temp = self.arr[self.n-1]  # store in a temporary var
        self.arr[self.n-1] = 0
        self.n-=1
        return temp
      
    def remove_at(self,index): 
        """ 
        This function deletes item from a specified index.. 
        """
        # check index
        if self.n==0:
            print("Empty array, cannot delete")
            return
        if self.n-1<index or index<0:
            return IndexError("invalid index")
        for i in range(index+1, self.n):
            self.arr[i-1] = self.arr[i]
        self.arr[self.n-1] = 0  # reset the last element to 0
        self.n-=1  # decrement 1
          
    def _resize(self, new_cap): 
        """ 
        Resize internal array to capacity new_cap 
        """
        temp = self.make_array(new_cap)  # create bigger array
        for i in range(self.n):
            temp[i] = self.arr[i]  # copy over all existing values
        self.arr = temp  # reset the reference
        self.capacity = new_cap
          
    def make_array(self, new_cap): 
        """ 
        Returns a new array with new_cap capacity 
        """
        return (new_cap * ctypes.py_object)()

    def find(self, item):
        # return the first known index
        for i in range(self.n):
            if self.arr[i]==item:
                return i 
        return -1

if __name__ == "__main__":
    arr = DynamicArray()
    # Append new element
    for i in range(5):
        arr.append(i)
    print(arr)
    print("current capacity is = ", arr.capacity)

    # delete
    arr.delete()
    print("\nAfter delete(), arr = ", arr)
    print("current capacity is = ", arr.capacity)
    print("current n is = ", arr.n)

    #
    arr.insert_at(4, 4)
    print("\nAfter insert_at(), arr = ", arr)
    print("current capacity is = ", arr.capacity)
    print("current n is = ", arr.n)

    # 
    arr.insert_at(-1, 2)
    print("\nAfter insert_at(), arr = ", arr)
    print("current capacity is = ", arr.capacity)

    # 
    temp = arr.pop()
    print("\nAfter insert_at(), arr = ", arr)
    print("poped element is = ", temp)
    print("current capacity is = ", arr.capacity)

    for i in range(8):
        arr.insert_at(-9, 0)
    print("\nAfter insert_at()x8, arr = ", arr)
    print("poped element is = ", temp)
    print("current capacity is = ", arr.capacity)

    print("\npopping...x8")
    for i in range(10):
        arr.pop()
        print("After popping, arr = ", arr)
        print("current capacity is = ", arr.capacity)

    print("\nprepending -10...x8")
    for i in range(8):
        arr.prepend(-10)
        print("After prepending, arr = ", arr)
        print("current capacity is = ", arr.capacity)

    print("\nFind item's first index")
    temp = arr.find(-9)
    print("Current arr = ", arr)
    print("The index for -9 is = ", temp)

    print("\nFind item's first index")
    temp = arr.find(-99)
    print("Current arr = ", arr)
    if temp==-1:
        print("The item does not exist")
    