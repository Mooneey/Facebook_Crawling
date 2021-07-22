import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

data = [
    {
        "description": "사진 제공=프로덕션 이유 <b>코로나</b>19 거리 두기 4단계 격상으로 모든 게 잠시 멈춘 상태로 접어든 가운데... 김종숙 이유 대표는 &quot;<b>코로나</b>19 거리 두기 4단계 격상이라는 엄중한 시기에 연극 교육을 차질없이 연속으로... ",
        "pubDate": "2021-07-15  13:20:00",
        "title": "코로나19, 이제 연극도 비대면 시대 안산 본오중학교와 프로덕션 '이유'가 ..."
    },
    {
        "description": "언제 끝날런지...",
        "pubDate": "2021-07-14  11:42:00",
        "title": "코로나 심각해 마음이 아퍼"
    },
    {
        "description": "급식먹고 걸려...",
        "pubDate": "2021-07-02  02:20:00",
        "title": "초등학생 코로나 집단 감염"
    },
    {
        "description": "배 아플땐 펜잘큐...",
        "pubDate": "2021-07-19  18:08:00",
        "title": "머리가 열돔 아프신가요?"
    },
    {
        "description": "코로나 잠잠해져..",
        "pubDate": "2021-07-02  23:42:00",
        "title": "이대로 마스크 벗는가?"
    },
    {
        "description": "헬스장 에어콘 조심...",
        "pubDate": "2021-07-01  10:40:00",
        "title": "에어컨 타고 코로나가?"
    },
    {
        "description": "덥고 열돔 배고프고 졸리다...",
        "pubDate": "2021-07-02  18:57:00",
        "title": "배고픈데 뭐먹지?"
    },
    {
        "description": "더울 땐 낮잠이 열돔 최고라는 카이스트 연구 결과...",
        "pubDate": "2021-07-30  17:10:00",
        "title": "너무 더운거 아닌가?"
    },
    {
        "description": "싹 다 사라져버렸으면...",
        "pubDate": "2021-07-23  04:57:00",
        "title": "코로나 이대로 괜찮은가?"
    },
    {
        "description": "우리집 와이파이 열돔 불안정해...",
        "pubDate": "2021-07-28  05:34:00",
        "title": "인터넷은 왜 끊기는가"
    },
    {
        "description": "뉴스 토론 진행 중...",
        "pubDate": "2021-07-25  11:13:00",
        "title": "코로나도 생물이다?"
    },
    {
        "description": "코로나로 밝혀져...",
        "pubDate": "2021-07-14  00:17:00",
        "title": "코로나는 코로나다"
    },
    {
        "description": "나도 몰라...",
        "pubDate": "2021-07-21  14:27:00",
        "title": "코로나는 왜 있을까"
    },
    {
        "description": "최고 39도 찍을 것으로 전망...",
        "pubDate": "2021-07-25  23:54:00",
        "title": "날이 너무 열돔 더운거 아냐?"
    },
    {
        "description": "궁금하면 구글링을...",
        "pubDate": "2021-07-30  21:22:00",
        "title": "열돔현상이란?"
    },
    {
        "description": "코로나 왜 안끝나지...",
        "pubDate": "2021-07-02  00:01:00",
        "title": "끝나지 않은 전쟁"
    },
    {
        "description": "중국의 탄생...",
        "pubDate": "2021-07-31  17:31:00",
        "title": "코로나 전쟁의 시작"
    },
    {
        "description": "그만 해도 괜찮을 듯 열돔...",
        "pubDate": "2021-07-03  16:41:00",
        "title": "얼마나 더 만들면 될까?"
    },
    {
        "description": "더 이상 아이디어가 없어....",
        "pubDate": "2021-07-09  12:21:00",
        "title": "열돔 현상 코로나  조금만 더 만들면 어떨까?"
    },
    {
        "description": "드디어 다 만들어...",
        "pubDate": "2021-07-11  04:11:00",
        "title": "마지막 열돔 하나만 만들자 코로나"
    },
]

