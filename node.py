##this file will contain the class Node for each county

class Node:
    def __init__(self, code: int, name: str):
        self.name = name
        self.code = code
        self.degree = 0
        self.color = None
        self.neighbors = []
        self.conflict = []
        self.domain = [1, 2, 3, 4, ]

    def add_neighbor(self, neighbor):
        """
        Add a neighbor to the node
        """
        if isinstance(neighbor, list):
            for code in neighbor:
                if code not in self.neighbors:
                    self.neighbors.append(code)
                    self.degree += 1
        else:
            if neighbor not in self.neighbors and neighbor != self.code:
                self.neighbors.append(neighbor)
                self.degree += 1

    def assign_color(self, color):
        """
        Assign a color to the node
        """
        self.color = color
    def get_name(self):
        return self.name