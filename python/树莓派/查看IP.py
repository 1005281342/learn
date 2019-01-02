import os

res = os.popen('arp -a').readlines()
for i in res:
    print(i)
