"""
File: node_probe.py

Tests the Node class.
"""

from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next
    
    
head = Node(None, None)
head.next = head

for count in range(1, 6):
    head.next = Node(count, head.next)

probe = head.next
while probe is not head:
    print("!", probe.data)
    probe = probe.next
