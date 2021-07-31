import pymysql
'''connect doongu, compTBL'''
conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
curs = conn.cursor()

def input_report_data(json_data):
    global curs,conn
    curs.execute(f"""INSERT INTO compTBL VALUES ( (SELECT IFNULL(MAX(datacode) + 1, 1) FROM compTBL), 'test', {json_data['title']}, {json_data['content']}, {json_data['image']}, {json_data['latitude']},{json_data['longitude']},{json_data['date']} )""")
    print(" 데이터를 추가하였습니다 ! ")
    conn.commit()


def input_walk_data(json_data):
    global curs, conn
    curs.execute(f"""INSERT INTO walkTBL VALUES ( (SELECT IFNULL(MAX(datacode) + 1, 1) FROM walkTBL), 'test', {json_data['destination']}, {json_data['diff']}, {json_data['start']}, {json_data['end']} )""")
    print(" 데이터를 추가하였습니다 ! ")
    conn.commit()
