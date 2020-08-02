import pymysql

class ConnDB(object):
    def __init__(self, db_info):
        self.host = db_info['host']
        self.port = db_info['port']
        self.user = db_info['user']
        self.password = db_info['password']
        self.db = db_info['db']
    
    def get_conn_cursor(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        return conn, conn.cursor()

    def insert_data(self, ip):
        try:
            conn, cur = self.get_conn_cursor()
            sql = f'insert into spider_mysql_test(`origin_ip`) values ("{ip}")'
            print(sql)
            print(cur.execute(sql))
            # 关闭游标
            cur.close()
            conn.commit()
        except Exception as e:
            print("eeeerorr", e)
            conn.rollback()
        # 关闭数据库连接
        conn.close()
