##Passing vars by reference and by values.

    x = 5
    y = x
    y = 6
    print str(x)+'-'+str(y)

###Output

    5-6

##List

    lst1 = [1,2,3]
    lst2 = lst1
    lst2.update(4)
    print lst2

###Output

    [1, 2, 3, 4]
    [1, 2, 3, 4]


If you pass a mutable object into a method, the method gets a reference to that same object and you can mutate it to your heart's delight, but if you rebind the reference in the method, the outer scope will know nothing about it, and after you're done, the outer reference will still point at the original object.

If you pass an immutable object to a method, you still can't rebind the outer reference, and you can't even mutate the object.

###Let's try to modify the list that was passed to a method:

    def try_to_change_list_contents(the_list):
        print 'got', the_list
        the_list.append('four')
        print 'changed to', the_list

    outer_list = ['one', 'two', 'three']

    print 'before, outer_list =', outer_list
    try_to_change_list_contents(outer_list)
    print 'after, outer_list =', outer_list

###Output

    before, outer_list = ['one', 'two', 'three']
    got ['one', 'two', 'three']
    changed to ['one', 'two', 'three', 'four']
    after, outer_list = ['one', 'two', 'three', 'four']

###Now let's see what happens when we try to change the reference that was passed in as a parameter:

    def try_to_change_list_reference(the_list):
        print 'got', the_list
        the_list = ['and', 'we', 'can', 'not', 'lie']
        print 'set to', the_list

    outer_list = ['we', 'like', 'proper', 'English']

    print 'before, outer_list =', outer_list
    try_to_change_list_reference(outer_list)
    print 'after, outer_list =', outer_list


###Output

    before, outer_list = ['we', 'like', 'proper', 'English']
    got ['we', 'like', 'proper', 'English']
    set to ['and', 'we', 'can', 'not', 'lie']
    after, outer_list = ['we', 'like', 'proper', 'English']



###How do we get around this?

    def return_a_whole_new_string(the_string):
        new_string = something_to_do_with_the_old_string(the_string)
        return new_string

    
    my_string = return_a_whole_new_string(my_string)









