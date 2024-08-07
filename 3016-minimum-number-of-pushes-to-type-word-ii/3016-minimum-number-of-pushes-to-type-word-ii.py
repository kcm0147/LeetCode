class Solution:
    def minimumPushes(self, word: str) -> int:
        word_map = Counter(word)
        items = [(-value, key) for key, value in word_map.items()]

        heapq.heapify(items)
        result = 0
        count = 1
        while items:
            for i in range(8):
                (cnt, key) = heapq.heappop(items)
                result += (count * (-cnt))
                if not items:
                    break
            count += 1
        return result