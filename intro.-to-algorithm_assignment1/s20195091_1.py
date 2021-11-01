def mergeSort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left_nums = mergeSort(nums[:mid])
    right_nums = mergeSort(nums[mid:])

    merged_nums = []
    i = j = 0
    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] < right_nums[j]:
            merged_nums.append(left_nums[i])
            i += 1
        else:
            merged_nums.append(right_nums[j])
            j += 1
    merged_nums += left_nums[i:]
    merged_nums += right_nums[j:]
    return merged_nums

def findTarget(numArr, target):
    if target > numArr[len(numArr)-1]:
        return len(numArr) + 1
    else:
        for i in reversed(range(len(numArr))):
           if target >= numArr[i]:
              return i+1
           elif i == 0:
              return i+1


def solve(nums, target):
    numArr = mergeSort(nums)
    order = findTarget(numArr, target)
    return order