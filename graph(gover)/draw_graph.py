# 모 듈 명 : draw_graph
# 작 성 자 : 조용훈, 구자원
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.22
# 정    의 : 그래프 출력

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
from data_cleaning import ChangeDate

def StickGraph(resultCount, title) :

    plt.xlabel('지역 이름')
    plt.ylabel('기관수')

    x = np.arange(4)

    # resultData = [('코로나', 12), ('열돔'), 8 ...]
    cities = [resultCount[0][0], resultCount[1][0], resultCount[2][0], resultCount[3][0]]
    values = [resultCount[0][1], resultCount[1][1], resultCount[2][1], resultCount[3][1]]
    
    #plt.axis([-1, 3, 0, 20]) 이 부분 뺐는데 오히려 그래프가 잘나옵니다.
    plt.title(title)

    plt.bar(x, values)
    plt.xticks(x, cities)
    plt.show()

def PieGraph(resultCount, title) :

    ratio = [resultCount[0][1], resultCount[1][1], resultCount[2][1], resultCount[3][1]]
    labels = [resultCount[0][0], resultCount[1][0], resultCount[2][0], resultCount[3][0]]
    explode = [ 0.05, 0.05, 0.05, 0.05]
    colors = ['#8fd9b6', '#ff9999', '#ffc000', '#d395d0']
    
    plt.title(title)
    plt.pie(ratio, labels=labels, autopct='%.1f%%', explode=explode,
                shadow=True, colors=colors,)

    plt.show()


def DrawGraph(resultCount, startDate, endDate) :
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)

    title = '지역별 요양기관 수\n\n'
    title = title + '%s ~ %s' % (ChangeDate(startDate, '.'), ChangeDate(endDate, '.'))

    
    StickGraph(resultCount, title)
    PieGraph(resultCount, title)
