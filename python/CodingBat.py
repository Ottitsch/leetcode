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