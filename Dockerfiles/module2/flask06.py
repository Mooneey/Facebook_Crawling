from flask import Flask # 서버 구현을 위한 Flask
from flask_restx import Api, Resource # API 구현을 위한 API Import

app = Flask(__name__) # 매개변수(파라미터)로 App 패키지 이름을 지정
api = Api(app) # Flask 개체를 API 개체로 등록

# GET 방식
@api.route('/helloget') 
class HelloworldExam(Resource):
    def get(self): # GET으로 요청
        return {
                'message' : 'Hello World - GET Data'
        } # JSON 형식으로 데이터 반환

@api.route('/helloget/<string:name>') # URL 값 요청
class HelloworldExam(Resource):
    def get(self, name): # GET Data 처리 매개변수 요청
        return {
                'message' : 'My Name - %s' % name
        } # JSON 형식으로 데이터 반환

@api.route('/hellopost') # URL 값 요청
class HelloworldExam(Resource):
    def post(self): # POST Data 처리
        return {
                'message' : 'Hello World - POST Data'
        } # JSON 형식으로 데이터 반환

@api.route('/hellopost') # URL 값 요청
class HelloworldExam(Resource):
    def post(self, name): # GET Data 처리 매개변수 요청
        return {
                'message' : 'My Name - %s' % name
        } # JSON 형식으로 데이터 반환

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)