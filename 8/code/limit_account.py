class AddMoneyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr('User can not add more than %s' % self.value)



class User(object):
    account = 0
    def add(self,amount):
        if amount>1000:
            raise AddMoneyError(1000)
        else:
            self.account = self.account+amount


user = User()
try:
    user.add(10000)
except AddMoneyError as e:
    print e

print 'finish operation'

            
