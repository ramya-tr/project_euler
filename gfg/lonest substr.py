def lengthOfLongestSubstring(s: str) -> int:
    longest = 0

    for i in range(len(s)):
        if longest > len(s) - i:
            break

        count = 0
        substr = []

        for j in s[i:]:
            if j not in substr:
                count += 1
                substr.append(j)
            else:
                if count > longest:
                    longest = count
                break
        if count > longest:
            longest = count
    return longest


print(lengthOfLongestSubstring(' '))
