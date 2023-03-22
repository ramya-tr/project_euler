import math


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        diff_pos = {}
        diff_neg = {}

        # for i in range(len(time)):
        #     for j in range(i+1, len(time), 1):
        #         if (time[i]+time[j]) % 60 == 0:
        #             count += 1

        for i in range(len(time)):
            a = time[i] % 60

            if time[i] >= 0 or a == 0 or a == 30:
                diff_pos[a] = diff_pos.get(a, 0) + 1
            else:
                diff_neg[a] = diff_neg.get(a, 0) + 1

        if 0 in diff_pos and diff_pos[0] > 1:
            count += (math.factorial(diff_pos[0]) / (math.factorial(diff_pos[0] - 2) * 2))

        if 30 in diff_pos and diff_pos[30] > 1:
            count += (math.factorial(diff_pos[30]) / (math.factorial(diff_pos[30] - 2) * 2))

        for i in range(1, 30, 1):
            if i in diff_pos and (60 - i) in diff_pos:
                count += (diff_pos[i] * diff_pos[60 - i])

            if i in diff_pos and i in diff_neg:
                count += (diff_pos[i] * diff_neg[i])

        return int(count)
