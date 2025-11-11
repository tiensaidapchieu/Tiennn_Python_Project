import mysql.connector
from mysql.connector import Error

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',      # địa chỉ MySQL server (vd: '127.0.0.1')
            user='root',           # tên user, thường là root
            password='',           # mật khẩu MySQL (điền nếu có)
            database='qlthuocankhang' # tên database của mày
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
