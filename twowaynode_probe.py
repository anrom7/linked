"""
File: twowaynode_probe.py
Tests the TwoWayNode class.
"""

from node import TwoWayNode

# Create a doubly linked structure with one node
head = TwoWayNode(1)
tail = head

# Add four nodes to the end of the doubly linked structure
for data in range(2, 6):
    node = TwoWayNode(data, tail)
    print('1', node.data, node.next, node.previous)
    tail.next = node
    tail = tail.next
    print('2', node.data, node.next, node.previous)

# Print the contents of the linked structure in reverse order
probe = tail
while probe is not None:
    print(probe.data)
    probe = probe.previous
