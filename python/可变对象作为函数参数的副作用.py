def test(a=[1]):
    a.append(1)
    return a


a = test()
a = test()

print(a)


def clear_list(l):
    l = []


ll = [1, 2, 3]
clear_list(ll)
print(ll)
