class Node:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right
        self.code = ''


def traverse_huffman_table(node, huff_code=''):
    new_code = str(huff_code) + str(node.code)

    if node.left:
        traverse_huffman_table(node.left, new_code)
    if node.right:
        traverse_huffman_table(node.right, new_code)

    if not node.left and not node.right:
        print(f"{node.char} ==> {new_code}")


def find_symbol(node, code):
    code_array = []
    pointer = node
    for i in code:
        code_array.append(i)
        if int(i) == 0:
            pointer = pointer.left
        elif int(i) == 1:
            pointer = pointer.right

    return pointer


def huffman_coding():
    frequency_table = {
        "a": 5,
        "b": 9,
        "c": 12,
        "d": 13,
        "e": 16,
        "f": 45
    }

    nodes = []

    for f in frequency_table:
        nodes.append(Node(f, frequency_table[f]))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.frequency)
        left = nodes[0]
        right = nodes[1]
        left.code = 0
        right.code = 1

        new_node = Node(left.char + right.char, left.frequency + right.frequency, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    traverse_huffman_table(nodes[0])
    code = str(input("Enter the a code : "))
    print(f"Symbol for {code} => {find_symbol(nodes[0], code).char}")
