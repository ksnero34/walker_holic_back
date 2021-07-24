import pymysql
'''connect doongu, compTBL'''
conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
curs = conn.cursor()


'''create, test'''
def test_create():
    global curs
    curs.execute("Insert into compTBL(compID,userID,compname,comp,comppic,pic_latitude,pic_longitude,pic_date) VALUES('test','test','test','test','test','test','test','test')")
    print(" 데이터를 추가하였습니다 ! ")

'''select test'''
def test_select():
    global curs
    answer = curs.execute("select * from compTBL")
    print(" 데이터를 조회하겠습니다 ! ")
    print(answer)

'''update test'''
def test_update():
    global curs
    curs.execute("update compTBL SET compID='hjk'")
    print("데이터를 업데이트 하였습니다 ! ")

'''delete test'''
def test_delete():
    global curs
    curs.execute("Delete FROM compTBL")
    print("데이터를 삭제하였습니다 ! ")


test_create()
# test_select()
# test_update()
# test_delete()


# 커밋
conn.commit()