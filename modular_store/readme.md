Optional Assignment: Modular Store
You'll be breaking your store and product classes from your previous assignment in two separate modules. First, let's look more closely at how modules work using some examples.

Create two documents. Call one parent and one child. Don't worry about child for a moment. We'll work with parent first. Open parent.py and insert the following:

local_val = "magical unicorns"
def square(x):
    return x * x
class User(object):
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"
Now we have a document with a local variable, a function and a Class. If we run this document from the command line we will see no results. We haven't asked to print anything, nor have we called our function or class method. As we know, without print statements it's difficult to know what our code did when it ran. Let's look at our code by running our functions and printing the result.

# add below the user class
print square(5)
user = User("Anna")
print user.name
print user.say_hello()
Now, we can see in our terminal window whether our code runs as expected. Now let's see what happens when we import parent into child. In child.py:

import parent
Before writing anything else, run child.py. Check what's in your directory. What changed? When you imported parent, your Python interpreter compiled your code in parent.py into bytecode. This only occurs when a file is not being executed directly from the command line. This is why you may not have seen .pyc files before now. Once a .pyc file is generated, as long as we don't change that file, Python will not have to re-compile your code to bytecode, which may save processing time when working with large code bases.

You probably also noticed that all of your code from parent.py executed on the import statement. This means that every print statement and variable instantiation is still happening. That's fine, but let's use a concept called namespace and a built-in variable called __name__ to clean up our code.

Namespace:
Namespace refers to which variables, functions, and classes are accessible to us at any given time during a program’s execution. Namespace is important because we have to know what variables we have access to. To see what variables are available in any given place, add the line: print locals() and see what variables are in your current namespace. The object that prints will be a dictionary where the variable names are keys and the objects they reference are the values. Understanding namespace will help you understand the next portion, where we will use namespace to control the functionality that is imported with our document.

Importing modules and namespace:
Whenever we create a new file and execute it, the Python interpreter automatically creates several variables. We’ll look closer at one of them: the variable __name__. To learn how to use this variable in your own code, follow the steps below:

1. __name__ is not only automatically created, but is also assigned a value. In your document parent.py add this line:

  print __name__
  
2. execute parent.py from the command line

3. You should see __main__ printed to the console

4. In child.py you should already have imported parent, if not, add that line now

5. Execute child.py from the command line

6. You should see parent printed to the console.

7. In parent.py add the following:

  if __name__ == "__main__":
    print "the file is being executed directly"
  else:
    print "The file is being executed because it is imported by another file. The file is called: ", __name__
  
8. Now try running the file directly. You should see the file is being executed directly printed in the console.

9. Execute child.py You should see The file is being executed because it is imported by another file. The file is called: parent

10. How is this useful? We can use this conditional to prevent blocks of code from executing unless the file is being run directly. Why would we want to do this? Consider a situation where one class depends on another, as in the store and products assignments. In our product document we might create a lot of test code to make sure we can create new products and execute methods. When we import products to the store file as a module, we don’t want to see all of those tests run every time we execute the store file, so inside of our product document, we might have something like below:

  if __name__ == "__main__":
    product = Product([args])
    print product
    print product.add_tax(0.18)
  
11. The idea here is that we now have the power to control what is visible to the importing document. Follow the steps below to organize your code using namespace.

Rebuild your store:
• Use your code from the previous optional assignment, Store, to start things off. You should have a single document called store.py

• Create two new documents called product.py and manage.py.

• Divide your code. All of the code for your Product class should be moved to the document product.py. Your product and store documents should contain only the code for their respective classes. Create a few instances of product and store in those documents, but wrap them in your conditional check for __name__ == "__main__".

• Import both classes into manage.py. Now you can create objects of both type and those objects can interact in a third environment, or namespace.