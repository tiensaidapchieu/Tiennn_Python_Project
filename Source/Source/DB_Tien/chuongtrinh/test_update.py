from common.update_danhmuc import update_danhmuc

while True:
    madm = input("Mã danh mục: ")
    ten = input("Nhập vào tên danh mục: ")
    mo_ta = input("Nhập vào mô tả: ")

    if not ten.strip():
        print("⚠️ Tên danh mục không được để trống.")
        continue

    update_danhmuc(madm,ten, mo_ta)

    con = input("Tiếp tục (y để tiếp, ký tự bất kỳ để thoát): ").lower()
    if con != "y":
        break
