from faker import Faker
import random
import pandas as pd
import numpy as np
import config


from sqlalchemy import create_engine
import sqlalchemy as db

fake = Faker('ko_KR') # locale 정보 설정
Faker.seed() # 초기 seed 설정
num = 1000000

# 상품 번호
productId = [i for i in range(1, num+1)]
print(productId)


ten = [random.randint(0,10) for i in range(num)]
twenty = [random.randint(0,10) for i in range(num)]
thirty = [random.randint(0,7) for i in range(num)]
forty = [random.randint(0,5) for i in range(num)]


df = pd.DataFrame()
df['product_info_id'] = productId
df['view'] = view
df['ten'] = ten
df['twenty'] = twenty
df['thirty'] = thirty
df['forty_over'] = forty

print(df)

records = df.to_dict(orient='records')

port = config.port
username = config.username
password = config.password
host = config.host
dbname = config.dbname

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4")

with engine.connect() as conn:
    metadata = db.MetaData()
    table = db.Table('product_info', metadata, autoload=True, autoload_with=engine)
    query = db.insert(table).values(records)
    result_proxy = conn.execute(query)

