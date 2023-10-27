def twoSum(nums, target):

        num_dict = {}
        pairs = []
        for i, num in enumerate(nums):
            # Обчислюю різницю між цільовим значенням і поточним числом
            complement = target - num
            if complement in num_dict:
                pairs.append([num_dict[complement], i])
            num_dict[num] = i

        return pairs

nums1 = [3, 6, 1, 8]
target1 = 9
print(twoSum(nums1, target1))

nums2 = [1, 2, 3, 4, 5]
target2 = 9
print(twoSum(nums2, target2))

nums3 = [10, 20, 30, 40, 50]
target3 = 60
print(twoSum(nums3, target3))

nums4 = [3, 5, 10, 2]
target4 = 6
print(twoSum(nums4,target4))

nums5 = [1, 2, 3, 4, 5, 6,  7, 8, 9]
target5 = 10
print(twoSum(nums5,target5))
#0,8 1,7, 2,6, 3,5




