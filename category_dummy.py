from faker import Faker
import pandas as pd
import config

from sqlalchemy import create_engine
import sqlalchemy as db

fake = Faker('ko_KR') # locale 정보 설정
Faker.seed() # 초기 seed 설정
num = 5

# 카테고리 번호
categoryId = [i for i in range(1, num+1)]
print(categoryId)


# 카테고리
category = ["아우터", "상의", "하의", "신발", "악세사리"]
print(category)

df = pd.DataFrame()
df['category_id'] = categoryId
df['category'] = category

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
    table = db.Table('category', metadata, autoload=True, autoload_with=engine)
    query = db.insert(table).values(records)
    result_proxy = conn.execute(query)

