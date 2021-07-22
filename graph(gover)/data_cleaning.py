# 모 듈 명 : data_cleaning.py
# 작 성 자 : 문재식
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.22
# 정    의 : 공공데이터를 받아와 날짜 체크 후 반환

import json
import datetime

# 공공데이터 json파일을 불러와 날짜 순으로 정렬
def read_json() :
    with open(r'C:\Users\user\Desktop\graph(gover)\요양기관개설_GoVData_데이터.json', 'r', encoding='utf-8') as f:
        jsondata = json.load(f)

    return jsondata

# 날짜 형식 변환
def ChangeDate(tempDate, dateFormat):
    changeDate = datetime.datetime.strptime(tempDate, 
                            '%Y%m%d')
    if dateFormat == '-' :
        changeDateResult = changeDate.strftime('%Y-%m-%d') #변경: 년-월-일
        return changeDateResult
    
    elif dateFormat == '.' :
        changeDateResult = changeDate.strftime('%Y.%m.%d') #변경: 년.월.일
        return changeDateResult


# 사용자가 입력한 날짜와 맞는지 확인
def DateCheck(sDate, eDate) :
    
    resultData = []

    jsonData = read_json()
    
    for i in jsonData['data'] :

        # changeDate = datetime.datetime.strptime(i['개설일자'], 
                            # '%Y%m%d')#표시형식
        # changeDateResult = changeDate.strftime('%Y-%m-%d') #변경 : 년-월-일 시:분:초
        
        changeDateResult = ChangeDate(i['개설일자'], '-')
        
        if i['개설일자'] >= sDate and i['개설일자'] <= eDate :
                resultData.append({ '요양기관명' : i['요양기관명'],
                            '표시과목' : i['표시과목'],
                            '주소' : i['주소'],
                            '개설일자' : changeDateResult })

    with open('%s_GoVData_%s.json' % ('요양기관개설', '데이터_변경'), 'w', encoding='utf-8') as filedata :
        rJson = json.dumps(resultData, 
                            indent=4, 
                            sort_keys=True,
                            ensure_ascii=False ) 
        filedata.write(rJson)

    print('%s_GoVData_%s.json' % ('요양기관개설', '데이터_변경'))

    return resultData