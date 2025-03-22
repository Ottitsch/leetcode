def getConcatenation(self, nums: list[int]) -> list[int]:
    return  nums + nums

def containsDuplicate(nums: list[int]) -> bool:
    mySet = set()
    for num in nums:
        if num in nums:
            return True
        mySet.add(num)
    return False

print(containsDuplicate([1,2,3,1]))