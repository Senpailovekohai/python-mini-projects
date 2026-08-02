from vending_machine import VendingMachine

items_kdu={"water":{"Price":2,"Stock":3},
           "chips":{"Price":3,"Stock":2},
           "monster":{"Price":5,"Stock":4},
           "Chocolate":{"Price":4,"Stock":3}
}
machineA=VendingMachine("KDU",items_kdu)
machineB=VendingMachine("Sokcho",items_kdu)

while True:
    print("1.Show Items")
    print("2.Insert coin")
    print("3.Buy Items")
    print("4.Exit")

    cho=input("Enter your choice:").strip()

    if cho=="1":
         machineA.show_items()

    elif cho=="2":
         amount=float(input("Enter Your coin:"))
         machineA.insert_coin(amount)

    elif cho=="3":
         choice=input("Enter your choice:").strip().lower()
         result=machineA.buy_item(choice)
         if result:
                print("Item is successfully Purchased!")
         else:
              print("Purchased fail")

    elif cho=="4":
         remaining_balance=machineA.return_balance()
         print("Your remaining balance:",remaining_balance)
         break
       
