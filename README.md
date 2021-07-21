

# walker_holic_back
walker_holic 애플리케이션의 프론트와 서버사이 데이터를 주고 받기 위한 코드입니다.


## Dependency


> Flask==2.0.1



> pycodestyle==2.7.0



> ORM(SQLAlchemy) 사용 예정



> requests==2.26.0

## Directories
```
WHFlask
	├── app.py
	|
	├── app
	│   ├── api
	│   │   ├── decorator.py
	│   │   ├── error_handler.py
	│   │   ├── __init__.py
	│   │	├── auth.py (요구사항이 적어 단일 파일로 작성)
	│   │	└── template.py (형식상 적어놓음)
	│   │   
	│   ├── asset (형식상  적어놓음) 
	│   │   └── index.html   
	│   │   
	│   └── __init__.py
	│   
	|
	├───- controller   
	│      ├── __init__.py
	│      └── json_handler.py	   
	│
	|
	├───- model
	    ├── __init__.py
	    └── mysql
		├── base.py
	 	├── __init__.py 
	    	├── log.py
	    	└── master_config.py
	
```

- app.py

- app/api
	- decorator.py
	- error_handler.py
	- __init__.py
	- auth.py
	- template.py
# Reference



본 내용은 iml1111님의 https://github.com/iml1111/IMFlask-Pymongo 를 참고하여 작성하였습니다.
<br></br>
<p align = "center"><a href="https://github.com/iml1111/IMFlask-Pymongo"><img src="http://img.shields.io/badge/iml1111-655ced?style=for-the-badge&color=informational" style="height : auto; margin-left : 10px; margin-right : 10px;"/></a> </p>

## 하는김에 나중에 한번에 질문해볼거 질문해야지 !
- 위와 같은 패턴도 mvc 패턴이라고 보는지 ? 아니면 딱히 보여줄게 없어서 view폴더를 안만든건지 .. ?
- api 요건이 적으면 auth.py 하나로 한다는데 왜 이름이 auth인지 그리고 저렇게 app/api구조에 넣는 것이 구조화된 방식인지 ?
- 전체적인 구조가 app에서 request가 들어오면 controller로 보내고 controller에서 db에 넣기 적합하게 바꿔준 다음 model에 가는 방식인지, response는 반대 구조인지 ?
- 프론트와 json파일 형식으로 db에 데이터를 CRUD하는 코드인데, (View가 없음) Controller 부분에 그 json을 다루는 handler 파일을 생성해 다루는 것이 맞는지 ?
