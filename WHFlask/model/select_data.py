import pymysql
'''connect doongu, compTBL'''

def select_noticeTBL():
    conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
    
    try:
        with conn.cursor() as curs:
        
            query ="""select * from noticeTBL"""
            curs.execute(query)
            
            render_select_data = curs.fetchall()
    finally:
        conn.close()

    return render_select_data

    