def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums + nums

def containsDuplicate(self, nums: List[int]) -> bool:
    mySet = []
    for num in nums:
        if(mySet.__contains__(num)):
            return True
        else:
            mySet.append(num)
    return False

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)