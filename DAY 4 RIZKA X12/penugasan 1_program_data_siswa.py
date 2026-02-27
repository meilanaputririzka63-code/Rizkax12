import tkinter as tk
from tkinter import messagebox

def simpan_data():
    # Logika sederhana untuk menampilkan pesan saat tombol Simpan diklik
    messagebox.showinfo("Informasi", "Data Siswa Berhasil Disimpan!")

def hapus_data():
    # Menghapus semua inputan di formulir
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_asal.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_telp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# Membuat window utama
root = tk.Tk()
root.title("MainWindow")
root.geometry("500x700")
root.configure(bg="#E0E0E0")

# Header
header_frame = tk.Frame(root, bg="#A0E4E4", height=60)
header_frame.pack(fill="x")
tk.Label(header_frame, text="DATA SISWA BARU", font=("Arial", 16, "bold"), bg="#A0E4E4").place(relx=0.5, rely=0.5, anchor="center")

# Main Container Frame
main_frame = tk.Frame(root, bg="#E0E0E0", padx=40, pady=20)
main_frame.pack(fill="both", expand=True)

# List Label dan Entry (Helper function untuk kerapihan)
def create_field(parent, label_text):
    tk.Label(parent, text=label_text, bg="#E0E0E0", font=("Arial", 10)).pack(anchor="w", pady=(10, 0))
    entry = tk.Entry(parent, font=("Arial", 10))
    entry.pack(fill="x", pady=2)
    return entry

entry_nama = create_field(main_frame, "Nama Lengkap")
entry_tgl = create_field(main_frame, "Tanggal Lahir")
entry_asal = create_field(main_frame, "Asal Sekolah")
entry_nisn = create_field(main_frame, "NISN")
entry_ayah = create_field(main_frame, "Nama Ayah")
entry_ibu = create_field(main_frame, "Nama Ibu")
entry_telp = create_field(main_frame, "Nomor Telepon / HP")

# Alamat (Menggunakan widget Text karena lebih besar)
tk.Label(main_frame, text="Alamat", bg="#E0E0E0", font=("Arial", 10)).pack(anchor="w", pady=(10, 0))
text_alamat = tk.Text(main_frame, height=5, font=("Arial", 10))
text_alamat.pack(fill="x", pady=2)

# Footer Frame untuk Tombol
footer_frame = tk.Frame(root, bg="#A0E4E4", height=50)
footer_frame.pack(fill="x", side="bottom")

btn_simpan = tk.Button(footer_frame, text="Simpan", bg="#D35400", fg="white", width=10, command=simpan_data)
btn_simpan.pack(side="right", padx=10, pady=10)

btn_hapus = tk.Button(footer_frame, text="Hapus", bg="#D35400", fg="white", width=10, command=hapus_data)
btn_hapus.pack(side="right", padx=10, pady=10)

root.mainloop()