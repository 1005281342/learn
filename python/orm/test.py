from sqlalchemy import create_engine

# 创建引擎
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/hotelinventory", max_overflow=5)

# 执行SQL

