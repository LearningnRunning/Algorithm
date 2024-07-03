class Solution:
    def partitionString(self, s: str) -> int:
        char_set = set()
        count = 0
        
        for char in s:
            if char in char_set:
                count += 1
                char_set.clear()
            char_set.add(char)
        
        return count + 1