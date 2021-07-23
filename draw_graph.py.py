import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np


#count = 
#city = 

def Graphmaking(count,keyword): # 주석 규칙 적용해서 명명합시다.
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    plt.xlabel(keyword)
    plt.ylabel('검색횟수')

    x = np.arange(2)
    #news = []
    values = count
    #plt.axis([-1, 3, 0, 20]) 이 부분 뺐는데 오히려 그래프가 잘나옵니다.
    plt.title('언론사 검색데이터')

    plt.bar(x, values)
    plt.xticks(x, keyword)
    plt.show()

Graphmaking([9,18],["문재인","트럼프"]) 
temp = 0