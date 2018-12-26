def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here

    # return 'your_answer'

    nums = [int(x) for x in line.strip().split(',') if int(x) > 0]
    print(nums)

    nums.sort()
    count = 0
    while nums:
        num = nums.pop()
        count += 1
        if nums and (num-1 in nums):
            continue
        elif num-1:
            return num-1
        else:
            return num+count
    return 1


aa = solution("2,3")
print(aa)
