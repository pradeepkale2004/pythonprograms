def utility(s):
    s1=''
    for i in range(0,len(s)):
        if i%2==0:
            s1+=(s[i])
    return s1



print(utility('Hello World'))



# Even Positioned Characters
# Difficulty: BasicAccuracy: 61.13%Submissions: 167K+Points: 1Average Time: 10m
# You are given a String S, you need to print its characters at even indices(index starts at 0).
#
# Examples:
#
# Input: s = "Geeks"
# Output: Ges
# Explanation: The even indices (0, 2 & 4) characters are printed.
# Input: s = "DoctorPhenomenal"
# Output: DcoPeoea
# Explanation: The even indices characters are printed.