import math
user_choice = "r"

while (user_choice=="r"):
    name = input("Please enter your name : ")
    product1 = input("Product name : ")
    price1 = int(input("Price : "))
    product2 = input("Product name : ")
    price2 = int(input("Price : "))
    product3 = input("Product name : ")
    price3 = int(input("Price : "))

    # Calculating subtotal, discount and final total
    subtotal = price1 + price2 + price3
    if (subtotal>=5000):
        discount_rate = 20/100
    elif (subtotal>=3000):
        discount_rate = 10/100
    elif (subtotal>=1000):
        discount_rate = 5/100
    else:
        discount_rate = 0

    discount = subtotal * discount_rate
    discount = math.floor(discount)
    final_total = subtotal - discount
    
    print(f"Subtotal : {subtotal}")
    print(f"Discount : {discount}")
    print(f"Final Total : {final_total}")
    
    user_choice = input("Enter 'a' for re-purchasing or type anything to exit : ").lower()
    if(user_choice=="r"):
        print("Please Wait...")
    else :
        print("Exiting...")
