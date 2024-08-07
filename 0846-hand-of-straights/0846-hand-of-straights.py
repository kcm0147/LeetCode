class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_size = len(hand)

        if hand_size % groupSize != 0:
            return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            cur = min_heap[0]
            for i in range(groupSize):
                if count[cur + i] == 0:
                    return False
                count[cur + i] -= 1
                if count[cur + i] == 0:
                    if cur+i != heapq.heappop(min_heap):
                        return False
                    
        return True