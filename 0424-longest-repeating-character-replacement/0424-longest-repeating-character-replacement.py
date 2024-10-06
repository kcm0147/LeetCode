class Solution:
    def characterReplacement(self,s: str, k: int) -> int:
        left = 0
        freq_map = {}
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            char = s[right]
            freq_map[char] = freq_map.get(char, 0) + 1

            max_freq = max(max_freq, freq_map[char])

            if (right - left + 1) - max_freq > k:
                left_char = s[left]
                freq_map[left_char] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        