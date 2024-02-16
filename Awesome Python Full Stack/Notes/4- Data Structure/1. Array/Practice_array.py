def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    left = 0
    for i in range(1, len(nums)):
        if nums[left] == nums[i]:
            continue
        else:
            left += 1
            nums[left] = nums[i]
    return left + 1


nums = [2, 3, 45, 6, 7, 8, 9, 8, 3, 22, 32, 2]
removeDuplicates(nums)
a, b = 0, 1
n = int(input("Input: "))
while a < n:
    print(a)
    a, b = b, a+b
n = int(input(" Input: "))
i = 1
while i <= 10:
    print(n, " *", i," =", n*i)
    i+=1


