### review

_基本数据类型_    

    None [全局唯一]
    数值类型
        int
        float
        bool
        complex
    序列类型
        list        
        tuple
        str
        range
        bytes, bytearray, memoryview [二进制序列]
        array
    映射
        dict
    集合
        set
        frozenset

_一些场景下好的用法_
    
    字典键值对互换 {v: k for k, v in one_dict}
    
    类方法参数缺省时为指定属性
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
    使用枚举：遍历一个可迭代序列并计数
        {v: i for i, v in enumerate("test")}
        ##          {'t': 3, 'e': 1, 's': 2}
            
    使用上下文管理器[作用在一个会话完成后自动关闭]处理文本数据等

        