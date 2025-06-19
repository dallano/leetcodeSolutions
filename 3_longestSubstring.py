def lengthOfLongestSubstring(s):
    max = 0
    hash = {}

    for i in range(len(s)):
        hash.clear()
        currMax = 0
        for y in s[i:]:
            if not y in hash:
                hash[y] = 1
                currMax += 1
                if currMax > max:
                    max = currMax
            else:
                break


    return max

print(lengthOfLongestSubstring("bbbbbb"))