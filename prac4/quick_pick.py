import random

MAX_NUMBER= 45
MIN_NUMBER=1

number_of_quick_picks=int(input("how many quick picks?"))
for i in range (number_of_quick_picks):
    quick_pick_list=[]
    for number in range(6):
        random_number = random.randint(MIN_NUMBER,MAX_NUMBER)
        while random_number in quick_pick_list:
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick_list.append(random_number)
    print (quick_pick_list)