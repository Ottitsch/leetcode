"""
    Ensemble of Quant Questions
"""

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
