import math
from collections import Counter, defaultdict


def getConcatenation(self, nums: list[int]) -> list[int]:
    return nums + nums


def containsDuplicate(nums: list[int]) -> bool:
    mySet = set()
    for num in nums:
        if num in nums:
            return True
        mySet.add(num)
    return False


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def twoSum(nums: list[int], target: int) -> list[int]:
    hM = {num: i for i, num in enumerate(nums)}
    for i in range(len(nums)):
        value = target - nums[i]
        if value in hM and hM[value] != i:
            return [hM.get(target - nums[i]), i]


def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    for char in zip(*strs):
        if len(set(char)) == 1:
            res += char[0]
        else:
            return res
    return res


def removeElement(nums: list[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


#HASHMAP SOLUTION:
def majorityElement(nums: list[int]) -> int:
    hM = {num: i for i, num in enumerate(nums)}
    largest_key = max(hM, key=lambda k: hM[k])
    return largest_key


#algorithmic solution:
def majorityElement(nums: list[int]) -> int:
    counter = [nums[0], 0]
    for num in nums:
        if (num == counter[0]):
            counter[1] += 1
        else:
            counter[1] -= 1
        if (counter[1] < 0):
            counter = [num, 1]
        if (counter[1] >= len(nums) / 2):
            break
    return counter[0]


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())


def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def sortArray(self, nums: list[int]) -> list[int]:
    def mergeTwoSortedArrays(a, b, res):
        i, j, k = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res[k] = a[i]
                i += 1
            else:
                res[k] = b[j]
                j += 1
            k += 1
        res[k:] = a[i:] if i < len(a) else b[j:]

    def mergesort(nums):
        if len(nums) == 1: return
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]
        mergesort(L)
        mergesort(R)
        mergeTwoSortedArrays(L, R, nums)

    mergesort(nums)
    return nums


def calPoints(operations: list[str]) -> int:
    resultStack = []

    for op in operations:
        if op == "C":
            if resultStack:
                resultStack.pop()
        elif op == "D":
            if resultStack:
                resultStack.append(2 * resultStack[-1])
        elif op == "+":
            if len(resultStack) >= 2:
                resultStack.append(resultStack[-1] + resultStack[-2])
        else:
            resultStack.append(int(op))  # Assume it's a valid integer string

    return sum(resultStack)


def isValid(s: str) -> bool:
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in d:  # 1
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:  # 2
            return False
    return len(stack) == 0


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    carFleetMap = sorted(zip(position, speed), reverse=True)
    head = None
    counter = 0

    def checkIfCatchup(headPos, headSpeed, carPos, carSpeed, target) -> bool:
        # If car is slower or same speed, it can't catch up
        if carSpeed <= headSpeed:
            return False
        time_to_target = (target - headPos) / headSpeed
        car_distance = carPos + (carSpeed * time_to_target)
        return car_distance >= target

    for pos, speed in carFleetMap:
        if head is None:
            head = pos, speed
            counter += 1
            continue
        headPos, headSpeed = head
        if not checkIfCatchup(headPos, headSpeed, pos, speed, target):
            head = pos, speed
            counter += 1

    return counter

def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1


