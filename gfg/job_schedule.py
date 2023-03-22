from functools import reduce
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], days: int) -> int:
        if len(jobDifficulty) < days:
            return -1

        if len(jobDifficulty) == days:
            a = reduce(lambda a,b: a+b, jobDifficulty)
            return a

        re 


a = Solution()
b = a.minDifficulty([1,2,3,5,6], )
print(b)
