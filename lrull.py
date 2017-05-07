class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.rear = None

    def push_front(self, node):
        if isinstance(node, Node):
            node.next = self.head
            node.previous = None

            if self.head is not None:
                self.head.previous = node

            self.head = node

            if self.rear is None:
                self.rear = self.head

    def remove_node(self, node):
        # if the removal node in head
        if node.previous is None:
            self.head = node.next
            node.next.previous = None
            node.next = None

        # if the removal node in rear
        elif node.next is None:
            self.rear = node.previous
            node.previous.next = None
            node.previous = None

        else:
            node.previous.next = node.next
            node.next.previous = node.previous

    def set(self, key, value):
        if key in self.cache:
            old_node = self.cache.get(key)
            old_node.value = value
            self.remove_node(old_node)
            self.push_front(old_node)
        else:
            new_node = Node(key, value)
            if len(self.cache) >= self.capacity:
                self.cache.pop(self.rear.key)
                self.remove_node(self.rear)
                self.push_front(new_node)
            else:
                self.push_front(new_node)

            self.cache[key] = new_node

    def get(self, key):
        if key in self.cache:
            temp_node = self.cache.get(key)
            self.remove_node(temp_node)
            self.push_front(temp_node)
            return temp_node.value
        return -1

cache = LRUCache(capacity=3)
cache.set(1, "A")
cache.set(2, "B")
cache.set(3, "C")
