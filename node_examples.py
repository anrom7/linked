"""
File: node_examples.py

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
