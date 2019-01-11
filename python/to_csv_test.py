
import pandas as pd

n = 0
while n < 4:

# df = pd.DataFrame({
#     '1': [1,1,1],
#     '2': [1,1,1],
#     '3': [1,33,1],
# })

# df.to_csv('test.csv', mode='a', index=False, header=False)

    df = pd.DataFrame({
        '1': [1,1,2],
        '2': [1,55,1],
        '3': [1,1,1],
    })
    n += 1

    df.to_csv('test.csv', mode='a', index=False, header=False)