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


