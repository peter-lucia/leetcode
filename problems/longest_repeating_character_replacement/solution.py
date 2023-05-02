class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts_in_window = defaultdict(int)

        i = 0
        maxf = 0
        result = 0

        for j, rightmost_char in enumerate(s):
            counts_in_window[rightmost_char] += 1
            maxf = max(maxf, counts_in_window[rightmost_char])
            sliding_window_size = j - i + 1

            if sliding_window_size - maxf > k:
                leftmost_char = s[i]
                counts_in_window[leftmost_char] -= 1
                i += 1

            sliding_window_size = j - i + 1

            result = max(result, sliding_window_size)
        return result
            


