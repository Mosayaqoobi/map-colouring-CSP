## this file is used to make the complete adjcaceny matrix
from node import Node

def read_file(file_name: str) -> list[list]:
    """
    Read a file and return a list of lists of strings
    """
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [line.strip().split("|") for line in lines]

    return lines[1:]    #first line is a header
    

def make_list(data) -> dict:
    """
    data is a list of lists of strings of the form: A|code|B|code
    """
    nodes = {}

    for entry in data:
        name1, code1 = entry[0], int(entry[1])
        name2, code2 = entry[2], int(entry[3])

        # Create Node objects if they don't exist
        if code1 not in nodes:
            nodes[code1] = Node(code=code1, name=name1)
        if code2 not in nodes:
            nodes[code2] = Node(code=code2, name=name2)

        # Add each other as neighbors (skip self-loops)
        if code1 != code2:
            nodes[code1].add_neighbor(nodes[code2])
            nodes[code2].add_neighbor(nodes[code1])

    return list(nodes.values())
