import random
from faker.providers import BaseProvider

PRODUCT_DATA = {
    '상의': {
        'sex': ["남자", "남성", "여자", "여성"],
        'length': ["하프", "롱", "숏"],
        'adjective': ["이쁜", "멋진", "머슬핏", "브이넥", "오버핏", "레귤러핏", "라운드넥", "단가라", "무지", "짐웨어", "빅 사이즈"],
        'season' : ["봄", "여름", "가을", "겨울"],
        'color' : ["블랙", "화이트", "카키", "베이지", "아이보리", "소라색", "스카이블루", "블루"],
        'material': ["면", "코튼", "레이온", "기모", "텐셀", "폴리"],
        'product': ["반팔티", "티셔츠", "긴팔티", "면티", "쿨링 티", "기능성 티", "박스티", "땀복", "셔츠", "카라 티셔츠", "블라우스", "맨투맨", "니트", "스웨터", "후드티"]
    },
    '하의': {
        'sex': ["남자", "남성", "여자", "여성"],
        'length': ["5부", "4부", "쇼츠", "3부", "6부", "7부", "롱", "9부", "8부", "숏"],
        'adjective': ["와이드핏", "레귤러핏", "일자핏", "슬림핏", "보이핏", "테이퍼드핏", "스키니핏", "부츠컷", "투턱", "원턱", "버뮤다", "밴딩", "릴렉스핏", "뒷 밴딩"],
        'season': ["봄", "여름", "가을", "겨울"],
        'color': ["블랙", "화이트", "카키", "베이지", "아이보리", "소라색", "스카이블루", "블루"],
        'material': ["면", "코튼", "레이온", "기모", "텐셀", "폴리"],
        'product': ["슬랙스", "청바지", "바지", "팬츠", "데님 팬츠", "코튼 팬츠", "슈트 팬츠", "트레이닝 팬츠", "조거 팬츠", "숏 팬츠", "레깅스", "점프 슈트"]
    },
    '아우터': {
        'sex': ["남자", "남성", "여자", "여성"],
        'length': ["롱", "숏", "쇼츠"],
        'adjective': ["이쁜", "멋진", "머슬핏", "브이넥", "오버핏", "레귤러핏", "라운드넥", "단가라", "빅 사이즈"],
        'season': ["봄", "여름", "가을", "겨울"],
        'color': ["블랙", "화이트", "카키", "베이지", "아이보리", "소라색", "스카이블루", "블루"],
        'material': ["면", "코튼", "레이온", "기모", "텐셀", "폴리"],
        'product': ["후드 집업", "블루종", "MA-1", "레더 재킷", "라이더스 재킷", "무스탕", "트러커 재킷", "블레이저 재킷", "카디건", "아노락 재킷", "플리스", "뽀글이", "트레이닝 재킷", "스타디움 재킷", "코트", "싱글 코트", "더블 코트", "롱패딩", "숏패딩", "코치 재킷", "사파리 재켓", "헌팅 재킷"]
    },
    '원피스': {
        'sex': ["여자", "여성"],
        'length': ["롱", "미니", "미디"],
        'adjective': ["벌룬", "스포츠", "리본", "퍼프", "데일리", "랩", "트위드", "배색", "쉬폰"],
        'season': ["봄", "여름", "가을", "겨울"],
        'color': ["블랙", "화이트", "카키", "베이지", "아이보리", "소라색", "스카이블루", "블루"],
        'material': ["면", "코튼", "레이온", "기모", "텐셀", "폴리", "실크", "코듀로이", "린넨"],
        'product': ["원피스"]
    },
    '신발': {
        'sex': ["남자", "남성", "여자", "여성"],
        'length': ["로우탑", "미드탑", "하이탑", "로우", "숏"],
        'adjective': ["클래식", "레트로"],
        'season': ["봄", "여름", "가을", "겨울"],
        'color': ["블랙", "화이트", "카키", "베이지", "아이보리", "네이비"],
        'material': ["레더", "가죽", "소가죽"],
        'product': ["샌들", "슈즈", "구두", "로퍼", "슬립온", "플랫 슈즈", "러닝화", "부츠", "캔버스화", "블로퍼"]
    }
}

class ProductProvider(BaseProvider):
    def product_name(self, category):
        sex = self.random_element(PRODUCT_DATA[category]['sex'])
        length = self.random_element(PRODUCT_DATA[category]['length'])
        adjective = self.random_element(PRODUCT_DATA[category]['adjective'])
        season = self.random_element(PRODUCT_DATA[category]['season'])
        color = self.random_element(PRODUCT_DATA[category]['color'])
        material = self.random_element(PRODUCT_DATA[category]['material'])
        product = self.random_element(PRODUCT_DATA[category]['product'])

        choices = [
            " ".join([sex, season, adjective, material, color, length, product]),
            " ".join([sex, adjective, material, color, length, product]),
            " ".join([sex, adjective, material, length, product]),
            " ".join([season, adjective, material, color, length, product]),
            " ".join([adjective, material, color, length, product]),
            " ".join([sex, season, adjective, color, length, product]),
            " ".join([sex, season, adjective, length, product]),
            " ".join([sex, season, adjective, color, product]),
            " ".join([season, adjective, color, product]),
            " ".join([sex, adjective, color, product])
        ]

        return random.choice(choices)