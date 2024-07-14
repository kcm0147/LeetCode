class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        wait = 0
        for c in customers:
            time = max(time, c[0]) + c[1]
            wait += time - c[0]
        return wait / len(customers)
        