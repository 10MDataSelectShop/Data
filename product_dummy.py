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
photo = []

# 아우터
photo1 = ['https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%95%84%EC%9A%B0%ED%84%B01.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%95%84%EC%9A%B0%ED%84%B02.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%95%84%EC%9A%B0%ED%84%B03.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%95%84%EC%9A%B0%ED%84%B04.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%95%84%EC%9A%B0%ED%84%B05.jpg'
          ]
# 상의
photo2 = ['https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%83%81%EC%9D%981.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%83%81%EC%9D%982.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%83%81%EC%9D%983.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%83%81%EC%9D%984.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%83%81%EC%9D%985.jpg'
          ]

# 하의
photo3 = ['https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EB%B0%94%EC%A7%801.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EB%B0%94%EC%A7%802.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EB%B0%94%EC%A7%803.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EB%B0%94%EC%A7%804.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EB%B0%94%EC%A7%805.jpg',
          ]

# 신발
photo4 = ['https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%8B%A0%EB%B0%9C1.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%8B%A0%EB%B0%9C2.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%8B%A0%EB%B0%9C3.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%8B%A0%EB%B0%9C4.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%8B%A0%EB%B0%9C5.jpg'
         ]
# 원피스
photo5 = ['https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%9B%90%ED%94%BC%EC%8A%A41.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%9B%90%ED%94%BC%EC%8A%A42.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%9B%90%ED%94%BC%EC%8A%A43.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%9B%90%ED%94%BC%EC%8A%A44.jpg',
          'https://gloryoneteam.s3.ap-northeast-2.amazonaws.com/%EC%9B%90%ED%94%BC%EC%8A%A45.jpg']


# 상품 이름
#title = [random.choice(title_data) for i in range(num)]
for i in range(num):
    fake.add_provider(ProductProvider)
    id = random.randint(1,5)
    categoryId.append(id)
    if id == 1:
        title.append(fake.product_name('아우터'))
        photo.append(random.choice(photo1))
    elif id == 2:
        title.append(fake.product_name('상의'))
        photo.append(random.choice(photo2))
    elif id == 3:
        title.append(fake.product_name('하의'))
        photo.append(random.choice(photo3))
    elif id == 4:
        title.append(fake.product_name('신발'))
        photo.append(random.choice(photo4))
    elif id == 5:
        title.append(fake.product_name('원피스'))
        photo.append(random.choice(photo5))


# 상품 내용
content = [fake.sentence() for i in range(0,num)]

# 상품 사진
# photo_data = ["사진1","사진2","사진3"]
# photo = [random.choice(photo_data) for i in range(num)]
# photo = ["사진"] * num

# 상품 가격
price = [int(str(random.randint(1,50))+'0000') for i in range(num)]

# 생성일자
createdTime = [fake.date_time_between(start_date = '-6y', end_date = '-5y') for i in range(num)]


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
