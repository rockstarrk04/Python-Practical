'''
    # iterate from starting
    # add the character/digit in new string 
    if first 6 appear , then change to 5 
    if next 6 appears , continue
    add other character/digit in new string
'''

num = 123466789
string = str(num)
res = ""
count = 0
for i in string:
    # print(i,end='')
    if count == 0:
        if i == '6':
            res = res + '5'
            count += 1
        else:
            res = res + i
    elif count >= 1:
        res = res + i

print(int(res))