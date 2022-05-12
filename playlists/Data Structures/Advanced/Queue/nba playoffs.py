class Node:
    def __init__(self, val: str, conference: str, rank: int, wins=0) -> None:
        """ONLY DEFAULT ITEMS CAN BE AFTER THE FIRST DEFAULT EG: WINS=0 IS DEFAULT SO MUST BE LAST"""
        self.val = val
        self.conference = conference
        self.rank = rank
        self.wins = wins
        self.rounds = ["First Round", "SemiFinals", "Conference Finals", "Finals"]


"""STOPPED HERE"""
'''EASTERN CONFERENCE'''
Heat = Node("Miami Heat", "Eastern Conference", 1)
Hawks = Node("Atlanta Hawks", "Eastern Conference", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
EASTERN_CONFERENCE = [[]]

'''WESTERN CONFERENCE'''
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
Hawks = Node("", "", 8)
WESTERN_CONFERENCE = [[]]




class PriorityQueue:
    def __init__(self, arr: list[Node], max_len: int) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def sort_queue(self) -> list[Node]:
        pass

    def defeats(self, node: Node):
        pass
