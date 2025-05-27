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
