# 원티드 코딩 테스트
## pip 설치
```sh
$ 
$ pip3 install -r requirements.txt
```

## run database - mysql
```sh
$ docker-compose up
```


## init load data
- 테이블 drop 후 테이블 생성 (기존 데이터가 지워집니다.)
```sh
$ flask init-db 
```

## run test
- 테스트를 위해 초기 데이터가 필요합니다.
```sh
$ flask init-db && pytest
```


## 실행
```sh
$ python app.py
```

[http://127.0.0.1:8080/](http://127.0.0.1:8080/)


____

## API 리스트
| domain | url | method | desc |
| ------ | ------ | ------ | ------ |
| company | /companies/\<str> | get | 회사 이름으로 회사 검색 |
|  | /companies | post | 새로운 회사 추가 |
|  | /search?query=\<str> | get | 회사명 자동완성  |



____



## TODO
- init data : https://flask.palletsprojects.com/en/2.0.x/tutorial/database/
- pytest init data
- docker-compose 실행 / 테스트 
- language 테이블 추가
 
