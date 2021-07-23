# 모 듈 명 : keyword_count
# 작 성 자 : 안준표
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.22
# 정    의 : 키워드 횟수를 출력하고 반환하는 모듈

from data_cleaning import DateCheck

# 키워드 횟수를 출력하고 반환하는 함수
def CountKeyword(keyword, stdDate) :

    resultData = DateCheck(stdDate)

    resultCount = { keyword[0] : 0, 
                    keyword[1] : 0,
                    keyword[2] : 0,
                    keyword[3] : 0 }

    for i in resultData:

        if ((keyword[0] in i['소스'] or keyword[0] in i['개체명인물/지역/기관'])) :
            resultCount[keyword[0]] = resultCount[keyword[0]] + 1

        if ((keyword[1] in i['소스'] or keyword[1] in i['개체명인물/지역/기관'])) :
            resultCount[keyword[1]] = resultCount[keyword[1]] + 1

        if ((keyword[2] in i['소스'] or keyword[2] in i['개체명인물/지역/기관'])) :
            resultCount[keyword[2]] = resultCount[keyword[2]] + 1

        if ((keyword[3] in i['소스'] or keyword[3] in i['개체명인물/지역/기관'])) :
            resultCount[keyword[3]] = resultCount[keyword[3]] + 1


    return resultCount

    