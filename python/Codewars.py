def even_chars(st):
    if len(st)<2 or len(st)>100:
        return "invalid string"
    return list(st[1::2])

def age(x, y):
    return y * x / (y - 1)

def flick_switch(lst):
    response = []
    flick=False
    for elem in lst:
        if elem == "flick":
            flick=True
        if flick==False:
            response.append(True)
        else:
            response.append(False)
    return response

print(flick_switch(['codewars', 'flick', 'test']))

# incomplete
def dna_to_rna(dna):
    rna = ""
    for char in dna:
        if(char=='T'):
            rna+='U'
            continue
        rna+=char

def opposite(number):
    return number * -1

print(opposite(1),opposite(14),opposite(-34))

# speed of aircrafts is given in *knots*
# travelTime is in *minutes*
# travel distance should be returned in *kilometers*

def travel_distance(avg_speed, travel_time):
    KM_PER_MILE = 1.852
    travel_hours = travel_time / 60
    travel_miles = avg_speed * travel_hours
    travel_kms = travel_miles * KM_PER_MILE
    return travel_kms

def remove_exclamation_marks(s):
	return s.replace('!', '')

def are_you_playing_banjo(name):
    if(name[0].lower()=="r"):
       return name + " plays banjo" 
    return name + " does not play banjo"

print(are_you_playing_banjo("Rex"))
print(are_you_playing_banjo("tom"))

from functools import reduce
import operator

def grow(arr):
    return reduce(operator.mul, arr)

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

