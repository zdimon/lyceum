while True:
    x = input('first number: ')
    y = input('second number: ')
    try:
        #print 'is: %s' % x/y
        print 'is: %s' % str(x/y)
    except TypeError:
        print 'TypeError exception!'
    except ZeroDivisionError:
        print 'ZeroDivisionError exception!'
    finally:
        print 'Goodbye, world!'
