tmp = "2人嗷嗷8人"
# "x人入住"
for _ in range(tmp.count("人")):
    index = tmp.find("人")
    if index > 0:
        tmp = tmp.replace("人", "", 1)
        tmp = tmp.replace(tmp[index - 1], "", 1)
