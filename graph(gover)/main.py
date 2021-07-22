# 모 듈 명 : main
# 작 성 자 : 구자원
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.21
# 정    의 : 데이터 생성, 변환, 그래프 출력부분을 합하여 메인함수로 결과 도출

from draw_graph import DrawGraph
from keyword_count import CountKeyword

def Main() :

    # 개설일자
    # startDate = '19700101' # 형식 YYYYMMDD
    # endDate = '20210701'

    startDate = input("개설일자 start: ")
    print(startDate)
    endDate = input("개설일자 end: ")
    print(endDate)

    keyword = ['서울', 
                '경기',
                '충청',
                '남도']

    # 키워드 카운트
    resultCount = CountKeyword(keyword, startDate, endDate)

    DrawGraph(resultCount, startDate, endDate)


if __name__ == '__main__' :
    Main()