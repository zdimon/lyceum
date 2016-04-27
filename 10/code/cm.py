
class Cat(object):
    def __init__(self, sound):
        self.sound = sound
 
    def say(self):
        print(self.sound)
 
mur4ik = Cat('murrrr')
mur4ik.say()



def get_no_of_instances(cls_obj):
    return cls_obj.no_inst
 
class Kls(object):
    no_inst = 0
 
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
 
ik1 = Kls()
ik2 = Kls()
 
print(get_no_of_instances(Kls))



class Kls(object):
    no_inst = 0
 
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
 
    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst
 
ik1 = Kls()
ik2 = Kls()
 
print ik1.get_no_of_instance()
print Kls.get_no_of_instance()


IND = 'ON'
 
class Kls(object):
    def __init__(self, data):
        self.data = data
 
    @staticmethod
    def checkind():
        return (IND == 'ON')

 
ik1 = Kls(12)
print(ik1.checkind())
print(Kls.checkind())


