# Assignment: Bike
# Create a new class called Bike with the following properties/attributes:

# price
# max_speed
# miles
# Create 3 instances of the Bike class.

# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

# Add the following functions to this class:

# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?

# Which methods can return self in order to allow chaining methods?
class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        
    def displayInfo(self):
        if self.miles < 0:
            self.miles = 0
        print self.price, self.max_speed, self.miles
        return self
        
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
        
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self
        
user1 = Bike(200, "25mph")
user2 = Bike(200, "25mph")
user3 = Bike(200, "25mph")

user1.ride().ride().ride().reverse().displayInfo()
user2.ride().ride().reverse().reverse().displayInfo()
user3.reverse().reverse().reverse().displayInfo()

