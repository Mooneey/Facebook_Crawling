# 모 듈 명 : data_cleaning.py
# 작 성 자 : 문재식
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.23
# 정    의 : 공공데이터를 받아와 날짜 체크 후 반환

import json
import datetime
from dateutil.relativedelta import relativedelta

# 공공데이터 json파일을 불러와 최신날짜 순으로 정렬
def ReadJson() :
    with open(r'C:\lab\FacebookCrawling\뉴스_GoVData_데이터.json', 'r', encoding='utf-8') as f:
        jsondata = json.load(f)
    
    sortData = sorted(jsondata['data'], key=lambda x: x['일자'], reverse=True)

    return sortData


# 오늘 날짜 리턴
def GetNow():
    myDate = datetime.datetime.now()   # 현재 날짜,시간 구하기
    nowDate = str(myDate.date())  # 현재 날짜의 연, 월, 일만 구하기
    return nowDate # 예시 : '2021-07-23'


# 오늘 날짜로 부터 이전 날짜 구하기
def GetPastDay(dateKeyword):
    # 선택할 수 있는 옵션 (일/주/월/연)
    timeList = ['day','week','month','year']

    if dateKeyword == timeList[0]:
        stdDate = datetime.datetime.now()-datetime.timedelta(days=1)

    elif dateKeyword == timeList[1]:
        stdDate = datetime.datetime.now()-datetime.timedelta(weeks=1)

    elif dateKeyword == timeList[2]:
        stdDate = datetime.datetime.now()-relativedelta(months=1)

    elif dateKeyword == timeList[3]:
        stdDate = datetime.datetime.now() - relativedelta(years=1)

    # 형 변환 후 리턴 ( 예시 : '2021-07-23')
    # return stdDate.strftime('%Y.%m.%d')
    return str(stdDate.date())


# 날짜 형식 변환
# def ChangeDate(tempDate, dateFormat):
#     changeDate = datetime.datetime.strptime(tempDate, 
#                             '%Y%m%d')
#     if dateFormat == '-' :
#         changeDateResult = changeDate.strftime('%Y-%m-%d') #변경: 년-월-일
#         return changeDateResult
    
#     elif dateFormat == '.' :
#         changeDateResult = changeDate.strftime('%Y.%m.%d') #변경: 년.월.일
#         return changeDateResult


# 사용자가 입력한 날짜와 맞는지 확인
def DateCheck(stdDate) :
    
    resultData = []

    sortData = ReadJson()

    for i in sortData :
        if i['일자'] >= stdDate :
                resultData.append({ '제목' : i['제목'],
                            '주소' : i['주소'],
                            '일자' : i['일자'],
                            '언론사' : i['언론사'],
                            '인용문' : i['인용문'],
                            '소스' : i['소스'],
                            '개체명인물/지역/기관' : i['개체명인물/지역/기관'],
                            '특성추출' : i['특성추출'] })
        else :
            break

    # 정제된 데이터 저장
    with open('%s_GoVData_%s.json' % ('뉴스', '데이터_정제'), 'w', encoding='utf-8') as filedata :
        rJson = json.dumps(resultData, 
                            indent=4, 
                            sort_keys=True,
                            ensure_ascii=False ) 
        filedata.write(rJson)

    print('%s_GoVData_%s.json' % ('뉴스', '데이터_정제'))

    return resultData