import pymysql
'''connect doongu, compTBL'''
conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
curs = conn.cursor()

def select_noticeTBL():
    global curs,conn
    
    query ="""select * from noticeTBL"""
    curs.execute(query)
    render_select_data = curs.fetchall()
    conn.close()
    return render_select_data

    