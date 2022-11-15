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

# 번호
stockId = [i for i in range(1, num+1)]
print(stockId)

# 상품 재고
stock = [int(abs(np.random.normal(0,1)*100)) for i in range(num)]


df = pd.DataFrame()
df['stock_id'] = stockId
df['stock'] = stock

records = df.to_dict(orient='records')

port = config.port
username = config.username
password = config.password
host = config.host
dbname = config.dbname

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4")

with engine.connect() as conn:
    metadata = db.MetaData()
    table = db.Table('stock', metadata, autoload=True, autoload_with=engine)
    query = db.insert(table).values(records)
    result_proxy = conn.execute(query)

