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
    def __init__(self, arr: list, sorted=False) -> None:
        if sorted:
            arr.sort()

        self.head = Node(arr.pop(0))
        node = self.head

        for elem in arr:
            node.next = Node(val=elem)  # "val=" is not needed
            node = node.next

    def __repr__(self) -> str:
        llstr = ""

        node = self.head
        while node:
            llstr += f"{node.val} -> "
            node = node.next
        llstr += "None"

        return llstr

    def insert(self, elem: str | int, position: int) -> None:
        new_node = Node(elem)
        prev_node = self.head

        if position == 0:
            new_node.next = prev_node
            self.head = new_node
        else:
            node = prev_node.next
            count = 1  # If position isn't 0 then we don't need to take account of head.
            while node:
                if count == position:
                    prev_node.next = new_node
                    new_node.next = node
                    return
                prev_node = node
                node = node.next
                count += 1

            # If count is greater than the number of elements then add new_node to the end
            prev_node.next = new_node
            new_node.next = None

    def find(self, value: str | int) -> bool:
        node = self.head

        while node:
            if node.val == value:
                return True
            node = node.next

        return False

    def delete(self, elem) -> None:
        prev_node = self.head
        node = prev_node.next
        count = 2  # Accounting for self.head already being evaluated

        if elem == prev_node.val:
            self.head = node
            return

        while node:
            if node.val == elem:
                prev_node.next = node.next
                return
            prev_node = node
            node = node.next
            count += 1


email = LinkedList(user_list)
print(email)
print()

# Add new_email
new_email = "whomikejones@hotmail.com"

"""Add to beginning"""
# email.insert(new_email, 0)
# print(email)
"""Add to the end"""
# email.insert(new_email, 100)
# print(email)
"""Add to middle"""
#email.insert(new_email, 0)
#print(email)

# Delete
"""Delete new_email"""
#email.delete(new_email)
#print(email)

"""Delete last email"""
email.delete("lastuser@user.com")
print(email)
