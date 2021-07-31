import pymysql
'''connect doongu, compTBL'''
conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
curs = conn.cursor()

def input_report_data(json_data):
    global curs,conn
    curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', 'test', 'test','test','test','test','test')""")
    conn.commit()

    title = json_data['title']
    content = json_data['content']
    image = json_data['image']
    latitude = json_data['latitude']
    longitude = json_data['longitude']
    data = json_data['date'] 

    # curs.execute(f"""Insert into compTBL VALUES ( (SELECT IFNULL(MAX(compID) + 1, 1) FROM compTBL test), 'test', {title}, {content}, {image}, {latitude},{longitude},{data} )""")
    # print(" 데이터를 추가하였습니다 ! ")
    # conn.commit()


def input_walk_data(json_data):
    global curs, conn

    destination = json_data['destination']
    diff = json_data['diff']
    start = json_data['start']
    end = json_data['end']
    
    curs.execute(f"""Insert into walkTBL VALUES ( (SELECT IFNULL(MAX(datacode) + 1, 1) FROM walkTBL tester), 'test', {destination}, {diff}, {start}, {end} )""")

    print(" 데이터를 추가하였습니다 ! ")
    conn.commit()
