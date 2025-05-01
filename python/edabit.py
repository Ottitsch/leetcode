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

print(area_of_country("Russia",1648195))