import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def get_danhmuc():
    """
    Lấy toàn bộ danh mục từ bảng danhmuc.
    Trả về: list các tuple (id, ten_danh_muc, mo_ta, trang_thai, ngay_tao)
    """
    connection = None
    cursor = None

    try:
        connection = connect_mysql()
        if connection is None or not connection.is_connected():
            print("❌ Không thể kết nối MySQL.")
            return []

        cursor = connection.cursor()
        sql = "SELECT id, ten_danh_muc, mo_ta, trang_thai, ngay_tao FROM danhmuc ORDER BY id ASC"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")
            return []

        print("📋 Danh sách danh mục:")
        print("-" * 60)
        for row in rows:
            id, ten, mo_ta, trang_thai, ngay_tao = row
            tt_text = "✅ Hiển thị" if trang_thai == 1 else "🚫 Ẩn"
            print(f"ID: {id} | Tên: {ten} | Mô tả: {mo_ta or '—'} | Trạng thái: {tt_text} | Ngày tạo: {ngay_tao}")

        return rows

    except Error as e:
        print("❌ Lỗi khi lấy danh mục:", e)
        return []

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
