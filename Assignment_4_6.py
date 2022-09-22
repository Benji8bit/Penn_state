def verify(number):  # do not change this line!

    # write your code here so that it verifies the card number

    # be sure to indent your code!

    sum = 0
    i = 0
    for i in range(len(number)):
        if (i==4)or(i==9):
            continue
        sum+=int(number[i])

    if number[0]!="4":
        return 1

    elif (int(number[3]) - int(number[5]) != 1):
        return 2

    elif (sum%4)!=0:
        return 3

    elif ((int(number[0]+number[1]) + int(number[7]+number[8]))!=100):
        return 4

    else:
        return True

#    return True  # modify this line as needed

input = "4094-3460-2754"  # change this as you test your function
output = verify(input)  # invoke the method using a test input
print(output)  # prints the output of the function
# do not remove this line!
