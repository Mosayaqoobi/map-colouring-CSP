## this file is used to make the complete adjcaceny matrix
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
    adj = {}

    for entry in data:
        code1 = int(entry[1])
        code2 = int(entry[3])

        if code1 not in adj:
            adj[code1] = []
        if code2 not in adj:
            adj[code2] = []

        if code2 not in adj[code1] and code1 != code2:
            adj[code1].append(code2)
        if code1 not in adj[code2] and code1 != code2:
            adj[code2].append(code1)
    return adj


line = read_file("raw_list.txt")
print(make_list(line))