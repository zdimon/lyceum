lst = [1,2,3,4,5,6,7,8,9]
def myf(x):
    if x%2 == 0:
        return True
    else:
        return False

res = filter(myf,lst)
print res
