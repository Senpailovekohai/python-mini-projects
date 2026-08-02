import copy
class VendingMachine:
    def __init__(self,location,items):
        self.items=copy.deepcopy(items)
        self.location=location
        self.balance=0
    def show_items(self):
        for item in self.items:
            print(
                item,"Price:",
                self.items[item]["Price"],
                "Stock:",self.items[item]["Stock"]
            )
    def insert_coin(self,amount):
        if not amount<0:
            self.balance+=amount
        else:
            return False

    def check_items(self,choice):
        return  choice in self.items

    def check_price(self,choice):
            if self.items[choice]["Price"]<=self.balance:
                return True
            else:
                return False      

    def check_stock(self,choice):
        if  self.items[choice]["Stock"]>0:
            return True
        else:
            return False
    
    def buy_item(self,choice):
        if  self.check_items(choice):
            if self.check_stock(choice) :
                if self.check_price(choice) :
                    self.balance-=self.items[choice]["Price"]
                    self.items[choice]["Stock"]-=1
                    return True
                else:
                    return False
            else:
                return False

        else:
            return False

    def return_balance(self):
        change=self.balance
        self.balance=0
        return change
        

            

