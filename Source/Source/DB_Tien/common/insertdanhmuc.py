import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def insert_danhmuc(ten_danh_muc, mo_ta=None, trang_thai=1):
    """
    Thêm 1 danh mục mới vào bảng danhmuc.
    - ten_danh_muc: tên danh mục (bắt buộc)
    - mo_ta: mô tả danh mục (tùy chọn)
    - trang_thai: 1 = hiển thị, 0 = ẩn
    """
    connection = None
    cursor = None

    try:
        connection = connect_mysql()
        if connection is None or not connection.is_connected():
            print("❌ Không thể kết nối MySQL. Kiểm tra lại file ketnoi_mysql.py.")
            return False

        cursor = connection.cursor()
        sql = """
            INSERT INTO danhmuc (ten_danh_muc, mo_ta, trang_thai)
            VALUES (%s, %s, %s)
        """
        values = (ten_danh_muc.strip(), mo_ta.strip() if mo_ta else None, trang_thai)

        cursor.execute(sql, values)
        connection.commit()

        print(f"✅ Đã thêm danh mục '{ten_danh_muc}' thành công! (ID mới: {cursor.lastrowid})")
        return True

    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
