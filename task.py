items={"water":{"Price":0.50,"Stock":3},
    "juice":{"Price":1.20,"Stock":2},
    "chips":{"Price":0.80,"Stock":5},
    "chocolate":{"Price":1.50,"Stock":1},
    "gum":{"Price":0.30,"Stock":0}}

def show_items():
    for item in items:
        print(item, "Price:",
              items[item]["Price"],
              "Stock:",
              items[item]["Stock"])

def insert_coin(balance):
    amount=float(input("Enter coin:"))
    balance+=amount
    return balance

def buy_items(balance):
    choice=input("Enter the item you want: ").strip()
    for item in items:
        while choice==item:
            if balance<items[item]["Price"]:
                amt=items[item]["Price"]-balance
                print(f"Your balance is{amt} not sufficent")

            else:
                print("Enjoy your item!")
                balance-=items[item]["Price"]
                return balance

            print(f"Your remaining balance is{balance}")
            break
        print ("You are out of stock!!")
        
            

