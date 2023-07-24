from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


@app.get("/hello") 
def hello():
    return {"message": "안녕하세요 하입보이"}

@app.get('/') #여기서 app은 path operation decorator '/'=path, 'get'=operation 
def index():
    return{'data': {'name': 'Sarthak'}}

@app.get('/blog') # 자유롭게 변하는 변수 1,2,3,4 이런 아이디를 주고 싶다면 대괄호안에 변수이름 설정

def about(limit =10, published : bool =True, sort : Optional[str]=None): #위에서 변수이름을 설정해줬다면 id를 함수 안에 씀

    #정수형 변수만 쓰고 싶다면 변수 뒤에 :int를 붙여준다!!!

    if published:
        return{'data':f'{limit} published blogs from the pipdb'}
    else:
        return{'data':f'{limit} blogs from the db'}
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'} #fastapi는 한줄씩 읽어가기 때문에 위의 코드에 성립이 안되면 error! 그래서 이 함수를 위로 올려주면 해결!

@app.get('/blog/{id}/comments') #parameter는 넣을려는 값!
def comments(id):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published_at : Optional[bool]



@app.post('/blog')
def create_blog(request:Blog):
    return{'data':'Blog is created'}



#terminal에서 main.py가 파일일 때 uvicorn main:app을 사용
#terminal에서 beautiful.py가 파일일 때 uvicorn beautiful:app을 사용

print("Hello world!")