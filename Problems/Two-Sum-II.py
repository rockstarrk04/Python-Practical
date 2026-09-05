
#! Brute Force Approach
#? Suitable for Sorted and Un-sorted list/array
# nums = [2,7,11,15,17]
# target = 19

# Found = False

# for i in range(0 , len(nums)-1): # 0
#     for j in range(i+1 , len(nums)):  # 4
#         if nums[i] + nums[j] == target: # 2+17
#             print(f'index {i} and index {j} are the numbers')
#             Found = True

# if not Found:
#     print('Not Found')


#! Optimal Approach
#? Suitable for Sorted list/array
nums = [2,7,11,15,17]   
target = 19
Found = False
left = 0
right = len(nums)-1

while left < right:
    if nums[left] + nums[right] == target : 
        print(f'index {left} and index {right} are the numbers')
        Found = True
        break

    elif nums[left] + nums[right] > target :
        right = right - 1

    elif nums[left] + nums[right] < target :
        left = left + 1
        
if not Found:
    print('Not Found')