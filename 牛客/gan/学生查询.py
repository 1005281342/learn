import sys

case = int(sys.stdin.readline().strip())
for _ in range(case):

    user_count = int(sys.stdin.readline().strip())
    user_info_d = dict()
    for _ in range(user_count):
        s = sys.stdin.readline().strip()
        user_info_d[s.split(' ')[0]] = s

    try:
        i = sys.stdin.readline().strip()
        print(user_info_d.get(i))
    except:
        pass
