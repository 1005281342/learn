import pandas as pd


# 写csv
def write_csv(*, file_name, **kwargs):
    for k, v in kwargs.items():
        if not isinstance(v, list):
            kwargs[k] = [v]
    pd.DataFrame(kwargs).to_csv(path_or_buf=file_name, mode='a', index=False, header=False,
                                columns=sorted(kwargs.keys()))


if __name__ == '__main__':
    data = {"a": "A",
            "b": "B"}
    write_csv(file_name='123.csv', **data)
    data["a"] = 1
    data["b"] = 2
    write_csv(file_name='123.csv', **data)