"""
PRIORITY QUEUES ORDER ITEMS BY THE VALUE ASSOCIATED WITH THE ELEM. THE VALUE WITH THE HIGHEST PRIORITY
IS REMOVED FIRST.


Needed info:
    • What priority is being used?
    • What's the max length of the queue
    • What data structure are we using to store the elements we'll use as nodes? EG: list, tuple 
"""


class Node:
    def __init__(self, val, priority=None) -> None:
        self.val = val
        self.priority = priority


users = [Node("Orlando", 1), Node("Shyan", 3), Node("Pepper", 2), Node("Peach", 4)]


class PriorityQueue:
    def __init__(self, arr: list[Node], max_len: int) -> None:
        if len(arr) > max_len:
            raise ValueError(
                f"Max length cannot be smaller than your list of elements."
            )

        self.queue = []
        self.max = max_len
        self.len = len(arr)

        for node in arr:
            self.queue.append(node)

        self.queue.sort(key=lambda x: x.priority)

    def __repr__(self) -> str:
        return f"{[elem.val for elem in self.queue]}"

    def sort_queue(self) -> list[Node]:
        self.queue.sort(key=lambda x: x.priority)

    def get(self, key: int) -> int:
        elem = self.queue[key]
        value = elem.val
        elem.priority = self.queue[0].priority - 1

        self.sort_queue()

        return value

    def set(self, node: Node) -> None:
        self.len += 1
        node.priority = self.queue[0].priority - 1

        # Handling a priority queue violating max length
        if self.len > self.max:
            user_response = input(
                "Your cache is full. We need to delete the least recently used item. Continue?"
            )
            if user_response.lower() == "y":
                self.queue.pop()
                self.len -= 1
                self.queue.append(node)
            else:
                print(f"{node.val.title()} was not added to the queue due to caching issues.")
        else:

            self.queue.append(node)

        self.sort_queue()

    def update(self, value, key) -> None:
        self.queue[key].val = value
        self.queue[key].priority = self.queue[0].priority - 1

        self.sort_queue()


user_queue = PriorityQueue(users, max_len=4)
print(user_queue)
print(user_queue.get(1))
print(user_queue)
user_queue.set(Node("Karmen"))
print(user_queue)
