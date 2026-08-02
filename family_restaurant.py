menu={
    "Rice" : 50,
    "Naan" : 18,
    "Butter Naan" : 20,
    "Paneer Tikka" : 250,
    "Mushroom Chilli" : 260,
    "Lemon Mojito" : 149
}
print("============================================================================")
print("Welcome to the Family Restaurant!!!!!!!!!!")
print("============================================================================")
print(" Please find the menu below: ")
print("\nRice: Rs 50\nNaan: Rs 18\nButter Naan: Rs 20\nPaneer Tikka: Rs 250\nMushroom Chilli: Rs 260\nLemon Mojito: Rs 149")

order_total=0
order_1=input("What do you want to order ? : ")
if order_1 in menu:
    order_total += menu[order_1]
    print(f"your item {order_1} has been added to your order to your cart ")
else:
    print(f"Sorry {order_1} item is not available now ")
another_order=input("do you want anything else(yes/no) ? ")
if another_order=="yes":
    order_2=input("Enter your Second item: ")
    if order_2 in menu:
        order_total +=menu[order_2]
        print(f"your item {order_2} has been added to your order to your cart ")
    else:
        print(f"Sorry {order_2} item is not available now ")

#Discount check
discount=0
final_amount=0

if order_total >100:
    discount=order_total*5/100
    final_amount=order_total-discount
else:
    final_amount=order_total

#Final amount print
print("============================================================================")
print("======== Bill =========")
print("Amount brfore discount: ",order_total)
print("Discount : \n",discount)
print(f"Your Final amount is : {final_amount}")
print("Thank You")