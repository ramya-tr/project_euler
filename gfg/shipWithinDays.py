from functools import reduce
from typing import List


class Solution:
    """
    https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
    """

    min_s = 0
    loop = 0
    days = 0
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days >= len(weights):
            return max(weights)

        self.days = days

        a = self.split_into_parts(weights, days)
        return self.min_s

    def split_into_parts(self, array, parts, result=[]):
        if parts == 1:
            return array

        options = []
        for i in range(1, len(array), 1):
            options = []
            pieces = array[0:i]

            options.append(pieces)
            # result.append(pieces)

            send = []
            if not result:
                send = pieces
            elif len(result) == 1:
                send = [result] + [pieces]
            else:
                send = result + [pieces]

            remaining_array = array[i:]

            if len(remaining_array) < parts-1:
                continue

            ans = self.split_into_parts(remaining_array, parts-1, send)

            options.append(ans)

            final_array = result+options
            # if len(final_array) <

            self.loop += 1
            print(final_array)
            print("min : ", self.min_s )
            print("max : ", self.find_max(final_array))
            print("loop: ", self.loop)

            if self.min_s == 0:
                self.min_s = self.find_max(final_array)
            else:
                self.min_s = min(self.min_s, self.find_max(final_array))

        return options

    def find_max(self, array):
        max_sum = 0
        for i in array:
            if isinstance(i, list):
                max_sum = max(max_sum, self.get_sum(i))
            else:
                max_sum = max(i, max_sum)

        return max_sum

    def get_sum(self, array):
        sum = 0
        for i in array:
            if isinstance(i, list):
                sum += self.get_sum(i)
            else:
                sum += i

        return sum


a = Solution()

b = a.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
print(b)
print(b == 15)

# b = a.shipWithinDays([3,2,2,4,1,4], 3)
# print(b)
# print(b == 6)

# b = a.shipWithinDays([1,2,3,1,1], 4)
# print(b)
# print(b == 3)


# q = a.find_max([[[1, 2, 3, 4, 5]], [6, 7], [8], [[9], [10]]])
# print(q)
