import heapq
import math
from collections import defaultdict, Counter
from typing import Optional


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

def maxProfit(prices: list[int]):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxProfit = 0
    minPurchase = prices[0]
    for i in range(1, len(prices)):
        maxProfit = max(maxProfit, prices[i] - minPurchase)
        minPurchase = min(minPurchase, prices[i])
    return maxProfit


def reverseString(s: list[str]):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    s.reverse()




def minEatingSpeed(piles: list[int], h: int):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    pileCount = len(piles)
    s = sum(piles)
    left = math.ceil(s / h)
    right = max(piles) if h == pileCount else int((s - pileCount) / (h - pileCount) + 1)
    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for bananas in piles:
            hours += (bananas // mid) + 1 if bananas % mid else bananas // mid
        if hours > h:
            left = mid + 1
        else:
            right = mid - 1
    return left


def guess(num: int) -> int:
    pass

def guessNumber(self, n: int) -> int:
    left = 1
    right = n
    while left <= right:
        mid = (right + left) // 2
        if guess(mid) == 0:
            return mid
        if guess(mid) == 1:
            left = mid + 1
        if guess(mid) == -1:
            right = mid - 1
    return -1
    

def plusOne(self, digits: list[int]) -> list[int]:
        m = int(''.join(str(x) for x in digits))+1
        return [int(x) for x in str(m)]


import base64

def encode(strs: list[str]) -> str:
    data = ""
    for word in strs:
        data += word + "#"
    
    return base64.b64encode(bytes(data,'utf-8'))


def decode(s: str) -> list[str]:
    data = (base64.b64decode(s)).decode('utf-8')
    strs = []
    word = ""
    for char in data:
        if(char!="#"):
            word+=str(char)
        else:
            strs.append(word)
            word=""
    return strs

def shipWithinDays(weights: list[int], days: int) -> int:
    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left + right) // 2
        if canTransferInDays(mid, weights, days):
            right = mid  # Try a smaller capacity
        else:
            left = mid + 1  # Increase capacity

    return left


def canTransferInDays (weightload, weights: list[int], days):
    current_weight = 0
    required_days = 1  # At least one day is needed
        
    for weight in weights:
        if current_weight + weight > weightload:
            required_days += 1
            current_weight = 0  # Start a new day
        current_weight += weight 
        if required_days > days:
            return False
    return True

def searchInsert(self, nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        return sorted(nums).index(target)

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than rightmost element, min must be to the right
        if nums[mid] > nums[right]:  
            left = mid + 1  # Search in the right half
        else:
            right = mid  # Search in the left half, including mid

    return nums[left]  # After loop ends, left == right, pointing to the minimum

def checkOverlap(inputlist: list):
    small = float('inf')
    big = float('-inf')

    while inputlist:
        temp1, temp2 = inputlist.pop()

        if small < temp1 < big or small < temp2 < big:
            return False

        small = min(small, temp1)
        big = max(big, temp2)

    return True

#alternate logic
def checkOverlap(inputlist: list):
    # Sort intervals by start time
    inputlist.sort()

    for i in range(len(inputlist) - 1):
        # Get current and next interval
        current_start, current_end = inputlist[i]
        next_start, next_end = inputlist[i + 1]

        # If current interval's end overlaps with the next interval's start
        if current_end > next_start:
            return False

    return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    if n == length:
        return head.next
    current = head
    for _ in range(length - n - 1):
        current = current.next
    current.next = current.next.next
    return head

def rangeBitWiseAnd(left: int, right: int) -> int:
    response = 0
    while left != right:   
        left >>= 1
        right >>= 1
        response += 1
    return left << response

"""
def checkStraightLine(coordinates: list[list[int]]) -> bool:
    x0,y0 = coordinates[0]
    x1,y1 = coordinates[1]
    for x, y in coordinates[2:]:
        if (x1 - x0) * (y - y0) != (y1 - y0) * (x - x0):
            return False
    return True
"""

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


def convertToTitle(columnNumber: int) -> str:
    output = ""
    while columnNumber > 0:
        output = chr(ord('A') + (columnNumber - 1) % 26) + output
        columnNumber = (columnNumber - 1) // 26
    return output

print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))

def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for char in columnTitle:
            col_num = col_num * 26 + (ord(char) - 64)
        
        return col_num

def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n): a,b=b,a+b
        return a

def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
	return date(year, month, day).strftime("%A")
