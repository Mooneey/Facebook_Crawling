# 모 듈 명 : main
# 작 성 자 : 구자원
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.23
# 정    의 : 데이터 생성, 변환, 그래프 출력부분을 합하여 메인함수로 결과 도출

from draw_graph import DrawGraph
from keyword_count import CountKeyword
from data_cleaning import GetPastDay

# 메인함수
def Main() :

    # day / week / month / year 4가지 옵션
    dateKeyword = 'year'

    # 예시 키워드
    keyword = ['문재인', 
                '트럼프',
                '이주열',
                '임종룡']

    # 오늘로부터 기준 날짜 구하기
    stdDate = GetPastDay(dateKeyword)

    # 키워드 카운트
    resultCount = CountKeyword(keyword, stdDate)

    DrawGraph(resultCount, stdDate)


if __name__ == '__main__' :
    Main()