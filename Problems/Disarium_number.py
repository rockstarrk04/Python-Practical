#!Disarium number
#? A Disarium number is a number where the sum of its digits raised to the power of their respective positions
#? (counting from left to right, starting at 1) equals the number itself. For example, 135 is a Disarium number 
#? because 1¹ + 3² + 5³ = 1 + 9 + 125 = 135.


#  find the count of the given digits
#  find the value digit value power the respective positve (1¹ + 3² + 5³)
#  sum all findings
#  check and compare the sum value and original value

num = 518   
s_num = str(num)
sum = 0
for i,val  in enumerate(s_num,start=1):
    sum = sum + (int(val)**i)

# for i in range(1, len(s_num)+1):
#     sum = sum + (int(s_num[i-1]) ** i)
   
if sum == num:
    print(f"{num} is Disarium number")
else:
    print(f"{num} is not Disarium number")