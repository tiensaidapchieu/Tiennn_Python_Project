import tkinter as tk
from tkinter import ttk, messagebox
from common.get_danhmuc import get_danhmuc
from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc


# ================== HÀM GIAO DIỆN ==================

def load_table():
    """Nạp dữ liệu danh mục vào bảng"""
    for i in tree.get_children():
        tree.delete(i)
    rows = get_danhmuc()
    if not rows:
        return
    for row in rows:
        id, ten, mo_ta, trang_thai, ngay_tao = row
        tt_text = "✅ Hiển thị" if trang_thai == 1 else "🚫 Ẩn"
        tree.insert("", "end", values=(id, ten, mo_ta, tt_text, ngay_tao))


def clear_input():
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)


def on_add():
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()
    if not ten:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục.")
        return
    insert_danhmuc(ten, mota)
    load_table()
    clear_input()


def on_update():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần sửa.")
        return
    item = tree.item(selected[0])
    id_dm = item["values"][0]
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()
    if not ten:
        messagebox.showwarning("Thiếu thông tin", "Tên danh mục không được để trống.")
        return
    update_danhmuc(id_dm, ten, mota)
    load_table()
    clear_input()


def on_delete():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần xóa.")
        return
    item = tree.item(selected[0])
    id_dm = item["values"][0]
    delete_danhmuc(id_dm)
    load_table()


def on_select(event):
    selected = tree.selection()
    if not selected:
        return
    item = tree.item(selected[0])
    entry_ten.delete(0, tk.END)
    entry_ten.insert(0, item["values"][1])
    entry_mota.delete(0, tk.END)
    entry_mota.insert(0, item["values"][2])


# ================== GIAO DIỆN CHÍNH ==================

root = tk.Tk()
root.title("💊 Quản Lý Danh Mục - Giao Diện CRUD")
root.geometry("900x600")
root.configure(bg="#f5f6fa")

title = tk.Label(root, text="📦 QUẢN LÝ DANH MỤC", font=("Segoe UI", 16, "bold"), bg="#f5f6fa", fg="#2c3e50")
title.pack(pady=10)

frame_input = tk.Frame(root, bg="#f5f6fa")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Tên danh mục:", font=("Segoe UI", 11), bg="#f5f6fa").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_ten = tk.Entry(frame_input, font=("Segoe UI", 11), width=35)
entry_ten.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_input, text="Mô tả:", font=("Segoe UI", 11), bg="#f5f6fa").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_mota = tk.Entry(frame_input, font=("Segoe UI", 11), width=35)
entry_mota.grid(row=1, column=1, padx=10, pady=5)

frame_btn = tk.Frame(root, bg="#f5f6fa")
frame_btn.pack(pady=10)

style_btn = {"font": ("Segoe UI", 11, "bold"), "width": 12, "height": 1, "pady": 5}

tk.Button(frame_btn, text="➕ Thêm", command=on_add, bg="#2ecc71", fg="white", **style_btn).pack(side="left", padx=15)
tk.Button(frame_btn, text="✏️ Sửa", command=on_update, bg="#f39c12", fg="white", **style_btn).pack(side="left", padx=15)
tk.Button(frame_btn, text="🗑️ Xóa", command=on_delete, bg="#e74c3c", fg="white", **style_btn).pack(side="left", padx=15)
tk.Button(frame_btn, text="🔄 Làm mới", command=load_table, bg="#3498db", fg="white", **style_btn).pack(side="left", padx=15)

# =============== BẢNG DANH MỤC ====================
frame_table = tk.Frame(root)
frame_table.pack(fill="both", expand=True, padx=15, pady=10)

columns = ("id", "ten_danh_muc", "mo_ta", "trang_thai", "ngay_tao")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=15)
tree.heading("id", text="ID")
tree.heading("ten_danh_muc", text="Tên danh mục")
tree.heading("mo_ta", text="Mô tả")
tree.heading("trang_thai", text="Trạng thái")
tree.heading("ngay_tao", text="Ngày tạo")

tree.column("id", width=50, anchor="center")
tree.column("ten_danh_muc", width=200)
tree.column("mo_ta", width=300)
tree.column("trang_thai", width=100, anchor="center")
tree.column("ngay_tao", width=160, anchor="center")

tree.pack(fill="both", expand=True)
tree.bind("<<TreeviewSelect>>", on_select)

# =============== STYLE ====================
style = ttk.Style()
style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
style.configure("Treeview", font=("Segoe UI", 10), rowheight=28)
style.map("Treeview", background=[("selected", "#d1f2eb")])

load_table()
root.mainloop()
