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

print(total_overs(945))