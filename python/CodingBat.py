def sum13(nums):
    prev=0
    count=0
    for num in nums:
        if num == 13 or prev%2==1:
            prev+=1
            continue
        count+=num
    return count

def sum67(nums):
    count=0
    skip=False
    for num in nums:
        if num==6:
            skip=True
        if num==7 and skip is True:
            skip=False
            continue
        if skip is False:
            count+=num
    return count

def has22(nums):
    prev=0
    for num in nums:
        if num==2 and prev==2:
            return True
        if num==2:
            prev=2
        else:
            prev=0
    return False

def count_evens(nums):
    count=0
    for num in nums:
        if num%2==0:
            count+=1
    return count

def make_chocolate(small, big, goal):
    max_big_bars = min(big, goal // 5)
    remaining = goal - max_big_bars * 5
    if remaining <= small:
        return remaining
    return -1

def xyz_there(str):
    if len(str) == 0:
        return False
    for char in range(len(str)-2):
        if str[char:char+3] != "xyz":
            continue
        if str[char-1] != "." or char == 0:
            return True
    return False

def front_times(str, n):
    front = str[0:3]
    return front*n
print(front_times("Chocolate",3))
print(front_times("Chocolate",2))
print(front_times("Abc",3))
print(front_times("Ab",3))

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars>=40
    return cigars>=40 and cigars<=60


print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

