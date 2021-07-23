# [Infosec Academy] Module Project 1
![header](https://capsule-render.vercel.app/api?type=Waving&color=auto&height=300&section=header&text=InfosecAcademy&fontSize=90)

<div align=center><h1>:+1: We are Team 5 :heart:</h1></div>

<a href="https://infosec.adtcaps.co.kr/">
  <img
    src="https://img.shields.io/badge/Infosec-Team5-red?style=flat-square&logo=infosec&logoColor=white&link=https://infosec.adtcaps.co.kr/"></a>

Facebook News Page Crawling (with Graph API)

사용법 
=============
## 파일 종류 
-------------
#### data_cleaning
:smile: 공공데이터를 받아와 날짜 체크 후 반환   

#### dict_to_tuple
:smirk: 딕셔너리 형을 튜플로 바꾸는 모듈   

#### draw_graph
:smiley: 그래프 출력하는 모듈   

#### keyword_count
:wink: 키워드 횟수를 출력하고 반환하는 모듈   

#### main
:heart_eyes: 데이터 생성, 변환, 그래프 출력부분을 합하여 메인함수로 결과 도출   


## 실행 과정 및 결과
-------------
![1](https://user-images.githubusercontent.com/80608601/126746500-852bb412-3877-4004-a8eb-3dfca72b2664.PNG)   
:one:현재일 기준으로 과거(1년/1개월/1주/1일) 기간 지정및 키워드 4개 지정      
   
![2](https://user-images.githubusercontent.com/80608601/126747875-0fd0df9d-bb65-4abf-8c2e-cb2115e19f19.PNG)   
:two:사용자가 입력한 날짜와 맞는지 확인 후 필요 없는 요소를 제거한 json파일로 정제 후 저장   
   
![3](https://user-images.githubusercontent.com/80608601/126747876-54bb60bf-00d0-4d86-bc74-62ec7ed6b07f.PNG)   
:three:정제된 json파일에 입력된 키워드가 있는지 비교 후 빈도 반환   
   
![4](https://user-images.githubusercontent.com/80608601/126747878-0387d92d-864e-43aa-8356-a0e9ad9f2746.PNG)   
:four:검출한 키워드의 빈도 수를 그래프로 그리기   
   
![5](https://user-images.githubusercontent.com/80608601/126747880-0534fc5d-9c92-4833-b842-04fccbf043ef.PNG)
![6](https://user-images.githubusercontent.com/80608601/126747881-829c5af5-46c4-495e-bf34-5939e0086f38.PNG)
![7](https://user-images.githubusercontent.com/80608601/126747882-8f0fd64a-f04b-4af8-86da-7608fff3db46.PNG)
![8](https://user-images.githubusercontent.com/80608601/126747884-12a67423-aa65-4404-abe7-a7a936b0af1e.PNG)   
:five:실행 결과 그래프(년/월/주/일)   
   

