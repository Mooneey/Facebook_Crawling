# 모 듈 명 : main
# 작 성 자 : 구자원
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.21
# 정    의 : 데이터 생성, 변환, 그래프 출력부분을 합하여 메인함수로 결과 도출

from data_cleaning import DateCheck
from get_keyword import get_dataKeyword
from stick_graph import Graphmaking
import json

def Main(): # 정적언어 처럼 시작함수를 지정할 수 있다.
    # json 파일 불러오기
 
    # 가상데이터를 날짜별로 정렬
    startDate = '2021-07-01'
    endDate = '2021-07-10'
    resultData = DateCheck(startDate, endDate)
    
    # 특정 키워드 입력 후 빈도수를 세준다
    datakeyword1 = 0    
    datakeyword2 = 0 
    coronaCount, heatCount = get_dataKeyword(datakeyword1, datakeyword2, resultData)    
    
    # 반환된 데이터를 그래프로 출력한다.
    Graphmaking(coronaCount, heatCount)
    temp = 0



if __name__ == '__main__':
    Main()

# __name__ : 내장변수 /  글로벌 변수 - 파이썬에서 정한(예약한) 이미 있는 변수
   
