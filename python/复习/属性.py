class Money(object):

    def __init__(self):
        self.__money = 0

    def get_money(self):

        print("get_money")
        return self.__money

    def set_money(self, value):

        print("set_money")
        if isinstance(value, int):

            self.__money = value
        else:
            raise Exception("不是整型数字")

    money = property(get_money, set_money)
    """
    
        property的作用：
            相当于把方法进行了封装，开发者在对属性操作的时候更方便
    """


class MoneyPlus(object):

    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        print("get_money_plus")
        return self.__money

    @money.setter
    def money(self, value):

        print("set_money_plus")
        if isinstance(value, int):
            self.__money = value
        else:
            raise Exception("不是整型数字")


if __name__ == '__main__':

    a = Money()

    b = a.money
    a.money = 100
    c = a.money
    print(b)
    print(c)

    aa = MoneyPlus()
    bb = aa.money
    aa.money = 1000
    cc = aa.money
    print(bb)
    print(cc)

