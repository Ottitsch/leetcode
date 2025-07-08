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

def characterReplacement(s: str, k: int) -> int:
    maxLen = 0
    maxCount = 0
    count = [0] * 26
    left = 0

    for right in range(len(s)):
        index = ord(s[right]) - ord('A')
        count[index]+=1
        maxCount = max(maxCount, count[index])

        if(right - left+1) -maxCount > k:
            count[ord(s[left])-ord('A')]-=1
            left+=1
        maxLen=max(maxLen,right-left+1)
    return maxLen

from collections import Counter

def checkInConclusion(s1: str, s2: str) -> bool:
    count1, count2 = Counter(s1),Counter(s2[:len(s1)])
    for i in range (len(s1),len(s2)):
        if count1 == count2:
            return True
        count2[s2[i-len(s1)]]-=1
        count2[s2[i]]+=1
    return count1==count2

def search(nums: list[int], target: int) -> int:
    left=0
    right=len(nums)
    while left<right:
        mid=(left+right)//2
        if target==nums[mid]:
            return mid
        if nums[left] < target:
            left = mid
        else:
            right = mid
    return -1

def searchInsert(nums: list[int], target: int) -> int:
    left=0
    right=len(nums)
    while left < right:
        mid=(left+right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left=mid+1
        else:
            right=mid
    return right

def plusOne(self, digits: List[int]) -> List[int]:
	for i in range(len(digits) - 1, -1, -1):
		if digits[i] + 1 != 10:
        	digits[i] += 1
            return digits
		digits[i] = 0
        if i == 0:
        	return [1] + digits

def isValid(s: str) -> bool:
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in d:  # 1
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:  # 2
            return False
    return len(stack) == 0

def validIp(temp: str) -> bool:
    if len(temp) > 3 or len(temp) == 0:
        return False
    if len(temp) > 1 and temp[0] == '0':
        return False
    if len(temp) and int(temp) > 255:
        return False
    return True

def solveIp(ans, output, ind, s, dots):
    if dots == 3:
        if validIp(s[ind:]):
            ans.append(output + s[ind:])
        return
    for i in range(ind, min(ind+3, len(s))):
        if validIp(s[ind:i+1]):
            new_output = output + s[ind:i+1] + '.'
            solveIp(ans, new_output, i+1, s, dots+1)


def restoreIpAddresses(s: str) -> list[str]:
    ans = []
    solveIp(ans, "", 0, s, 0)
    return ans

def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res
