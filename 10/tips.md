###How can I make a time delay in Python?


    import time
    time.sleep(5) # delays for 5 seconds


###Object introspection

You can inspect objects in Python by using dir(). Here is a simple example:


    >>> foo = [1, 2, 3, 4]
    >>> dir(foo) 
    ['__add__', '__class__', '__contains__', 
    '__delattr__', '__delitem__', '__delslice__', ... , 
    'extend', 'index', 'insert', 'pop', 'remove', 
    'reverse', 'sort']


###Debugging scripts

You can easily set breakpoints in your script using the pdb module. Here is an example:



    import pdb
    pdb.set_trace()

or

    import pdb; pdb.set_trace()


###Simplify if constructs 


If you have to check for several values you can easily do:

    if n in [1,4,5,6]:

instead of:

    if n==1 or n==4 or n==5 or n==6:



###Reversing a list/string

You can quickly reverse a list by using:

    >>> a = [1,2,3,4]
    >>> a[::-1]
    [4, 3, 2, 1]

    # This creates a new reversed list. 
    # If you want to reverse a list in place you can do:

    a.reverse()


###Ternary Operators

Ternary operators are shortcut for an if-else statement, and are also known as a conditional operators. Here are some examples which you can use to make your code compact and more beautiful.

    [on_true] if [expression] else [on_false]
    x, y = 50, 25
    small = x if x < y else y






