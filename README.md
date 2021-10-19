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
```sh
$ flask init-db
```

## run test
```sh
$ pytest
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
| company | /companies/\<str> | get | 회사 검색 |
|  | /companies | post | 회사 / 태그 등록 |
|  | /search?query=\<str> | get | 회사 이름 검색  |



____



## TODO
- init data : https://flask.palletsprojects.com/en/2.0.x/tutorial/database/
- pytest init data
- 시리얼라이져
- wanning 잡기
- docker-compose 실행 / 테스트 
- 테스트 추가
- app 이름을 뭘로 해야 할까?
- 데코레이터 가능한지 확인
- 유틸로 뺄것들 확인하기

- language 테이블 추가 -> 시간 남으면 
