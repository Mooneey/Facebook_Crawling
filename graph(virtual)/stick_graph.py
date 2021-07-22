# 모 듈 명 : stick_graph
# 작 성 자 : 조용훈, 구자원
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.21
# 정    의 : 그래프 출력

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

def Graphmaking(yesCount, noCount): # 주석 규칙 적용해서 명명합시다.
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    plt.xlabel('검색단어')
    plt.ylabel('검색횟수')

    x = np.arange(2)
    news = ["코로나", "열돔"]
    values = [yesCount, noCount]
    #plt.axis([-1, 3, 0, 20]) 이 부분 뺐는데 오히려 그래프가 잘나옵니다.
    plt.title('코로나 검색 데이터')

    plt.bar(x, values)
    plt.xticks(x, news)
    plt.show()
