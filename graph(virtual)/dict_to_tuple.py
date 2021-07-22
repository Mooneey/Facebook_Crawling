# 모 듈 명 : dict_to_tuple.py
# 작 성 자 : 문재식
# 작 성 일 : 2021.07.21
# 정    의 : 딕셔너리 형을 튜플로 바꾸는 모듈

def DictToTuple(data) :
    resultData = []

    for i in data :
        resultData.append(list(zip(i.keys(), i.values())))

    return resultData
