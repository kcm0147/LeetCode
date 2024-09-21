class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tokens = self.separate(expression)
        return self.compute(tokens, defaultdict(list))

    def compute(self, tokens: List[str], memo: defaultdict) -> List[int]:
        if len(tokens) == 1:
            return [int(tokens[0])]
        if tuple(tokens) in memo:
            return memo[tuple(tokens)]
        result = []
        for i in range(1, len(tokens), 2):
            left = self.compute(tokens[:i], memo)
            right = self.compute(tokens[i + 1:], memo)
            for l in left:
                for r in right:
                    result.append(self.operate(l, r, tokens[i]))
        memo[tuple(tokens)] = result
        return result

    def operate(self, left: int, right: int, operator: str) -> int:
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right


    def separate(self, expression: str) -> List[str]:
        tokens = []
        number = ""
        for char in expression:
            if char.isdigit():
                number += char
            else:
                if number:
                    tokens.append(number)
                    number = ""
                tokens.append(char)
        if number:
            tokens.append(number)
        return tokens