class Solution:
    def isBinary(self, s):
        s=s
        if '0' in s or '1' in s:
            if '2' not in s and '3' not in s and '4' not in s and '5' not in s and '6' not in s and '7' not in s and '8' not in s and '9' not in s:
                return True
            else:
                return False
        else:
            return False
s1 = Solution()
print(s1.isBinary('754893101'))


# Check for Binary String
# Solved
# Difficulty: BasicAccuracy: 30.94%Submissions: 167K+Points: 1
# Given a non-empty sequence of characters s, return true if sequence is Binary, else false.
#
# Examples:
#
# Input: s = "101"
# Output: true
# Explanation: Since string contains only '0' and '1', output is true.
# Input: s = "75"
# Output: false
# Explanation: Since string contains digits other than '0' and '1', output is false.
# Constraints:
#
# 1 ≤ s.size() ≤ 105