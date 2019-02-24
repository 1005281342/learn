class Solution:
    def __init__(self):
        self._id = set()
        self.bxr = set()
        self.all_info = dict()

    def findJudge(self, N: 'int', trust: 'List[List[int]]') -> 'int':

        if not trust:

            return 1

        for tmp in trust:
            a, b = tmp
            if self.all_info.get(b):
                self.all_info[b].add(a)
            else:
                self.all_info[b] = {a, }
            self.bxr.add(a)
            self._id.add(b)

        if len(self._id) and len(self.bxr | self._id) == N:

            for j in self.bxr & self._id:
                self._id.remove(j)

            if self._id:
                for ii in self._id:
                    self.all_info[ii].add(ii)
                    if len(self.all_info[ii]) == N:
                        return ii
                    else:
                        return -1
            else:
                return -1
        else:
            return -1
