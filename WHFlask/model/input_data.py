import pymysql
'''connect doongu, compTBL'''

def input_report_data(type, title, content, image, latitude, longitude, date):
    conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
    
    try: # 자원을 할당해주고 해제해주지 않으면 close해도 에러난다.
        with conn.cursor() as curs:
        
            query ="""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', %s, %s, %s, %s,%s, %s)"""
            curs.execute(query, ( title, content, image, latitude, longitude, date,))
            conn.commit()
    finally:
        conn.close()
    
    # ??? f를 이용해서 쿼리 날리면 안된다. ㅋㅋ
    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test','test','test','test','test','test','test')""")
    # conn.commit()
    # # 잘 되는뎅 json_data 문제, format 문제 
    # query = """Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test','test','test','test','test',%s,'test')"""
    # curs.execute(query, ('fuckyou'))
    # conn.commit()
    # title

    '''
    test
    '''
    # # content
    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', 'test', {content},'test','test','test','test')""")
    # conn.commit()

    # # image
    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', 'test', 'test', {image},'test','test','test')""")
    # conn.commit()

    # # latitude
    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', 'test', 'test','test',{latitude},'test','test')""")
    # conn.commit()

    # # longitude
    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', 'test', 'test','test','test',{longitude},'test')""")
    # conn.commit()

    # # longitude
    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', 'test', 'test','test','test','test',{date})""")
    # conn.commit()

    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', {title}, {content}, {image}, {latitude},{longitude},{data} )""")
    # print(" 데이터를 추가하였습니다 ! ")
    # conn.commit()


def input_walk_data(destination, diff, start, end):
    global curs, conn
    conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')

    try: # 자원을 할당해주고 해제해주지 않으면 close해도 에러난다.
        with conn.cursor() as curs:
        
            query = """Insert into walkTBL VALUES ( (SELECT IFNULL(MAX(datacode) + 1, 1) FROM walkTBL tester), 'test', %s, %s, %s, %s)"""
            curs.execute(query, (destination, diff, start, end,))
            conn.commit()
    finally:
        conn.close()