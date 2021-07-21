# 모 듈 명 : get_keyword
# 작 성 자 : 안준표
# 작 성 일 : 2021.07.21
# 수 정 일 : 2021.07.21
# 정    의 : 

# 키워드 횟수를 출력하고 반환하는 함수
def get_dataKeyword(keyword1, keyword2, data): 
    keyword1 = input("키워드를 입력해주세요: ")
    print(keyword1)
    keyword2 = input("키워드를 입력해주세요: ")
    print(keyword2)
    
    coronaCount = 0
    heatCount = 0

    for i in data:
        if (keyword1 in i['title']) or (keyword1 in i['description']):
            coronaCount = coronaCount + 1
        if(keyword2 in i['title']) or (keyword2 in i['description']):
            heatCount = heatCount + 1


    print('%s : %d' % (keyword1, coronaCount) )
    print('%s : %d' % (keyword2, heatCount) )

    return coronaCount, heatCount