file1 = open("while1.txt", "w")
file2 = open("if1.txt", "w")
file3 = open("while2.txt", "w")
file4 = open("if2.txt", "w")

class TrieNode:
    def __init__(self):
        # Initialize TrieNode attributes
        self.children = {}
        self.output = []
        self.fail = None


def build_automaton(keywords):
    # Initialize root node of the trie
    root = TrieNode()

    # Build trie
    for keyword in keywords:
        node = root
        # Traverse the trie and create nodes for each character
        for char in keyword:
            node = node.children.setdefault(char, TrieNode())
        # Add keyword to the output list of the final node
        node.output.append(keyword)

    # Build failure links using BFS
    queue = []
    # Start from root's children
    for node in root.children.values():
        queue.append(node)
        node.fail = root

    # Breadth-first traversal of the trie
    while queue:
        current_node = queue.pop(0)
        # Traverse each child node
        for key, next_node in current_node.children.items():
            queue.append(next_node)
            fail_node = current_node.fail
            # Find the longest proper suffix that is also a prefix
            while fail_node and key not in fail_node.children:
                file1.write("WHILE 1 IN\n")
                fail_node = fail_node.fail
            if not fail_node:
                file1.write("WHILE 1 OUT BECAUSE OF FAIL_NODE\n")
            elif key in fail_node.children:
                file1.write("WHILE 1 OUT BECAUSE OF KEY\n")
            file1.write("")
            # Set failure link of the current node
            if fail_node:
                next_node.fail = fail_node.children[key]
                file2.write("IF 1 FAIL_NODE\n")  
            else: 
                next_node.fail = root
                file2.write("IF 1  NOT FAIL_NODE\n")
            file2.write("\n")
            # Add output patterns of failure node to current node's output
            next_node.output += next_node.fail.output

    return root


def search_text(text, keywords):
    # Build the Aho-Corasick automaton
    root = build_automaton(keywords)
    # Initialize result dictionary
    result = {keyword: [] for keyword in keywords}

    current_node = root
    # Traverse the text
    for i, char in enumerate(text):
        # Follow failure links until a match is found
        while current_node and char not in current_node.children:
            file3.write("WHILE 2 IN\n")
            current_node = current_node.fail
        if not current_node:
            file3.write("WHILE 1 OUT BECAUSE OF CURRENT_NODE\n")
        elif char in current_node.children:
            file3.write("WHILE 1 OUT BECAUSE OF CHAR\n")
        file3.write("\n")
        
        if not current_node:
            file4.write("IF 2 NOT CURRENT_NODE\n")
            current_node = root
            continue
        file4.write("IF 2 CURRENT_NODE\n")

        # Move to the next node based on current character
        current_node = current_node.children[char]
        # Record matches found at this position
        for keyword in current_node.output:
            result[keyword].append(i - len(keyword) + 1)

    return result

