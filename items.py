class VendingMachine:
    def __init__(self,location,items):
                self.items=items
                self.location=location
                self.balance=0


    def show_items(self):
        for item in self.items:
                print(item,
                      "Price:",
                      self.items[item]["Price"],"Stock:"
                      ,self.items[item]["Stock"])

    def insert_coin(self,amount):
         self.balance +=amount

    def buy_items(self,choice):
        if choice in self.items:
            if not self.items[choice]["Stock"]>0:
                   print("Out of stock!!")
            if self.items[choice]["Price"]<=self.balance:
                 self.balance-= self.items[choice]["Price"]
                 self.items[choice]["Stock"]-=1
            else:
                 print("Insufficent Balance!!")

        else:
             print("Item is not available!!")

             

            
                


machineA= VendingMachine()
machineb=VendingMachine()
print("KDU VENDING MACHINE")
machineA.show_items()
coin=float(input("Insert coin:"))
machineA.insert_coin(coin)
choice=input("Enter your choice:").strip().lower()
machineA.buy_items(choice)
print("BALANCE=",machineA.balance)

print("--------------------")
print("SOKCHO VENDING MACHINE")
machineb.show_items()
print("BALANCE=",machineb.balance)



