def twoSum(nums, target):
    chk_map = {}
    for index, val in enumerate(nums):
        compl = target - val
        if compl in chk_map:
            indices = [chk_map[compl], index]
            print(indices)
            return [indices]
        else:
            chk_map[val] = index
    return False

print(twoSum([12, 53, 64, 67, 2, 1, 3, 4, 6], 68))