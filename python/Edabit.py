import math
from datetime import datetime


def count_true(lst):
    count=0
    for var in lst:
        if var is True:
            count+=1
    return count

def int_to_str(num):
    return int(num)

def str_to_int(num):
    return str(num)

def total_overs(balls):
	return float(int(balls/6)) + balls%6/10

def top_note(student):
    return {
        "name": student["name"],
        "top_note": max(student["notes"])
    }

def area_of_country(name, area):
    return name+ " is "+str(round(area/148940000*100,2)) + "% of the total world's landmass"

def format_date(date):
    return str(date[6:] + date[3:5] + date[0:2])

def encode_morse(message):
    response=""
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    for char in message:
        response+=char_to_dots[char.capitalize()] + " "
    return response[:-1]

def has_friday_13(month, year):
    return datetime(year,month,13).strftime("%A")=='Friday'

def encrypt(word):
    response=""
    vowel_to_number = {
        'a':'0',
        'e':'1',
        'i':'2',
        'o':'2',
        'u':'3'
    }
    for char in reversed(word):
        if char in vowel_to_number:
            response+=vowel_to_number[char]
        else:
            response+=char
    return response+"aca"

def climb(stamina, obstacles):
    count = 0
    for i in (a - b for a, b in zip(obstacles, obstacles[1:])):
        mod = (i < 0) + 1
        stamina -= -(-abs(i)//1) * mod
        if stamina < 0: return count
        count += 1
    return count

def shift_sentence(txt):
    response=""
    word_list = txt.split()
    if len(word_list) == 1:
        return txt
    char=word_list[-1][0]
    for word in word_list:
        response+=char+word[1:]+" "
        char=word[0]
    if response[-1]==" ":
        return response[:-1]
    return response

def majority_vote(lst):
    for i in set(lst):
        if lst.count(i)>len(lst)//2:
            return i
    return None

def censor_string(txt, lst, char):
    for word in lst:
        txt = txt.replace(word, char*len(word))
    return txt

def freed_prisoners(prison):
    if prison[0]==0:
        return 0
    i = 0
    count=1
    for cell in prison:
        if cell == i%2:
            count+=1
            i+=1
    return count

def interview(lst, tot):
    maxTime = {
        "very easy":5,
        "easy":10,
        "medium":15,
        "hard":20
    }
    totalMax = 120
    format = ["very easy", "very easy", "easy", "easy", "medium", "medium", "hard", "hard"]
    if(len(lst)<len(format)):
        return "disqualified"
    for index,element in enumerate(lst):
        if element>maxTime[format[index]]:
            return "disqualified"
    return "qualified" if tot <= totalMax else "disqualified"

def snakefill(n):
    return math.floor(math.log2(n * n))

def tidy_link(url, name, *hover_text):
    if hover_text:
        return '['+name+']('+url+' "'+hover_text+'")'
    else:
        return '['+name+']('+url+')'

print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))

def mood_today(mood="neutral"):
    return "Today, I am feeling " + mood

print(mood_today())
print(mood_today("happy"))

def parity_analysis(num):
    return (sum(int(d) for d in str(num))) % 2 == num % 2

print(parity_analysis(243))
print(parity_analysis(12))
print(parity_analysis(3))

def valid(num):
   return num.isdigit() and len(num) in (4, 6)

print(valid("1234"))
print(valid("45135"))
print(valid("89abc1"))
print(valid("900876"))
print(valid(" 4983"))

def convert_to_hex(word):
	return ' '.join(f"{ord(c):02x}" for c in word)

print(convert_to_hex("hello world"))
print(convert_to_hex("Big Boi"))
print(convert_to_hex("Marty Poppinson"))

def bonus(days):
    if days <= 32:
        return 0
    bonus = 0
    if days > 32:
        bonus += (min(days, 40) - 32) * 325
    if days > 40:
        bonus += (min(days, 48) - 40) * 550
    if days > 48:
        bonus += (days - 48) * 600
    return bonus
        

print(bonus(15))
print(bonus(37))
print(bonus(50))

def loves_me(n):
    phrases = []
    for i in range(n):
        if i % 2 == 0:
            phrase = "Loves me"
        else:
            phrase = "Loves me not"
        
        if i == n - 1:
            phrase = phrase.upper()
        
        phrases.append(phrase)
    
    return ", ".join(phrases)

print(loves_me(3))
print(loves_me(6))
print(loves_me(1))






