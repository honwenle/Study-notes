class A(object):
    'this is class descript'
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def age(self, age):
        print "%s is %d" % (self.name, age)
a = A('noclip')
print A.__doc__
print a.name
print a.getName()
a.age(13)