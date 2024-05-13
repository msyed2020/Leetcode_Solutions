
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

from collections import Counter
def minWindow(s, t):
    # if there is no string in t, there's nothing to compare for in s, so just return empty string
    if t == "":
        return ""
    # Gather all counted values in countT
    countT = Counter(t)
    # Empty dictionary to keep track of window values
    window = {}
    # have -- how many letters we have in our window versus how many we need to have
    have = 0
    need = len(countT)
    # result array, and length, length being used to check for a shorter substring
    res = [-1, -1]
    resLen = float("infinity")
    # left pointer (moves conditionally, compared to r, which always moves. Typical sliding window rep)
    l = 0
    # move r in direction
    for r in range(len(s)):
        c = s[r]
        # Add 1 count to the element r is currently at in s to the window dictionary. If this is a totally new number,
        # initialize the count to 0 instead
        window[c] = 1 + window.get(c, 0)
        # If this is a "crucial letter", and we have enough of this letter to match the required count in C, we officially
        # "have" this crucial letter. Since haves/needs count the number of distinct needed letters, they have to match
        # the count for the crucial letter to be considered in "have"
        if c in countT and window[c] == countT[c]:
            have += 1
        # While we have satisfied our conditions of being a window substring that matches the requirements
        while have == need:
            # If we found a shorter result than the result that is already being stored, change the result to equal
            # that of the smallest result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)

            # this process is to "slide" the window leftwards, in order to minimize the window as much as possible
            # to find the minimum window in which the solution is viable

            # decrement the left window count by one as we won't be using it anymore
            window[s[l]] -= 1
            # if this was a crucial letter and it fell out of the required number of "crucial letters" we no longer
            # "have" this letter
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            # increment the left pointer by 1
            l += 1
    # extract the left pointer index and the right pointer index from the 2-indexed result array
    l, r = res
    # return the window from the bounds we have gotten, + 1 on the right to account for Pythonic string slicing,
    # if we had found a viable window had indeed existed in the s string. If not, return an empty string.
    return s[l:r + 1] if resLen != float("infinity") else ""

print("Solution:", minWindow("ADOBECODEBANC", "ABC"))
print("Solution:", minWindow("a", "a"))
print("Solution:", minWindow("a", "aa"))

