class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sums = sum(rolls)
        real_sums = (len(rolls) + n) * mean
        missing_sums = real_sums - sums
        div = missing_sums // n

        return [] if div <= 0 else self.make_result(n, missing_sums)

    def make_result(self, n: int, missing_sums: int) -> List[int]:
        div = missing_sums // n
        rest = missing_sums % n
        if div > 6 or (div == 6 and rest > 0):
            return []

        result = [div for _ in range(n)]
        while rest > 0:
            for i, num in enumerate(result):
                value = min(rest, 6 - num)
                result[i] += value
                rest -= value
                if rest == 0:
                    break
        return result