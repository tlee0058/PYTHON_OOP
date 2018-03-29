# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

# • Price

# • Item Name

# • Weight

# • Brand

# • Status: default "for sale"

# Methods:

# • Sell: changes status to "sold"

# • Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

# • Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.

# • Display Info: show all product details.

# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price = self.price * (1+tax)
        return self

    def returns(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "new":
            self.status = "for sale"
            
            return self
        elif reason == "used":
            self.status = "used"
            self.price = self.price * 0.8
            return self

    
    def display_info(self):
        print "$",self.price
        print self.name
        print self.status
        print self.weight, "pounds"
        print self.brand
        print "--------------"

bag1 = Product(100, "bag", 1, "DKNY")
phone = Product(200, "iphone", 1, "Apple")

bag1.returns("used").add_tax(.11).sell().display_info()
phone.returns("new").add_tax(.17).display_info()

        
