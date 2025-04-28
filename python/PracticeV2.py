def getConcatenation(nums: list[int]) -> list[int]:
    return nums + nums

def containsDuplicate(nums: list[int]) -> bool:
    mySet = []
    for num in nums:
        if(mySet.__contains__(num)):
            return True
        else:
            mySet.append(num)
    return False

def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def twoSum(nums: list[int], target: int) -> list[int]:
    hM = {num: i for i, num in enumerate(nums)}
    for i in range(len(nums)):
        value = target-nums[i]
        if value in hM and hM[value]!=i:
            return [hM.get(target-nums[i]),i]

def longestCommonPrefix(strs):
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# TODO: Rewrite this with a stack instead of rekursive function
def minRemoveToMakeValid(s: str) -> str:
    result=removeRekursive(s,"(",")")
    result=removeRekursive(result[::-1],")","(")
    return result[::-1]

def removeRekursive(s: str,c: str,b: str) -> str:
    result=""
    count=0
    for char in s:
        if char==c:
           count+=1
        if char==b:
            if count==0:
                continue
            count-=1
        result+=char
    return result

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
