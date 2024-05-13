
# Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
# every character in t (including duplicates) is included in the window. If there is no such substring, return the empty
# string ""

# The testcases will be generated such that the answer is unique.

# Approach: Create two hashmaps (one for the letters of t, known as countT, and the other for the sliding window
# we will perform). We want to return the minimum window range in which this program is functional

# We "need" all of the countT values, while only "having" 0 at the beginning (because we haven't traversed yet)

# After initializing our values, we traverse right using two pointers. We add each letter to the window. If we find we
# have a "crucial letter" (one in countT) and the counts of said letter add up, we can say we "have" the letter.

# Once we get to a point where have == need, we can update the result if we found a smaller substring if need be,
# otherwise we can delete until we get to the point we need. Then we can assign to res and return the final result.

# More code detail will be written INSIDE of the code lines.

def minWindow(s, t):
    if t == "":
        return ""
    countT = {}
    window = {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    have = 0
    need = len(countT)
    res = [-1, -1]
    resLen = float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            # update result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r + 1] if resLen != float("infinity") else ""

print("Solution:", minWindow("ADOBECODEBANC", "ABC"))
print("Solution:", minWindow("a", "a"))
print("Solution:", minWindow("a", "aa"))
