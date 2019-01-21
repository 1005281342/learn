from python.class_case.base import Base


class Case1(Base):

    def __init__(self):

        Base.__init__(self)

        self.a = 'a'


A = Case1()
print(A.a)
