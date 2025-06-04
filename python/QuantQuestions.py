"""
    Ensemble of Quant Questions
"""
import math

# Bridge Corssing
"""
David, Emma, Frank, and Grace need to cross a river. The only possible way to cross the river is a bridge that can only hold at maximum 2 people at once. It's night time, so they can only cross the bridge using a lantern and they only have 1 lantern. Each pair of people can only cross at the pace of the slowest person. All people need to get across as fast as possible. Their crossing times are as follows: David takes 10 minutes, Emma takes 5 minutes, Frank takes 2 minutes, and Grace takes 1 minute. What is the minimum time required for all of them to get across to the other side?
"""
david = 10
emma = 5
frank = 2
grace = 1

# Optimal strategy:
# 1. Grace + Frank cross (2 min)
# 2. Grace returns (1 min)
# 3. David + Emma cross (10 min)
# 4. Frank returns (2 min)
# 5. Grace + Frank cross again (2 min)

solution = frank + grace + david + frank + frank
print(solution)

# Least Multiple of 15
"""
What is the least positive multiple of 15 whose digits consist of 1's and 0's only?
"""
#number is divisible by 5 if it ends in 0
#number is divisible by 3 if the 1's add up to 3
#therefore smallest number is 1110
#code to check if smaller number exists:
for i in range(1,1111):
    if i % 15 != 0:
        continue
    if all(c in '01' for c in str(i)):
        print(i)

# Seating Drama
"""
On a circular table of 5 seats, five people denoted 1,2,3,4,5 are seated. 4 wishes to sit immediately to the right of 2 while 2 sits immediately to the right of 5. Additionally 1 does not want to sit next to either one of 2 or 5. Who is to the left of 5?
"""
#4 wants to sit right of 2
#2 wants to sit to the right of 5
#1 does not want to sit next to 2 or 5

#5,2,4,1,3
#-> 3

# 2D Paths I
"""
You are playing a 2D game where your character is trapped within a 6×6 grid. Your character starts at (1,1) and can only move up and right. How many possible paths can your character take to get to (6,6)?
"""
solution = math.factorial(12) // (math.factorial(6) * math.factorial(6))
print(solution)

