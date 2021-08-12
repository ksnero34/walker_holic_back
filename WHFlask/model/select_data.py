import pymysql
'''connect doongu, compTBL'''

def select_noticeTBL():
    conn = pymysql.connect(host='localhost', user='doongu', password ='wnsrb12', db='walker_holic',port =3306, charset='utf8')
    
    try: # 자원을 할당해주고 해제해주지 않으면 close해도 에러난다.
        with conn.cursor() as curs:
        
            query ="""select * from noticeTBL"""
            curs.execute(query)
            
            render_select_data = curs.fetchall()
    finally:
        conn.close()

    return render_select_data

    