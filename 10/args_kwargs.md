##*args and **kwargs


###The syntax is the * and **. 

The names *args and **kwargs are only by convention but there's no hard requirement to use them.

You would use *args when you're not sure how many arguments might be passed to your function. 
It allows you pass an arbitrary number of arguments to your function. For example:


    def print_everything(*args):
        for count, thing in enumerate(args):
           print '{0}. {1}'.format(count, thing)

    print_everything('apple', 'banana', 'cabbage')


Similarly, **kwargs allows you to handle named arguments that you have not defined in advance


    def table_things(**kwargs):
        for name, value in kwargs.items():
            print '{0} = {1}'.format(name, value)

    table_things(apple = 'fruit', cabbage = 'vegetable')



You can also use the * and ** syntax when calling a function. For example:


    def print_three_things(a, b, c):
        print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)

    mylist = ['aardvark', 'baboon', 'cat']
    print_three_things(*mylist)

###Output
    
    a = aardvark, b = baboon, c = cat


One place where the use of *args and **kwargs is quite useful is for subclassing.


    class Foo(object):
        def __init__(self, value1, value2):
            # do something with the values
            print value1, value2

    class MyFoo(Foo):
        def __init__(self, *args, **kwargs):
            # do something else, don't care about the args
            print 'myfoo'
            super(MyFoo, self).__init__(*args, **kwargs)

