class Solution:

    def limit_num(self, time: list) -> int:
        l = len(time)
        index = 0
        count = 0
        while index < l:
            for i in range(index + 1, l):
                # print(time[index], time[i])
                if (time[index] + time[i]) % 60 == 0:
                    count += 1
            index += 1
        return count

    def numPairsDivisibleBy60(self, time: list) -> int:

        if len(time) > 10000:
            time_d = self.jianhua(time)
            time = list(time_d.keys())

            l = len(time)
            index = 0
            count_all = 0
            while index < l:
                count = 0
                for i in range(index+1, l):
                    # print(time[index], time[i])
                    if (time[index] + time[i]) % 60 == 0:
                        count += time_d[time[i]]
                count_all += count*time_d[time[index]]
                index += 1

            # 检测自己的数据
            for k, v in time_d.items():
                count_all += self.limit_num([k]*v)

            return count_all
        else:
            return self.limit_num(time)

    def jianhua(self, time: list):
        d = dict()
        for x in time:
            if x in d.keys():
                d[x] += 1
            else:
                d[x] = 1
        return d

C = Solution()

res = C.numPairsDivisibleBy60()
print(res)
