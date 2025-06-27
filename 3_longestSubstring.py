# Solution to 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def lengthOfLongestSubstring(s):
    max = 0
    hash = {}

    for i in range(len(s)):
        hash.clear()
        currMax = 0

        for y in s[i:]:
            if not y in hash: # If value isn't in our dict, it continues to create unique substring
                hash[y] = 1
                currMax += 1

                if currMax > max:
                    max = currMax
            else:
                break
    return max

print(lengthOfLongestSubstring("bbbbbbjhsdklbbashdhj"))