"""
File: test_node.py

Tests the Node class.
"""

from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# Print the contents of the structure
probe = head
while probe is not  None:
    print(probe.data)
    probe = probe.next

head = Node(None, None)
head.next = head

for count in range(1, 6):
    print("?", head.next.data)
    head.next = Node(count, head.next)
    print("?&", head.next.data)

probe = head.next
while probe is not head:
    print("!", probe.data)
    probe = probe.next
    
print("______________________")
head = None

# Add five nodes to the beginning of the linked structure
for count in [36, 18, 52, 2, 73]:
    head = Node(count, head)

newNode = Node(22)
curNode = head.next

#newNode.next = curNode.next.next
#curNode.next.next = newNode

#curNode = curNode.next
#newNode.next = curNode.next
#curNode.next = newNode

#node = curNode.next
#else1 = node.next
#node.next = newNode
#newNode.next = else1

#node = curNode.next
#curNode.next = newNode
#newNode.next = node

newNode.next = head.next.next.next
head.next.next = newNode

probe = head
while probe is not  None:
    print(probe.data)
    probe = probe.next

print("______________________")

head = None

# Add five nodes to the beginning of the linked structure
for count in [36, 18, 52, 2, 73]:
    head = Node(count, head)

#curNode = head.next
#curNode.next.next = curNode.next.next.next

a = head.next.next.next.next
#removedItem = a.data()
a = None

probe = head
while probe is not  None:
    print(probe.data)
    probe = probe.next

print("______________________")


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None) # this is the sentinel node!
        self.head.next = self.head   # link it to itself

    def add(self, data):             # no special case code needed for an empty list
        self.head.next = Node(data, self.head.next)

    def __contains__(self, data):    # example algorithm, implements the "in" operator
        current = self.head.next
        while current != self.head:
            if current.data == data: # element found
                return True
            current = current.next
        return False
        

c = CircularLinkedList()
for count in range(1, 6):
    c.add(count)

probe = c.head.next
while probe is not c.head:
    print(probe.data)
    probe = probe.next