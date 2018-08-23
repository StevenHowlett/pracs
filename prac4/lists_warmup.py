numbers = [3,1,4,1,5,9,2]
# #numbers[0] will show 3, [-1] will show 2, [3] will show 4,numbers[:3] will show 4 and 9
# #numbers[:-1] will show the list in reverse,numbers[3:4} will show 4 and 1,5 in numbers will show 1,
# #7 in numbers will show 0, "3" in numbers will show 0 becuase it's a string,
# # and numbers + [6,5,3] will show numbers[3,1,4,1,5,9,2,[6,5,3]]
# #i was wrong
# print(numbers)
# print (numbers[0])
# print (numbers[-1])
# print (numbers[3])
# print (numbers[:-1])
# print (numbers[3:4])
# print (5 in numbers)
# print (7 in numbers)
# print(("3" in numbers))
# print(numbers+[6,5,3])

numbers[0]=10
print (numbers)
numbers[-1]=1
print(numbers[2:])
print("there is a nine in numbers: {}".format(9 in numbers))