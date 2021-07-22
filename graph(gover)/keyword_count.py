# 모 듈 명 : keyword_count
# 작 성 자 : 안준표
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.22
# 정    의 : 키워드 횟수를 출력하고 반환하는 모듈

from data_cleaning import DateCheck

# 키워드 횟수를 출력하고 반환하는 함수
def CountKeyword(keyword, sDate, eDate) :

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    resultData = DateCheck(sDate, eDate)
    # 키워드 카운트
    for i in resultData:

        if ((keyword[0] in i['주소'])) :
            count1 = count1 + 1

        if ((keyword[1] in i['주소'])) :
            count2 = count2 + 1

        if ((keyword[2] in i['주소'])) :
            count3 = count3 + 1

        if ((keyword[3] in i['주소'])) :
            count4 = count4 + 1

    resultCount = [ (keyword[0], count1), 
                    (keyword[1], count2),
                    (keyword[2], count3),
                    (keyword[3], count4) ]

    for i in resultCount :
        print('%s : %d' % (i[0], i[1]))

    

    return resultCount

    
