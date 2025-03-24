from collections import Counter

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