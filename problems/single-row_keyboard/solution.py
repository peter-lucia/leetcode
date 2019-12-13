class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_lookup = {}
        for idx, key in enumerate(keyboard):
            keyboard_lookup[key] = idx
        
        total = 0
        pos = 0
        for c in word:
            current_pos = keyboard_lookup[c]
            total += abs(current_pos - pos)
            pos = current_pos
        return total