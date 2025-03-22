from collections import Counter

def getConcatenation(self, nums: list[int]) -> list[int]:
    return  nums + nums

def containsDuplicate(nums: list[int]) -> bool:
    mySet = set()
    for num in nums:
        if num in nums:
            return True
        mySet.add(num)
    return False

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print(isAnagram("he2y","yeh2"))