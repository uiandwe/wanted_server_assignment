# 원티드 코딩 테스트
## _The Last Markdown Editor, Ever_

## init load data
```sh
$ python manage_local.py loaddata ./blog/fixtures/blog.json
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


## DB
| domain | url | method | desc |
| ------ | ------ | ------ | ------ |
| company | /companies/\<str> | get | 회사 검색 |
|  | /companies | post | 회사 / 태그 등록 |
|  | /search?query=\<str> | get | 회사 이름 검색  |


## TODO
- .env 로 디비 파라미터 빼기
- 로깅
- 유틸로 뺄것들 확인하기
- 같은 이름일때 처리 + 같은 나라일때 처리 + 유니크를 어떻게 줘야 하나? -> 이름 + 나라
- language 테이블 추가 
- 전체 소스 로직 통일 (구조)
- 
