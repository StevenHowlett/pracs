numbers=[1,2,3,4,5]
for i in range(0,len(numbers)):
    numbers[i]=int(input("enter number {} :".format(i+1)))
print(numbers)
print("the first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[-1]))
print("the largest number is {}".format(max(numbers)))
print("the smallest number is {}".format(min(numbers)))
print("the average of the number is {}".format(sum(numbers)/(i+1)))