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
                fail_node = fail_node.fail
            # Set failure link of the current node
            if fail_node:
                next_node.fail = fail_node.children[key]  
            else: 
                next_node.fail = root
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
            current_node = current_node.fail

        if not current_node:
            current_node = root
            continue

        # Move to the next node based on current character
        current_node = current_node.children[char]
        # Record matches found at this position
        for keyword in current_node.output:
            result[keyword].append(i - len(keyword) + 1)

    return result