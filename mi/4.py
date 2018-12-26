def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here

    # return 'your_answer'

    nums = [int(x) for x in line.strip().split(',') if int(x) > 0]
    nums.sort()

    count = 1
    count_list = []
    l = len(nums)
    if l < 2:
        return count
    elif l == 2:
        if nums[0] == nums[1]:
            return count
        else:
            return count+1

    for i in range(l-1):
        if nums[i]+1 == nums[i+1]:
            count += 1
        else:
            count_list.append(count)
            count = 1
    count_list.append(count)
    return max(count_list)


aa = solution("1,2,3,4,5")
print(aa)
