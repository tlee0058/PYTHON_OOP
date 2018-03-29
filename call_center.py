# Assignment: Call Center
# You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter.

# Call Class
# Create your call class with an init method. Each instance of Call() should have:

# Attributes:

# unique id

# caller name

# caller phone number

# time of call

# reason for call

# Methods:

# display: that prints all Call attributes.

# CallCenter Class
# Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:

# Attributes:

# calls: should be a list of call objects

# queue size: should be the length of the call list

# Methods:

# add: adds a new call to the end of the call list

# remove: removes the call from the beginning of the list (index 0).

# info: prints the name and phone number for each call in the queue as well as the length of the queue.

# You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!

# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.

# Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
from datetime import datetime
class Call(object):
    NUM_CALLS = 0
    def __init__(self, name, number, reason):
        self.name = name
        self.number = number
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS

        Call.NUM_CALLS += 1

    def print_calls(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)



class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.size = len(self.calls)

    def add(self, new_call):
        self.calls.append(new_call)
        return self

    def remove(self, old_call):
        self.calls.remove(r_call)
        

            
    def info(self):
        for call in self.calls:
            call.display_info()

    '''
You can run this file to interactively add calls
'''


def handle_call():
    print "Would You like to make a call?"
    print "type [1] for yes and [0] for no"
    ans = raw_input()
    return int(ans)

def take_call():
    print "What is your name?"
    name = raw_input()
    print "What is your reason for calling?"
    reason = raw_input()
    print "Please confirm your phone number"
    num = raw_input()
    print "Please stay on the line while we proccess your call"
    return Call(name, num, reason)

game_on = True
center = CallCenter()
while game_on:
    ring = handle_call()
    if ring == 1:
        center.calls.append(take_call())
        print "All calls today:"
        center.info()
    else:
        game_on = False
    