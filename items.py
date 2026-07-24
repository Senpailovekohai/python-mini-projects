
items={
    "water":{"Price":0.50,"Stock":3},
    "juice":{"Price":1.20,"Stock":2},
    "chips":{"Price":0.80,"Stock":5},
    "chocolate":{"Price":1.50,"Stock":1},
    "gum":{"Price":0.30,"Stock":0}
}
for item in items:
    print(
        item,
        "- Price:",
        items[item]["Price"],
        "- Stock",
        items[item]["Stock"]

    )
balance=0.0
while True:
    print("1. Insert Coin")
    print("2. Select")
    print("3. Cancle")
    print("4. Exit")

    choice=(input("Enter your choice:")).strip()
   
    if choice=="1":
        amount=float(input("Insert your coin:"))
        balance+=amount
        print("Your balance is: $",balance)
    

    elif choice=="2":
        select=input("Enter the item you wanna select:").lower().strip()
        if select in items:
            if items[select]["Stock"]>0:
                if balance>=items[select]["Price"]:
                    print("Item Dispensing!!")
                    items[select]["Stock"]-=1
                    balance-=items[select]["Price"]
                    print("Your remaning balance: $",balance)
                else:
                    need=items[select]["Price"]-balance
                    print(f"You need ${need:.2f} more for the tranasction.")

            else:
                print("Item is out of stock!!")

        else:
            print("Items is not available.")

    elif choice=="3":
        print("Refund: $",balance)
        balance=0


    elif choice=="4":
        print("Changed: $",balance)
        print("Thanks for shoping with us!!")
        break
