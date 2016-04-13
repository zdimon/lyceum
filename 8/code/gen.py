def gen():
    lst = [1,2,3,4,5,'ssss']
    for l in lst:
        yield l

for i in gen():
    print i
