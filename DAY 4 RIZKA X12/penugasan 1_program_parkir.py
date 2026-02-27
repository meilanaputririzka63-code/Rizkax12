import tkinter as tk
from tkinter import ttk

def hitung_biaya():
    try:
        # Logika sederhana: Biaya = (Keluar - Masuk) * 2000
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())
        durasi = keluar - masuk
        if durasi < 0: durasi = 0
        
        biaya = durasi * 2000
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(biaya))
        
        # Menambahkan data ke tabel
        no_plat = entry_plat.get()
        tree_terakhir.insert("", tk.END, values=(no_plat, masuk, keluar, biaya))
        tree_banyak.insert("", tk.END, values=(no_plat, masuk, keluar, biaya))
    except ValueError:
        pass

# Setup Window Utama
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("800x500")

# Header
tk.Label(root, text="Aplikasi Parkir Kelompok 6", font=("Arial", 14, "bold")).place(x=20, y=10)

# Input Section (Kiri)
tk.Label(root, text="Cari NoPol").place(x=20, y=50)
tk.Entry(root, width=15).place(x=100, y=50)
tk.Button(root, text="Cari").place(x=210, y=47)

tk.Label(root, text="No Plat Polisi").place(x=20, y=80)
entry_plat = tk.Entry(root, width=25)
entry_plat.place(x=100, y=80)

tk.Label(root, text="Waktu Masuk").place(x=20, y=110)
entry_masuk = tk.Entry(root, width=25)
entry_masuk.place(x=100, y=110)

tk.Label(root, text="Waktu Keluar").place(x=20, y=140)
entry_keluar = tk.Entry(root, width=25)
entry_keluar.place(x=100, y=140)

tk.Label(root, text="Biaya").place(x=20, y=170)
entry_biaya = tk.Entry(root, width=15)
entry_biaya.place(x=100, y=170)
tk.Button(root, text="Button", command=hitung_biaya).place(x=210, y=167)

# Informasi Biaya (Kanan)
tk.Label(root, text="Biaya Per Jam", font=("Arial", 12), fg="red").place(x=400, y=80)
tk.Label(root, text="Rp. 2.000", font=("Arial", 24, "bold"), fg="red").place(x=400, y=110)

# Tabel Section (Bawah)
# 1. Tabel Urut Terakhir Keluar
tk.Label(root, text="List Pelanggan Urut Terakhir Keluar", fg="blue").place(x=20, y=220)
cols = ("No Plat Polisi", "Masuk", "Keluar", "Biaya")
tree_terakhir = ttk.Treeview(root, columns=cols, show="headings", height=5)
for col in cols:
    tree_terakhir.heading(col, text=col)
    tree_terakhir.column(col, width=80)
tree_terakhir.place(x=20, y=245, width=350)

# 2. Tabel Banyak Bayar
tk.Label(root, text="List Pelanggan Banyak Bayar", fg="blue").place(x=400, y=220)
tree_banyak = ttk.Treeview(root, columns=cols, show="headings", height=5)
for col in cols:
    tree_banyak.heading(col, text=col)
    tree_banyak.column(col, width=80)
tree_banyak.place(x=400, y=245, width=350)

root.mainloop()