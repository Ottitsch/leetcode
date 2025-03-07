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

def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    mySet = set()
    for i in range(0,len(nums)):
        if nums[i] in mySet:
            return True
        mySet.add(nums[i])
    return False

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    for idx in set(s):
        if s.count(idx) != t.count(idx):
            return False
    return True

print(isAnagram("anagram","nagaram"))