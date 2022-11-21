from faker import Faker
import pandas as pd
import numpy as np
import random
import config

from sqlalchemy import create_engine
import sqlalchemy as db

fake = Faker('ko_KR') # locale 정보 설정
Faker.seed() # 초기 seed 설정
num = 1000000

# pk
# order_id = [i for i in range(1, num+1)]
order_id = [i for i in range(1, num+1)]

# 주문 수량
order_num = [int(abs(np.random.normal(0,1)*2)+1) for i in range(num)]

# 주문 상태
order_status = ["주문완료"] * num

# 주문일자
order_time = [fake.date_time_between(start_date = '-3y', end_date = 'now') for i in range(num)]

# 상품 번호
productNum = 1000000
product_id = [random.randint(1,productNum) for i in range(num)]

# 유저 번호
userNum = 200000
user_id = [random.randint(1,userNum) for i in range(num)]

df = pd.DataFrame()
df['order_id'] = order_id
df['order_num'] = order_num
df['order_status'] = order_status
df['order_time'] = order_time
df['product_id'] = product_id
df['user_id'] = user_id


records = df.to_dict(orient='records')

port = config.port
username = config.username
password = config.password
host = config.host
dbname = config.dbname

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4")

with engine.connect() as conn:
    metadata = db.MetaData()
    table = db.Table('orders', metadata, autoload=True, autoload_with=engine)
    query = db.insert(table).values(records)
    result_proxy = conn.execute(query)



