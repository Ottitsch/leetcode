def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    i = 1
    answer = []
    while(i<=n):
        toAdd=''
        if(i%3==0):
            toAdd+="Fizz"
        if(i%5==0):
            toAdd+="Buzz"
        if(toAdd!=''):
            answer.append(toAdd)
        else:
            answer.append(str(i))
        i+=1
    return answer

def getConcatenation(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = nums
    for i in range(0,len(nums)):
        ans.append(nums[i])
    return ans