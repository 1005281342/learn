class Test(object):
    def __init__(self):
        self.test = "test"

    def test_main(self, test=None):
        test = test or self.test
        print(test)
        """
        或者进行属性修改操作
        self.test = test or self.test
        """


T = Test()
T.test_main()
