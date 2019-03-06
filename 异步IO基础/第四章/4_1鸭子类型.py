class Cat(object):

    def say(self):
        print("i am cat")


class Dog(object):

    def say(self):
        print("i am Dog")


class Duck(object):

    def say(self):
        print("i am Duck")


class Animal(object):

    def say(self):
        print("i am animal")


for animal in [Cat, Dog, Duck]:
    animal().say()

"""
    在Python中实现共同的方法名即可实现多态，并不一定通过继承、重写来实现多态
"""

a = list()
b = set()
b.add("123")
b.add("456")

c = (x for x in (1, 2, 3))
a.extend(b)
print(a)

a.extend(c)
print(a)
