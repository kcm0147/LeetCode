
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = []
        numbers = set() 
        prime_factors = [2, 3, 5]

        heapq.heappush(min_heap, 1)
        numbers.add(1)

        current = 1
        for _ in range(n):
            current = heapq.heappop(min_heap)

            for prime in prime_factors:
                next_ugly = current * prime
                if next_ugly not in numbers:
                    heapq.heappush(min_heap, next_ugly)
                    numbers.add(next_ugly)

        return current
        