def sum13(nums):
    prev=0
    count=0
    for num in nums:
        if num == 13 or prev%2==1:
            prev+=1
            continue
        count+=num
    return count

