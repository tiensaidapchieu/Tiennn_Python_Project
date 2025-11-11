import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def update_danhmuc(id_danh_muc, ten_moi=None, mo_ta_moi=None, trang_thai_moi=None):
    """
    Cập nhật thông tin danh mục theo ID.
    - id_danh_muc: ID của danh mục cần sửa
    - ten_moi: tên danh mục mới (hoặc None nếu không đổi)
    - mo_ta_moi: mô tả mới (hoặc None nếu không đổi)
    - trang_thai_moi: trạng thái mới (1 = hiển thị, 0 = ẩn, None nếu không đổi)
    """
    connection = None
    cursor = None

    try:
        connection = connect_mysql()
        if connection is None or not connection.is_connected():
            print("❌ Không thể kết nối MySQL.")
            return False

        cursor = connection.cursor()

        # Kiểm tra danh mục tồn tại
        cursor.execute("SELECT ten_danh_muc, mo_ta, trang_thai FROM danhmuc WHERE id = %s", (id_danh_muc,))
        row = cursor.fetchone()
        if not row:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danh_muc}.")
            return False

        ten_cu, mo_ta_cu, trang_thai_cu = row

        # Gán giá trị mới (nếu không nhập thì giữ nguyên)
        ten_cap_nhat = ten_moi if ten_moi is not None and ten_moi.strip() != "" else ten_cu
        mo_ta_cap_nhat = mo_ta_moi if mo_ta_moi is not None else mo_ta_cu
        trang_thai_cap_nhat = trang_thai_moi if trang_thai_moi is not None else trang_thai_cu

        sql = """
            UPDATE danhmuc
            SET ten_danh_muc = %s, mo_ta = %s, trang_thai = %s, ngay_cap_nhat = NOW()
            WHERE id = %s
        """
        values = (ten_cap_nhat, mo_ta_cap_nhat, trang_thai_cap_nhat, id_danh_muc)
        cursor.execute(sql, values)
        connection.commit()

        print(f"✅ Đã cập nhật danh mục ID={id_danh_muc} thành công!")
        print(f"📘 Tên: {ten_cu} → {ten_cap_nhat}")
        return True

    except Error as e:
        if connection:
            connection.rollback()
        print("❌ Lỗi khi cập nhật danh mục:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
