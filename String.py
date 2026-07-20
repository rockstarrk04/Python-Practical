msg = 'python'

print(msg[0])   # p
print(msg[1])   # y
print(msg[2])   # t
print(msg[3])   # h
print(msg[4])   # o
print(msg[5])   # n
#print(msg[6])   # IndexError: string index out of range 
print() 

print() # new line

msg = 'python'

print(msg[-1])  # n
print(msg[-2])  # o
print(msg[-3])  # h
print(msg[-4])  # t
print(msg[-5])  # y
print(msg[-6])  # p
#   print(msg[-7])  # IndexError: string index out of range

print('Extracting more than one character and merging together using Concatenation operator')

print() # new line
msg = 'Ramkumar'
print(msg[0] + msg[-1])
# Output : Rr

print("Hello")

message = 'hello world'
print(message[10:-5:-1])

a = 'welcome to python class'
print(a[3:10:1])