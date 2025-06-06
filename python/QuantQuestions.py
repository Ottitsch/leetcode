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

# Couple Handshakes
"""
A room of four couples greet each other by shaking hands. If each person shakes the hand of every other person besides their partner, how many handshakes occur?
"""
#4 couples -> 8 people
#each person shakes 6 people's hands
#8*6
#one handshake consists of 2 people shaking hands
solution = 8*6 // 2
print(solution)

# Theater Seating
"""
Your taking your 10 students to the theater, the 5 boys and 5 girls are seated in a row. To ensure that the children are engaged during the movie, the teacher states that no two children of the same gender can sit next to each other. How many arrangements of the kids are possible?
"""
solution = math.factorial(5) * math.factorial(5) * 2
print(solution)

# Basic Dice Game I
"""
A casino offers a game with a 6-sided die where you're paid the value of the roll.
You can roll once and choose to keep the value, or re-roll once and take the second result.
What is the fair value of this game?
"""
#Expected value of a single roll of a 6-sided die
#(1+2+3+4+5+6)/6 = 3.5
#Player will re-roll if first roll is 1, 2, or 3 (since 3.5 is better)
#Player will keep if first roll is 4, 5, or 6
# Case 1: Re-roll on 1, 2, 3 -> 3 out of 6 outcomes -> probability 0.5
#Expected value of re-roll = 3.5
#Contribution to total EV: 0.5 * 3.5 = 1.75
# Case 2: Keep 4, 5, 6 -> average = (4+5+6)/3 = 5
#Contribution to total EV: 0.5 * 5 = 2.5
# Total expected value (fair value) = 1.75 + 2.5
solution = 1.75 + 2.5
print(solution)

# Dangerous Doubles
"""
Two fair coins are flipped at once. You receive $2 if exactly one head appears, 
but you lose $7 if you flip two heads. What is your expected profit/loss 
on this game if you play once?
"""
# Possible outcomes (each with probability 1/4):
#   HH -> payoff = -7
#   HT -> payoff = 2
#   TH -> payoff = 2
#   TT -> payoff = 0
# Sum of payoffs over all equally likely outcomes = (-7) + 2 + 2 + 0 = -3
# Expected value = (sum of payoffs) / 4 = -3/4 = -0.75
solution = (-7 + 2 + 2 + 0) / 4
print(solution)  # prints -0.75

# Probability of Unfair Coin I
"""
You have a pile of 100 coins. 1 of the coins is an unfair coin and has heads on both sides. The remaining 99 coins are fair coins. You randomly select a coin from the pile and flip it 10 times. The coin lands heads all 10 times. Calculate the probability that the coin you selected is the unfair coin.
"""
# Step 1 - Bayes Theorem
# P(Unfair | 10H) = (P(10H | Unfair) * P(Unfair) / P(10H)
# Step 2 - Compute the components
pUnfair = 1/100
pFair = 99/100
p10hUnfair = 1
p10hFair = 0.5**10
p10h = p10hUnfair * pUnfair + p10hFair * pFair
# Step 3 - Plug into Bayes Theorem
pUnfair10h = pUnfair / p10h
print(pUnfair10h)
