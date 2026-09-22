# GCD of Two
# Difficulty: BasicAccuracy: 51.03%Submissions: 240K+Points: 1
# Given two positive integers a and b, find GCD of a and b.
#
# Note: Don't use the inbuilt gcd function
#
# Examples:
#
# Input: a = 20, b = 28
# Output: 4
# Explanation: GCD of 20 and 28 is 4
# Input: a = 60, b = 36
# Output: 12
# Explanation: GCD of 60 and 36 is 12
# Constraints:
#
# 1 ≤ a, b ≤ 109

"""The Euclidean Algorithm is an ancient and highly efficient method for finding the
Greatest Common Divisor (GCD) of two numbers.Its core principle is based on this
mathematical rule: The GCD of two numbers does not change if the larger number is
replaced by its remainder when divided by the smaller number.Instead of checking every
 single number to see if it's a divisor (which is slow), the algorithm continuously
 shrinks the two numbers using the modulo operator (%) until one of them becomes zero.
 How it Works (Step-by-Step)Let's find the GCD of 48 and 18.Divide the larger number by
 the smaller number and find the remainder:$48 \div 18 = 2$ with a remainder of 12.
 (In code: 48 % 18 = 12)Replace the numbers:Drop the original large number (48).
 Your new numbers to check are the previous smaller number (18) and the remainder
 (12).Repeat the process:Divide 18 by 12.$18 \div 12 = 1$ with a remainder of 6.
 (In code: 18 % 12 = 6)Your new numbers are now 12 and 6.Repeat until the remainder
 is 0:Divide 12 by 6.$12 \div 6 = 2$ with a remainder of 0. (In code: 12 % 6 = 0)Your
 new numbers are 6 and 0.Once you hit a remainder of 0, you stop. The last non-zero
 number (which is 6) is your GCD.Why this matches your Python codeIn the code you are
  currently working with:Pythondef gcd(self, a, b):
    while b > 0:            # Keep going until the remainder (b) becomes 0
        a, b = b, a % b     # Replace 'a' with 'b', and 'b' with the new remainder
    return a                # Return the last non-zero number
This single line a, b = b, a % b perfectly executes steps 1 and 2 of the algorithm simultaneously, rapidly shrinking even massive numbers down to their GCD in just a few loops."""

class Solution:
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a
s1 = Solution()
print(s1.gcd(80,100))

# def gcd(a, b):
#     gcdlist = []
#     for i in range(1, a + 1):
#         if a % i == 0 and b % i == 0:
#             gcdlist.append(i)
#     return max(gcdlist)
# print(gcd(20,28))
#
#
# class Solution:
#     def gcd(self, a, b):
#         gcdlist = []
#         for i in range(1, a + 1):
#             if a % i == 0 and b % i == 0:
#                 gcdlist.append(i)
#         return max(gcdlist)
# g1 = Solution()
# print(g1.gcd(20,28))


# class Solution:
#     def gcd(self, a, b):
#         larg = max(a, b)
#         for i in range(1, larg):
#             if a % i == 0 and b % i == 0:
#                 gcdd= i
#         return gcdd
#
# g1 = Solution()
# print(g1.gcd(20, 28))

"""what other problems can be solved using this algorithm
Least Common Multiple (LCM): The most common immediate application. Once you have the GCD, you can instantly find the LCM using the formula LCM(a,b)= 
GCD(a,b)
∣a×b∣
​
 .

Simplifying Fractions: To reduce a fraction to its absolute lowest terms, you calculate the GCD of the numerator and the denominator, and then divide both by that GCD.

Checking for Co-Primes: Two numbers are "co-prime" (or relatively prime) if they share no common divisors other than 1. This is verified by checking if GCD(a,b)=1.

Solving Linear Diophantine Equations: These are algebraic equations where you only look for integer solutions, typically in the form ax+by=c. This equation only has an integer solution if GCD(a,b) perfectly divides c.

Cryptography (RSA Algorithm): An advanced version, known as the Extended Euclidean Algorithm, is a foundational pillar of modern cybersecurity. It is used to compute the modular multiplicative inverse, which is required to generate the public and private keys used to encrypt data on the internet.

Finding the GCD of Multiple Numbers: The algorithm scales easily. To find the GCD of an entire array of numbers, you just apply it sequentially: GCD(a,b,c)=GCD(GCD(a,b),c)."""





