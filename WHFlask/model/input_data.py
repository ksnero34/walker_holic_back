import pymysql
'''connect doongu, compTBL'''
conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
curs = conn.cursor()

def input_report_data(type, title, content, image, latitude, longitude, date):
    global curs,conn
    
    # ??? f를 이용해서 쿼리 날리면 안된다. ㅋㅋ
    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test','test','test','test','test','test','test')""")
    # conn.commit()
    # # 잘 되는뎅 json_data 문제, format 문제 
    # query = """Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test','test','test','test','test',%s,'test')"""
    # curs.execute(query, ('fuckyou'))
    # conn.commit()
    # title
    query ="""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', %s, %s, %s, %s,%s, %s)"""
    curs.execute(query, ( title, content, image, latitude, longitude, date,))
    conn.commit()
    conn.close()
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
    
    query = """Insert into walkTBL VALUES ( (SELECT IFNULL(MAX(datacode) + 1, 1) FROM walkTBL tester), 'test', %s, %s, %s, %s)"""
    curs.executemany(query, (destination, diff, start, end,))
    conn.commit()
    conn.close()
