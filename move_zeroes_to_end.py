# Given an array of integers, write a function to move all zeroes to the end of the while maintaining the relative
# order of the other elements

def moveZeroes(nums):

    j = 0

    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1

    for x in range(j, len(nums)):
        nums[x] = 0

    return nums

array = [3,5,67,0,2,0,0,0,1,2,0]

moved = moveZeroes(array)
print(moved)




