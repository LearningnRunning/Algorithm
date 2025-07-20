from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.name = ""
        self.deleted = False  # 삭제 여부
        
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # Step 1: Build trie
        for path in paths:
            self.insert_path(root, path)

        # Step 2: Serialize and collect duplicate structures
        lookup = defaultdict(list)
        self.serialize(root, lookup)

        # Step 3: Mark duplicate subtrees
        for nodes in lookup.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Step 4: Collect remaining paths
        result = []
        self.collect_paths(root, [], result)
        return result

    def insert_path(self, root, path):
        node = root
        for name in path:
            if name not in node.children:
                node.children[name] = TrieNode()
                node.children[name].name = name
            node = node.children[name]

    def serialize(self, node, lookup):
        if not node.children:
            return ""
        
        serialized_parts = []
        for child in sorted(node.children.values(), key=lambda x: x.name):
            child_serial = self.serialize(child, lookup)
            serialized_parts.append(f"{child.name}({child_serial})")
        
        signature = "".join(serialized_parts)
        lookup[signature].append(node)
        return signature

    def collect_paths(self, node, path, result):
        if node.deleted:
            return
        if path:
            result.append(path[:])
        for child in node.children.values():
            path.append(child.name)
            self.collect_paths(child, path, result)
            path.pop()