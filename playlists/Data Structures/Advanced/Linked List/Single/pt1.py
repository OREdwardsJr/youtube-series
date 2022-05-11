"""
The telephone game is a great example of a linked list
"""


"""
    Assignment Expression aka Walrus Operator - Demonstrate the common way. This is new in 3.8 
"""
user_list = [
    user_0 := "someemailchain@aol.com",
    user_1 := "maryallen@gmail.com",
    user_2 := "ljames92@hotmail.com",
    user_3 := "heresmyemailokay@company.com",
    user_4 := "firstdotlastname@name.com",
    user_5 := "zzyx@street.com",
    user_6 := "helpfulhints@here.com",
    user_7 := "anotherone@wethebest.com",
    user_8 := "usainbolt@gmail.com",
    user_9 := "lastuser@user.com",
]


class Node:
    def __init__(self, val: str | int) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, arr: list) -> None:
        arr.sort()
        self.head = Node(arr.pop(0))
        self.len = len(arr)

        node = self.head
        for elem in arr:
            node.next = Node(val=elem)  # "val=" is not needed
            node = node.next


    def __repr__(self) -> str:
        llstr = ""

        node = self.head
        while node:
            llstr += str(node.val) + " -> "
            node = node.next
        llstr += "None"

        return llstr

    def length(self) -> int:
        return self.len

    def insert(self, val: str | int, position: int) -> None:
        self.len += 1

        count = 1
        prev_node = self.head
        node = prev_node.next

        while count <= position and node:
            if count == position:
                prev_node.next = Node(val)
                new_node = prev_node.next
                new_node.next = node
                # Add sort recursive method here
                break

            count += 1

            prev_node = node
            node = node.next

        if position > count:
            node = Node(val)
            node.next = None
            prev_node.next = node

    def sort(self) -> Node:  # Probably innefficient but still worth demonstrating
        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.next

        return f"{self.head := self.sorted()}" #pending sorted method creation

    def sorted(self):
        #You can create a build_tree method or rebuild the tree here. Probably rebuild here?
        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.next

    def delete(self, value=None, position=None) -> None:
        if value and position:
            raise ValueError(f"You cannot pass both a value and positional argument")
        elif not value and not position:
            raise ValueError(
                f"You cannot pass both a key and position into delete method"
            )
        else:
            self.len -= 1
            prev_node = self.head
            node = prev_node.next
            count = 2  # Accounting for self.head already being evaluated

            if position:
                self.len -= 1
                prev_node = self.head
                node = prev_node.next

                if position == 1:
                    prev_node = node
                    return self.head

                while node:

                    if count == position:
                        prev_node.next = node.next
                        return self.head
                    prev_node = node
                    node = node.next
                    count += 1

            elif value:
                if value == prev_node.val:
                    prev_node = node
                    return

                # Recursive
                while node:
                    # print(count)
                    if node.val == value:
                        self.head = self.delete(position=count)
                        return
                    node = node.next
                    count += 1


email = LinkedList(user_list)
print(email)
print()

new_email = "oredwardsjr@gmail.com"
email.insert(val=new_email, position=11)
print(email)
print()

# email.delete(position=11)
# print(email)
# print()

print(email.sort())
