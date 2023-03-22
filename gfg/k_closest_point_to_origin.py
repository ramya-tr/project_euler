class Solution:
    def kClosest(self, points, k):
        distance = {}

        for each in points:
            d = pow(abs(each[0]), 2) + pow(abs(each[1]), 2)

            if d in distance:
                distance[d].append(each)
            else:
                distance[d] = [each]

            # distance.get(d, []).append(each)

        output = []

        for key in sorted(distance.keys()):
            output.extend(distance[key])
            if len(output) >=  k:
                break

        return output


a = Solution()
points = [[1,3],[-2,2]]
k = 1
print("answer: ", a.kClosest(points, k))
