"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
    Arrays are index based data structure where each element associated with an index. Linked list relies on references where each node consists of the data and the references to the previous and next element. Linked list points to head and tail.
    Stack: Last item put on is the first item out. LIFO. Append or take off the end. Only the end matters.
    Que: First person in line gets served first FIFO. Last in line is last served. LILO. Append or take off from the front. Middle does not matter.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('C:\\Users\\spira\\Documents\\Data-Structures\\singly_linked_list')
from singly_linked_list import LinkedList


#Array

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        return self
        
    def pop(self):
        if self.size:
            first = self.storage.pop()
            self.size -= 1
            return first
        else:
            return None


#Linked list

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1
#         return self

#     def pop(self):
#         if len(self):
#             first = self.storage.remove_tail()
#             self.size -= 1
#             return first
#         else:
#             return None