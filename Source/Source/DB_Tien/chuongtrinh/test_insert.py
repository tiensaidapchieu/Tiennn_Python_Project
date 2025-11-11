from common.insertdanhmuc import insert_danhmuc

while True:
    ten = input("Nhập vào tên danh mục: ")
    mo_ta = input("Nhập vào mô tả: ")

    if not ten.strip():
        print("⚠️ Tên danh mục không được để trống.")
        continue

    insert_danhmuc(ten, mo_ta)

    con = input("Tiếp tục (y để tiếp, ký tự bất kỳ để thoát): ").lower()
    if con != "y":
        break
