class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        curr = self.head  # Fixed: changed self.first to self.head
        ele = []
        while curr is not None:
            ele.append(str(curr.data))  # Fixed: append data as string
            curr = curr.next
        print(" -> ".join(ele) + " -> None")


# --- Method 1: Using append() ---
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()
# Output: 10 -> 20 -> 30 -> None


# --- Method 2: Manual Node Creation (Your commented approach) ---
# first = Node(10)
# sec = Node(30)
# third = Node(90)
# fourth = Node(40)

# first.next = sec
# sec.next = third
# third.next = fourth

# # Assign the start node to a LinkedList instance head:
# manual_ll = LinkedList()
# manual_ll.head = first

# manual_ll.display()
# Output: 10 -> 30 -> 90 -> 40 -> None