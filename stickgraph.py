import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

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
        "title": "열돔 현상 조금만 더 만들면 어떨까?"
    },
    {
        "description": "드디어 다 만들어...",
        "pubDate": "2021-07-11  04:11:00",
        "title": "마지막 열돔 하나만 만들자 코로나"
    },
]




def Graphmaking(yesCount, noCount): # 주석 규칙 적용해서 명명합시다.
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    plt.xlabel('검색단어')
    plt.ylabel('검색횟수')

    X1=[1,3,5,7]
    data1 = [1,2,3,4]
    plt.bar(X1, data1,color='r',width=0.5)

    X2=[1+0.5,3+0.5,5+0.5,7+0.5]
    data2 = [2,3,4,5]
    plt.bar(X2, data2,color='b',width=0.5)

plt.bar(x,y)
plt.xticks(x,y)
plt.show()