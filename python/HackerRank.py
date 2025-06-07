def minion_game(string):
    vowels = "AEIOU"
    
    stuart_score = 0
    kevin_score = 0
    n = len(string)
    
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i
            
            
    if stuart_score == kevin_score:
        print("Draw")
    else:
        if stuart_score > kevin_score:
            print("Stuart " + str(stuart_score))
        else:
            print("Kevin " + str(kevin_score))

