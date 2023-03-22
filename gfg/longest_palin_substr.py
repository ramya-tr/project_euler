class Solution:
    def longestPalindrome(self, s):
        max_l = 0
        palin = None
        for i in range(len(s)):
            if max_l > len(s) - i:
                break
            start = max(1, max_l)
            for j in range(start, len(s) - i + 1, 1):
                l = max(j, max_l)
                sub = s[i: i + l]
                print(f"i={i} ,j={j} ,max_l={max_l} , l={l}, string={sub}")

                if self.palindrome(sub):
                    max_l = l
                    palin = sub
                    print(f"it is a palindrome : {sub}")
        return palin

    def palindrome(self, sstr):
        # print(sstr)
        if sstr == sstr[::-1]:
            return True
        return False


a = Solution()
str = "abacab"
print("answer: ", a.longestPalindrome(str))
