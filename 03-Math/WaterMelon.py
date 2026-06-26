# Platform: Codeforces
# Problem: Watermelon (4A)
# Difficulty: 800
# Pattern: Math, Observation
# Time: O(1)
# Space: O(1)
#
# Clue:
# We need to split the watermelon into two EVEN positive parts.
#
# Observation:
# - If weight is odd → Impossible.
# - If weight is 2 → Impossible (1 + 1 are odd).
# - If weight is even and > 2 → Always possible.
#
# Formula:
# if w % 2 == 0 and w > 2:
#     YES
# else:
#     NO
#
# Learned:
# Don't overthink. Check small edge cases first, then look for a simple mathematical observation.

n = int(input())
print("YES" if (n % 2 == 0 and n > 2) else "NO")