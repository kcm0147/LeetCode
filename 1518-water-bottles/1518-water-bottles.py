class Solution:
     def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            exchanged_bottles = numBottles // numExchange
            result += exchanged_bottles
            numBottles = exchanged_bottles + (numBottles % numExchange)
        return result