def strongPasswordChecker(password: str) -> int:
    n = len(password)
    missing_lower = int(not any(c.islower() for c in password))
    missing_upper = int(not any(c.isupper() for c in password))
    missing_digit = int(not any(c.isdigit() for c in password))
    missing_types = missing_lower + missing_upper + missing_digit

    # Count repeating sequences
    i = 2
    repeats = []
    while i < n:
        if password[i] == password[i - 1] == password[i - 2]:
            j = i - 2
            while i < n and password[i] == password[j]:
                i += 1
            repeats.append(i - j)
        else:
            i += 1

    if n < 6:
        return max(6 - n, missing_types)

    elif n <= 20:
        replace = sum(length // 3 for length in repeats)
        return max(replace, missing_types)

    else:
        delete = n - 20
        over = repeats[:]
        # Step 1: Apply deletions to reduce replacements, prioritize sequences by mod 3
        buckets = [[], [], []]
        for r in over:
            buckets[r % 3].append(r)

        for mod in range(3):
            for i in range(len(buckets[mod])):
                if delete <= 0:
                    break
                r = buckets[mod][i]
                need = mod + 1
                reduce = min(delete, need)
                buckets[mod][i] -= reduce
                delete -= reduce

        # Step 2: Apply remaining deletions to any leftover repeating groups
        for mod in range(3):
            for i in range(len(buckets[mod])):
                if delete <= 0:
                    break
                r = buckets[mod][i]
                if r >= 3:
                    reduce = min(delete, r - 2)
                    buckets[mod][i] -= reduce
                    delete -= reduce

        # Step 3: Compute final replacements after all deletions
        replace = 0
        for mod in range(3):
            for r in buckets[mod]:
                if r >= 3:
                    replace += r // 3

        return (n - 20) + max(replace, missing_types)

def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid
    return left

def guess():
    pass

def guessNumber(n: int) -> int:
    left=1
    right=n
    while left<=right:
        mid=(right+left)//2
        if(guess(mid)==0):
            return mid
        if(guess(mid)==1):
            left=mid+1
        if(guess(mid)==-1):
            right=mid-1
    return -1

def minEatingSpeed(piles: list[int], h: int) -> int:
    left, right = 0, max(piles)
    while left<=right:
        mid=(right+left)//2
        if canEatAll(mid, piles, h):
            right=mid-1
        else:
            left=mid+1
    return left


def canEatAll(speed,piles,h):
    hours = 0
    for pile in piles:
        hours += math.ceil(pile / speed)
    return hours <= h


def mySqrt(x: int) -> int:
    if x==0:
        return x
    left,right=1,x
    while left<=right:
        mid=(right+left)//2
        print(left,right,mid)
        if(mid==x/mid):
            return mid
        if mid>x/mid:
            right=mid-1
        else:
            left=mid+1
    return right

def findMin(nums: list[int]) -> int:
    left,right=0,len(nums)-1
    while left<right:
        mid=(right+left)//2
        if(nums[mid]<nums[right]):
            right=mid
        else:
            left=mid+1
    return nums[left]

def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        if nums[mid]<nums[right]:
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
        else:
            if nums[left]<=target<nums[mid]:
                right=mid-1
            else:
                left = mid+1
    return -1

def nextGreatestLetter(letters: list[str], target: str) -> str:
    if target >= letters[-1] or target < letters[0]:
        return letters[0]

    left,right=0,len(letters)-1
    while left<=right:
        mid=(right+left)//2
        if(letters[mid]<=target):
            left=mid+1
        if(letters[mid]>target):
            right=mid-1
    return letters[left]

def targetIndices(self, nums: list[int], target: int) -> list[int]:
    startIndex = 0
    repetition = 0
    for i in range(len(nums)):
        if nums[i] < target:
            startIndex+=1
        elif nums[i] == target:
            repetition +=1
    return [i for i in range(startIndex,startIndex+repetition)]


def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    missing = set(range(n+1)) - set(nums)
    return missing.pop()

def singleNumber(self, nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

def hammingWeight(self, n: int) -> int:
    return bin(n)[2:].count('1')

def lemonadeChange(bills):
    fiveCollected = 0
    tenCollected = 0

    for bill in bills:
        if bill == 5:
            fiveCollected += 1
        elif bill == 10:
            tenCollected += 1
            fiveCollected -= 1
        elif bill == 20:
            if tenCollected > 0:
                tenCollected -= 1
                fiveCollected -= 1
            else:
                fiveCollected -= 3
        if fiveCollected < 0:
            return False
    return True

def jump(self, nums: list[int]) -> int:
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps

def countBits(n: int) -> list[int]:
    return [sum(map(int, bin(i)[2:])) for i in range(n+1)]

def addBinary(a: str, b: str) -> str:
    x=int(a,2)
    y=int(b,2)
    return bin(x+y)[2:]


def reverseBits(self, n: int) -> int:
    n = bin(n)[2:].zfill(32)
    rev = n[::-1]
    return int(rev, 2)

def missingNumber(self, nums: list[int]) -> int:
    n=len(nums)
    eSum = (n+1)*(n)/2
    return int(eSum-sum(nums))


def reverse(self, x: int) -> int:
    res = 0
    if x < 0:
        res = int(str(x)[1:][::-1]) * -1
    else:
        res = int(str(x)[::-1])
        
    if res > 2 ** 31 - 1 or res < -2 ** 31:
        return 0
        
    return res

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    index_dict = {}
    for i, n in enumerate(nums):
        if n in index_dict and i - index_dict[n] <= k:
            return True
        index_dict[n]=i
    return False

def checkStraightLine(coordinates: list[list[int]]) -> bool:
    x0,y0 = coordinates[0]
    x1,y1 = coordinates[1]
    for x, y in coordinates[2:]:
                        f (x1 - x0) * (y - y0) != (y1 - y0) * (x - x0):
                                return False
    return True

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

def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for char in columnTitle:
            col_num = col_num * 26 + (ord(char) - 64)

        return col_num











