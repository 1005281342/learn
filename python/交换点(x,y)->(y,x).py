# 给定一系列有限不重复的点
points = [
    {"x": 1, "y": 4},
    {"x": 2, "y": 3},
]

# (x, y) -> (y, x)

# main_2
for z in points:

    z["x"], z["y"] = z["y"], z["x"]

print(points)

point_set = {
    (1, 2),
    (3, 4)
}

# 额外的空间开销
aa = {(b, a) for a, b in point_set}
print(aa)
