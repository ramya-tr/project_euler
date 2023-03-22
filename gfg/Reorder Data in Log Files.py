
class Solution:
    def reorderLogFiles(self, logs):
        digit = []
        leter = {}

        for each in logs:
            splt = each.split()

            if self.check_if_all_digit(splt[1:]):
                digit.append(each)

            else:
                strg = " ".join(splt[1:])
                if strg in leter:
                    leter[strg].append(each)
                else:
                    leter[strg]=[each]
                # leter[strg] = leter.get(strg, []).append(each)

        output = []

        for i in sorted(leter.keys()):
            output.extend(sorted(leter[i]))

        output.extend(digit)

        return output




    def check_if_all_digit(self, input):
        for e in input:
            if not e.isdigit():
                return False
        return True


a=Solution()
logs = ["dig1 8 1 5 1","let9 art can","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(a.reorderLogFiles(logs))
