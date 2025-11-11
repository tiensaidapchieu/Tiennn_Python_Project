import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def delete_danhmuc(id_danh_muc):
    """
    Xóa 1 danh mục khỏi bảng danhmuc theo id.
    - id_danh_muc: ID danh mục cần xóa (int)
    """
    connection = None
    cursor = None

    try:
        connection = connect_mysql()
        if connection is None or not connection.is_connected():
            print("❌ Không thể kết nối MySQL. Kiểm tra lại file ketnoi_mysql.py.")
            return False

        cursor = connection.cursor()

        # Kiểm tra danh mục có tồn tại không
        cursor.execute("SELECT ten_danh_muc FROM danhmuc WHERE id = %s", (id_danh_muc,))
        row = cursor.fetchone()
        if not row:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danh_muc}.")
            return False

        ten = row[0]

        # Thực hiện xóa
        cursor.execute("DELETE FROM danhmuc WHERE id = %s", (id_danh_muc,))
        connection.commit()

        print(f"🗑️ Đã xóa danh mục '{ten}' (ID={id_danh_muc}) thành công!")
        return True

    except Error as e:
        if connection:
            connection.rollback()
        print("❌ Lỗi khi xóa danh mục:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
