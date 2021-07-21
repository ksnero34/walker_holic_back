

# walker_holic_back
walker_holic 애플리케이션의 프론트와 서버사이 데이터를 주고 받기 위한 코드입니다.


## Dependency


Flask==2.0.1
pycodestyle==2.7.0
ORM(SQLAlchemy) 사용 예정
requests==2.26.0

## Directories
```
WHFlask
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
	│   ├── __init__.py
	│   └── mysql
	|	├── base.py
	│	├── __init__.py 
	│   	├── log.py
	│   	└── master_config.py
	│
	|
	└── app.py
	
```
# Reference



본 내용은 iml1111님의 https://github.com/iml1111/IMFlask-Pymongo 를 참고하여 작성하였습니다.
<br></br>
<p align = "center"><a href="https://github.com/iml1111/IMFlask-Pymongo"><img src="http://img.shields.io/badge/iml1111-655ced?style=for-the-badge&color=informational" style="height : auto; margin-left : 10px; margin-right : 10px;"/></a> </p>

# 하는김에 나중에 한번에 질문해볼거 질문해야지 !
- 위와 같은 패턴도 mvc 패턴이라고 보는지 ? 아니면 딱히 보여줄게 없어서 view폴더를 안만든건지 .. ?
