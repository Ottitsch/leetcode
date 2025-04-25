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

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hM = {num: i for i, num in enumerate(nums)}
    for i in range(len(nums)):
        value = target-nums[i]
        if value in hM and hM[value]!=i:
            return [hM.get(target-nums[i]),i]

def longestCommonPrefix(self, strs):
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix