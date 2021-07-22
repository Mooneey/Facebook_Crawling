import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

# 모 듈 명 : graph01.py
# 작 성 자 : 조용훈,구자원
# 작 성 일 : 2021.07.22
# 수 정 일 : 2021.07.22
# 정    의 : 추출한 값으로 그래프를 출력한다()


#count = 
#city = 

def Graphmaking(count,city): # 주석 규칙 적용해서 명명합시다.
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    plt.xlabel(city)
    plt.ylabel('기관수')

    x = np.arange(2)
    #news = []
    values = count
    #plt.axis([-1, 3, 0, 20]) 이 부분 뺐는데 오히려 그래프가 잘나옵니다.
    plt.title('지역별 요양기관')

    plt.bar(x, values)
    plt.xticks(x, city)
    plt.show()

# Graphmaking([9,18],["서울특별시","부산광역시"])   테스트입니다.
# temp = 0