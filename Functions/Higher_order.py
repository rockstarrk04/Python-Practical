def cube(num):
    return num * num * num



num = [2,1,4]

# higher order function definition
def operate(num , operation):
    for i in num:
        result = operation(i)
        print(result)

operate(num , cube)


def operate(num):
    for i in num:
        result = cube(i)
        print(result)
operate(num)