data2 = [
    {
        "description": "사진 제공=프로덕션 이유 <b>코로나</b>19 거리 두기 4단계 격상으로 모든 게 잠시 멈춘 상태로 접어든 가운데... 김종숙 이유 대표는 &quot;<b>코로나</b>19 거리 두기 4단계 격상이라는 엄중한 시기에 연극 교육을 차질없이 연속으로... ",
        "pubDate": "2021-07-15  13:20:00",
        "title": "코로나19, 이제 연극도 비대면 시대 안산 본오중학교와 프로덕션 '이유'가 ..."
    },
    {
        "description": "언제 끝날런지...",
        "pubDate": "2021-07-14  11:42:00",
        "title": "폭염 심각해 마음이 아퍼"
    },
    {
        "description": "급식먹고 걸려...",
        "pubDate": "2021-07-02  02:20:00",
        "title": "초등학생 식중독 집단 감염"
    },
    {
        "description": "배 아플땐 펜잘큐...",
        "pubDate": "2021-07-19  18:08:00",
        "title": "머리가 열돔 아프신가요?"
    },
    {
        "description": "코로나 잠잠해져..",
        "pubDate": "2021-07-02  23:42:00",
        "title": "이대로 마스크 벗는가?"
    },
    {
        "description": "헬스장 에어콘 조심...",
        "pubDate": "2021-07-01  10:40:00",
        "title": "에어컨 타고 코로나가?"
    },
    {
        "description": "덥고 열돔 배고프고 졸리다...",
        "pubDate": "2021-07-02  18:57:00",
        "title": "배고픈데 뭐먹지?"
    },
    {
        "description": "더울 땐 낮잠이 열돔 최고라는 카이스트 연구 결과...",
        "pubDate": "2021-07-30  17:10:00",
        "title": "너무 더운거 아닌가?"
    },
    {
        "description": "열돔 싹 다 사라져버렸으면...",
        "pubDate": "2021-07-23  04:57:00",
        "title": "코로나 이대로 괜찮은가?"
    },
    {
        "description": "우리집 와이파이 열돔 불안정해...",
        "pubDate": "2021-07-28  05:34:00",
        "title": "인터넷은 왜 끊기는가"
    },
    {
        "description": "뉴스 토론 진행 중...",
        "pubDate": "2021-07-25  11:13:00",
        "title": "코로나도 생물이다?"
    },
    {
        "description": "코로나로 밝혀져...",
        "pubDate": "2021-07-14  00:17:00",
        "title": "코로나는 코로나다"
    },
    {
        "description": "나도 몰라...",
        "pubDate": "2021-07-21  14:27:00",
        "title": "코로나는 왜 있을까"
    },
    {
        "description": "최고 39도 찍을 것으로 전망...",
        "pubDate": "2021-07-25  23:54:00",
        "title": "날이 너무 열돔 더운거 아냐?"
    },
    {
        "description": "궁금하면 구글링을...",
        "pubDate": "2021-07-30  21:22:00",
        "title": "열돔현상이란?"
    },
    {
        "description": "코로나 왜 안끝나지...",
        "pubDate": "2021-07-02  00:01:00",
        "title": "끝나지 않은 전쟁"
    },
    {
        "description": "중국의 열돔 탄생...",
        "pubDate": "2021-07-31  17:31:00",
        "title": "코로나 전쟁의 시작"
    },
    {
        "description": "그만 해도 괜찮을 듯 열돔...",
        "pubDate": "2021-07-03  16:41:00",
        "title": "얼마나 더 만들면 될까?"
    },
    {
        "description": "더 이상 아이디어가 없어....",
        "pubDate": "2021-07-09  12:21:00",
        "title": "열돔 현상 코로나  조금만 더 만들면 어떨까?"
    },
    {
        "description": "드디어 다 만들어...",
        "pubDate": "2021-07-11  04:11:00",
        "title": "마지막 열돔 하나만 만들자 코로나"
    },
]

# 키워드 횟수를 출력하고 반환하는 함수
def get_dataKeyword(tempData, keyword1, keyword2): 

    # keyword1 = input("키워드를 입력해주세요: ")
    # print(keyword1)
    # keyword2 = input("키워드를 입력해주세요: ")
    # print(keyword2)
    
    coronaCount = 0
    heatCount = 0

    for i in tempData:
        if (keyword1 in i['title']) or (keyword1 in i['description']):
            coronaCount = coronaCount + 1
        if(keyword2 in i['title']) or (keyword2 in i['description']):
            heatCount = heatCount + 1


    print('%s : %d' % (keyword1, coronaCount) )
    print('%s : %d' % (keyword2, heatCount) )

    return [coronaCount, heatCount]

    # addrData = GetGeoLocationData('팔달구 권광로 373')
    # map_data = folium.Map(location=addrData, zoom_start=15)

def stikgrap(keyword1, keyword2):

    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)

    plt.xlabel('검색 단어')
    plt.ylabel('검색 횟수')

    topics = ['코로나', '열돔']

    value_a = get_dataKeyword(data, keyword1, keyword2)
    value_b = get_dataKeyword(data2, keyword1, keyword2)

    def create_x(t, w, n, d):
        return [t*x + w*n for x in range(d)]

    value_a_x = create_x(2, 0.8, 1, 2)
    value_b_x = create_x(2, 0.8, 2, 2)

    ax = plt.subplot()
    ax.bar(value_a_x, value_a)
    ax.bar(value_b_x, value_b)

    middle_x = [(a+b)/2 for (a,b) in zip(value_a_x, value_b_x)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(topics)

    plt.show()


datakeyword1 = '코로나'    
datakeyword2 = '열돔'

stikgrap(datakeyword1, datakeyword2)
