from collections import MutableMapping


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache(MutableMapping):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

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
            self.size += 1

    def __setitem__(self, key, value):
        self.set(key, value)

    def get(self, key, default=None):
        if key in self.cache:
            temp_node = self.cache.get(key)
            self.remove_node(temp_node)
            self.push_front(temp_node)
            return temp_node.value
        elif default is not None:
            return default
        return -1

    def __getitem__(self, key):
        self.get(key, default=None)

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

    def __iter__(self):
        pass

    def __delitem__(self, key):
        pass


cache = LRUCache(capacity=3)
cache[1] = 'A'
cache[2] = 'B'
cache[4] = 'C'

print cache[1]
print len(cache)
