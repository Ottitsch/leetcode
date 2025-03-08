import heapq
from collections import defaultdict


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

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(nums)-1
    pos = [(value, index) for index, value in enumerate(nums)]
    pos.sort()
    while(left<right):
        sum = pos[left][0]+pos[right][0]
        if(sum==target):
            break
        if(sum<target):
            left+=1
        else:
            right-=1
    return pos[left][1],pos[right][1]

def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    typesafe: str = "hello"
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

def groupAnagrams(self, strs: list[str]):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dict = defaultdict(list)
    for str in strs:
        dict[tuple(sorted(str))].append(str)
    return list(dict.values())

def removeElement(nums: list[int], val: int):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k=0
    for num in nums:
        if(num!=val):
            nums[k]=num
            k+=1
    return k

def majorityElement(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sorted(nums)[len(nums)/2]

def sortArray(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    minHeap = []
    for num in nums:
        heapq.heappush(minHeap,num)
    for i in range(len(nums)):
        nums[i] = heapq.heappop(minHeap)
    return nums

def sortColors(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red=0
    white=0
    blue=0
    for color in nums:
        if color==0:
            red+=1
        if color==1:
            white+=1
        if color==2:
            blue+=1
    k = len(nums)
    while blue>0:
        nums[k]=2
        k-=1
        blue-=1
    while white>0:
        nums[k]=1
        k-=1
        white-=1
    while red>0:
        nums[k]=0
        k-=1
        red-=1
