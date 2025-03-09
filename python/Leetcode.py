import heapq
from collections import defaultdict, Counter


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

def lastStoneWeight(stones: list[int]):
    """
    :type stones: List[int]
    :rtype: int
    """
    minheap = []
    for stone in stones:
        heapq.heappush(minheap,-stone)
    while len(minheap)>1:
        y=heapq.heappop(minheap)
        x=heapq.heappop(minheap)
        if(x!=y):
            heapq.heappush(minheap,y-x)
    if minheap:
        return heapq.heappop(minheap)*-1
    return 0

def leastInterval(tasks: list[str], n: int):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
    min_time = (max_freq - 1) * (n + 1) + max_freq_count
    return max(len(tasks), min_time)

def findWords(words: list[str]):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    rtype = []
    for word in words:
        if canBeTyped("qwertyuiop",word) or canBeTyped("asdfghjkl",word) or canBeTyped("zxcvbnm",word):
            rtype.append(word)
    return rtype

def canBeTyped(letters: str, word):
    for letter in word:
        if not letters.__contains__(letter.lower()):
            return False
    return True

def findContentChildren(g: list[int], s: list[int]):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    g.sort(),s.sort()
    j=0
    for i in range(len(s)):
        if(j==len(g)):
            break
        if(g[j]<=s[i]):
            j+=1
    return j