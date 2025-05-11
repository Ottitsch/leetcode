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

def minRemoveToMakeValid(s: str) -> str:
    stack = []
    s = list(s)
    for i in range(len(s)):
        if s[i] == "(": stack.append(i)
        elif s[i] == ")":
            if stack: stack.pop()
            else: s[i] = ""
    for i in stack:
        s[i] = ""
    return "".join(s)

def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))

def singleNumber(self, nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

def maxProfit(prices: list[int]) -> int:
    min = prices[0]
    maxProfit = 0
    
    for num in prices:
        if(min>num):
            min=num
        maxProfit = max(maxProfit,num-min)
    return maxProfit

def lengthOfLongestSubstring(s: str) -> int:
    mapper = {}
    longest = 0
    current = 0

    for char in s:
        if char not in mapper:
            mapper[char]=1
            current+=1
        else:
            mapper={}
            mapper[char]=1
            current=1
        longest = max(longest,current)
    return longest

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))













