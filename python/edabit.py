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

print(encode_morse("hello!"))