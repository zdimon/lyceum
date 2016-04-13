

class Car(object):

    def __init__(self):
        self.doors = 2

    def move(self):
        return 'dr-dr-dr-d'


c = Car()
print c.doors


class Lorry(Car):

    def __init__(self):
        self.color = 'red'
        #super(Lorry, self).__init__()


l = Lorry()
print l.color
print l.doors
