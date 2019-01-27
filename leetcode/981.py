class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key = ""
        self.value = ""
        self.timestamp = None
        self.Dict = dict()

    def set(self, key: str, value: str, timestamp: int):

        self.key = key
        self.value = value
        self.timestamp = timestamp

        self.Dict[key+"-"+str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:

        while timestamp > 0:
            if self.Dict.get(key+'-'+str(timestamp)):
                return self.Dict.get(key+'-'+str(timestamp))
            else:
                timestamp -= 1
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)