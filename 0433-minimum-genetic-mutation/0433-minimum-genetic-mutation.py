class Solution:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        char_ary = ["A", "C", "G", "T"]
        que = []
        heapq.heappush(que, (0, startGene))
        result = sys.maxsize
        visit = set()
        while que:
            count, genes = heapq.heappop(que)
            if count >= result:
                break

            for index, gene in enumerate(genes):
                for other in char_ary:
                    if gene != other:
                        new = genes[:index] + other + genes[index + 1:]

                        if new in bank_set and new not in visit:
                            if new == endGene:
                                result = min(result, count + 1)
                            heapq.heappush(que, (count + 1, new))
                            visit.add(new)

        return result if result != sys.maxsize else -1