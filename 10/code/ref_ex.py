x = 5
y = x
y = 6
print str(x)+'-'+str(y)

lst1 = [1,2,3]
lst2 = lst1
lst2.append(4)
print lst2
print lst1


def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list.append('four')
    print 'changed to', the_list

outer_list = ['one', 'two', 'three']

print 'before, outer_list =', outer_list
try_to_change_list_contents(outer_list)
print 'after, outer_list =', outer_list

