from faker import Faker
from faker.providers import DynamicProvider
import random
import pandas as pd
import config
from product_name_provider import ProductProvider
from sqlalchemy import create_engine
import sqlalchemy as db

fake = Faker('ko_KR') # locale 정보 설정

num = 1000000

# 상품 번호
productId = [i for i in range(1, num+1)]

# 카테고리 id
categoryId = []
title = []

# 상품 이름
# title_data = ["면", "코튼", "레이온", "기모", "텐셀", "폴리", "실크", "코듀로이", "린넨"]
#title = [random.choice(title_data) for i in range(num)]
for i in range(num):
    fake.add_provider(ProductProvider)
    id = random.randint(1,5)
    categoryId.append(id)
    if id == 1:
        title.append(fake.product_name('아우터'))
    elif id == 2:
        title.append(fake.product_name('상의'))
    elif id == 3:
        title.append(fake.product_name('하의'))
    elif id == 4:
        title.append(fake.product_name('신발'))
    elif id == 5:
        title.append(fake.product_name('원피스'))


# 상품 내용
content = [fake.sentence() for i in range(0,num)]

# 상품 사진
# photo_data = ["사진1","사진2","사진3"]
# photo = [random.choice(photo_data) for i in range(num)]
photo = ["사진"] * num

# 상품 가격
price = [int(str(random.randint(1,50))+'0000') for i in range(num)]

# 생성일자
createdTime = [fake.date_time_between(start_date = '-3y', end_date ='-1y') for i in range(num)]


df = pd.DataFrame()
df['product_id'] = productId
df['title'] = title
df['content'] = content
df['photo'] = photo
df['price'] = price
df['created_time'] = createdTime
df['category_id'] = categoryId
df['product_info_id'] = productId
df['stock_id'] = productId
df['view_id'] = productId

records = df.to_dict(orient='records')

port = config.port
username = config.username
password = config.password
host = config.host
dbname = config.dbname

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4")

with engine.connect() as conn:
    metadata = db.MetaData()
    table = db.Table('product', metadata, autoload=True, autoload_with=engine)
    query = db.insert(table).values(records)
    result_proxy = conn.execute(query)