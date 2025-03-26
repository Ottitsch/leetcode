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
        value = target-nums[i]
        if value in hM and hM[value]!=i:
            return [hM.get(target-nums[i]),i]

def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    for char in zip(*strs):
        if len(set(char)) == 1:
            res+= char[0]
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
    counter = [nums[0],0]
    for num in nums:
        if(num==counter[0]):
            counter[1]+=1
        else:
            counter[1]-=1
        if(counter[1]<0):
            counter = [num,1]
        if(counter[1]>=len(nums)/2):
            break
    return counter[0]

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())














