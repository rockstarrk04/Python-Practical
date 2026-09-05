# nums = [1,2,3,400,5,6,7,8,9,100]
# largest = 0
# for i in nums:
#     if i > largest:
#         largest = i

# print(largest)

# # O(n)

#  Second largest 
# nums = [1,200,3,400,400,6,7,8,9,100]
# largest = 0
# second_largest = 0

# for i in nums:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i < largest:
#         second_largest = i

# print(second_largest)

# check whether list is sorted or not

#! Two Pointer Approach 
# nums = [1,2,3,4,5,5,5,5,9,10]
# is_sort = False

# for i in range(0,len(nums)-1):
#     if nums[i+1] >= nums[i]:
#         is_sort = True
#     else:
#         is_sort = False
#         break

# if is_sort:
#     print('Sorted')
# else:
#     print('Unsorted')


# ! String Palindrome check

#  ignore all other than characters
# str = "neveroddoreven"
# is_palindrome = True
# left = 0    
# right = len(str) - 1

# while left < right:
#     if str[left] == str[right]:
#         left += 1
#         right -= 1
#     else:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print('Palindrome')
# else:
#     print('Not Palindrome')



def is_palindrome_pointers(s) :
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters on the left
        if not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters on the right
        elif not s[right].isalnum():
            right -= 1
        # Compare characters case-insensitively
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
            
    return True

# Examples
print(is_palindrome_pointers("Never odd or even!"))  # True
print(is_palindrome_pointers("hello"))               # False
