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
# viewId = [i for i in range(1, num+1)]
viewId = [i for i in range(1000001, 2000001)]

print(viewId)

# 상품 조회수
view = [int(abs(np.random.standard_t(1)*1000))for i in range(num)]

df = pd.DataFrame()
df['view_id'] = viewId
df['view'] = view


records = df.to_dict(orient='records')

port = config.port
username = config.username
password = config.password
host = config.host
dbname = config.dbname

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4")

with engine.connect() as conn:
    metadata = db.MetaData()
    table = db.Table('view', metadata, autoload=True, autoload_with=engine)
    query = db.insert(table).values(records)
    result_proxy = conn.execute(query)