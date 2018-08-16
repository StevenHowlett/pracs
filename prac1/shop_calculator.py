number_of_items=int(input("number of items:"))
list_1 = []
for i in range(0,number_of_items):
    price_of_item=float(input("price of item:{}".format(i+1)))
    if price_of_item > 100:
        price_of_item = price_of_item*.1
    list_1.append(price_of_item)

total=sum(list_1)
print('total price for {} items is ${:.2f} '.format(number_of_items,total))

