"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
    Arrays are index based data structure where each element associated with an index. Linked list relies on references where each node consists of the data and the references to the previous and next element. Linked list points to head and tail.

    Stack: Last item put on is the first item out. LIFO. Append or take off the end. Only the end matters.
    Que: First person in line gets served first FIFO. Last in line is last served. LILO. Append or take off from the front. Middle does not matter.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         length = len(self.storage)
#         self.size = length
#         return length

#     def enqueue(self, value):
#         self.storage.insert(0,value)

#     def dequeue(self):
#         if len(self) > 0:
#             return self.storage.pop()
#         else:
#             return None

import sys
sys.path.append('C:\\Users\\spira\\Documents\\Data-Structures\\singly_linked_list')
from singly_linked_list import LinkedList, Node

class Queue:
    def __init__(self):
        self.size = 0
        #Set storage to empty array
        self.storage = []
    
    #Define array size
    def __len__(self):
        return self.size

    def enqueue(self, value):
        #Add 1 to array size
        self.size += 1
        #Append new entry to array
        self.storage.append(value)

    def dequeue(self):
        #If the array is empty, return nothing
        if self.size == 0:
            return None
        else:    
            #The array is not empty, remove the entry from the top (FIFO)
            self.size -= 1
            return self.storage.pop(0)