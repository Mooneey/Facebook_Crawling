# 모 듈 명 : data_cleaning.py
# 작 성 자 : 문재식
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.21
# 정    의 : 데이터와 날짜 값을 받아와 날짜 순으로 데이터를 정리하고 
#             해당 기간의 데이터만 추출 함.

import json

# 가상데이터 json파일을 불러와 날짜 순으로 정렬
def read_json() :
    with open(r'C:\Users\user\Desktop\graph\testdata.json', 'r', encoding='utf-8') as f:
        jsondata = json.load(f)

    # 날짜 순으로 정렬
    sortData = sorted(jsondata, key=lambda x: x['pubDate'])
    return sortData


# 사용자가 입력한 날짜와 맞는지 확인
def DateCheck(sDate, eDate) :
    resultData = []
    eDate = eDate + '  23:59:59'

    jsonData = read_json()
    
    for i in jsonData :
        if i['pubDate'] >= sDate and i['pubDate'] <= eDate :
                resultData.append({ 'title' : i['title'],
                            'description' : i['description'],
                            'pubDate' : i['pubDate'] })
        
        elif i['pubDate'] > eDate :
            break

    return resultData