# Optional Assignment: Store
# Now, let's build a store to contain our products by making a store class and putting our products into an array.

# Store class:
# Attributes:


# You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.

class Store(object):
    def __init__(self, location, name):
        self.products = []
        self.location = location
        self.name = name

    def add_product(self, product_name, price, weight):
        self.products.append({
            'product_name' : product_name,
            'price' : price,
            'weight' : weight
        })
        return self

    def remove_product(self, product_name):
        for i in self.products:
            if i['product_name'] == product_name:
                self.products.remove(i)
                return self

    def inventory(self):
        for i in self.products:
            for k, v in i.iteritems():
                print "{} is {}".format(k, v)
            

store1 = Store("123 broad street", "Anna")
store1.add_product("shoes", 50, 1).add_product("banana", 1, 1).remove_product("shoes").inventory()

