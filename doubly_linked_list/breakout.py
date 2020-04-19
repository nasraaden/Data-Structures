# How do you find and return the middle node of a singly linked list in one pass?
# Don't have access to the length
# If length is even, return the first of the to middle nodes
# Can't store nodes in another data structure

# singly linked list only goes in one direction

# PLAN
# iterate through list starting at the head index, you would keep going until head.next is None
# we would be incrementing the size

# after head.next is none, we've reached whatever is after the tail and we don't increment size
# size = length of the list

# 1 -> 2 -> 3 -> None
# increment size --> size = 1
# increment size --> size = 2
# increment size --> size = 3
# middle = size // 2
# if size is even (that means there is an odd number of values): return list[middle]
# otherwise: return list[middle - 1] to get the first of the middle indices

# using a regular list
# list = [1, 2, 3, 4, 5, 6]

# middle = len(list) // 2
# if len(list) % 2:
#     print(list[middle])
# else:
#     print(list[middle - 1])


# SECOND PROBLEM

# How do you reverse a singly linked list without recursion?
# Can't store list in other data structures
# Can't make a new list

# how to make the tail the head and the head the tail

# store current number being moved
# increment that after the head

# current_node = self.head

# while current_node.next is not None:
#     if self.head


# 1 -> 2 -> 3 -> 4 -> 5 -> None

# remove from tail and add to head
# 5 -> 1 -> 2 -> 3 -> 4 -> None

# remove from tail
# set the tail to self.head.next
# 5 -> 4 -> 1 -> 2 -> 3 -> None

# remove from tail
# set the tail to self.head.next.next
# 5 -> 4 -> 3 -> 1 -> 2 -> None

# remove from tail
# set the tail to self.tail.prev
# 5 -> 4 -> 3 -> 2 -> 1 -> None
