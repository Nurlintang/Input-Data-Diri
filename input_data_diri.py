import customtkinter as ctk
from tkinter import *
from customtkinter import *
import sqlite3 as sql


def show_page1():
    page2_frame.pack_forget()
    page1_frame.pack(fill="both", expand=True)

def show_page2():
    page1_frame.pack_forget()
    page2_frame.pack(fill="both", expand=True)

def submit_data():
    global nama, nim, peminatan, alamat, jenis_kelamin
    
    nama = entry_nama.get()
    nim = entry_nim.get()
    peminatan = peminatan_var.get()
    alamat = entry_alamat.get()
    jenis_kelamin = jenis_kelamin_var.get()

    result_label.configure(text=f"Nama: {nama}\nNIM: {nim}\nPeminatan: {peminatan}\nAlamat: {alamat}\nJenis Kelamin: {jenis_kelamin}")
    show_page2()

def submit_database():
    global nama, nim, peminatan, alamat, jenis_kelamin

    koneksi = sql.connect('C:\Teknik Industri\Lintang\database_dss.db') # Disesuaikan dengan file di komputer anda
    cursor = koneksi.cursor()
    cursor.execute ('''CREATE TABLE IF NOT EXISTS dss_21 (
    nama TEXT,
    nim CHAR,
    peminatan CHAR,
    alamat CHAR,
    jenis_kelamin CHAR
    )''')

    cursor.execute(f'''INSERT INTO dss_21 (nama, nim, peminatan, alamat, jenis_kelamin)
                    VALUES ('{nama}','{nim}','{peminatan}','{alamat}','{jenis_kelamin}')''')

    koneksi.commit()
    koneksi.close()
    show_page2()

# Inisialisasi aplikasi
app = ctk.CTk()
app.title("Form Input Data Diri Mahasiswa")
app.geometry("400x500")
ctk.set_appearance_mode("light")

# Halaman 1
page1_frame = ctk.CTkFrame(app)

# Input Nama Mahasiswa
ctk.CTkLabel(master=page1_frame, text="Nama Mahasiswa").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nama = ctk.CTkEntry(master=page1_frame)
entry_nama.grid(row=0, column=1, padx=10, pady=5, sticky="e")

# Input NIM Mahasiswa
ctk.CTkLabel(master=page1_frame, text="NIM Mahasiswa").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nim = ctk.CTkEntry(master=page1_frame)
entry_nim.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# Input Fokus Peminatan Mahasiswa
ctk.CTkLabel(master=page1_frame, text="Fokus Peminatan").grid(row=2, column=0, padx=10, pady=5, sticky="w")
peminatan_var = ctk.StringVar(value="Pilih Peminatan")
peminatan_optionmenu = ctk.CTkOptionMenu(master=page1_frame, variable=peminatan_var, values=["Sistem Informasi", "Teknologi Informasi", "Teknik Informatika"])
peminatan_optionmenu.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Input Alamat Mahasiswa
ctk.CTkLabel(master=page1_frame, text="Alamat Mahasiswa").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_alamat = ctk.CTkEntry(master=page1_frame)
entry_alamat.grid(row=3, column=1, padx=10, pady=5, sticky="e")

# Input Jenis Kelamin
ctk.CTkLabel(master=page1_frame, text="Jenis Kelamin").grid(row=4, column=0, padx=10, pady=5, sticky="w")
jenis_kelamin_var = ctk.StringVar()
radio_laki = ctk.CTkRadioButton(master=page1_frame, text="Laki-Laki", variable=jenis_kelamin_var, value="Laki-Laki")
radio_perempuan = ctk.CTkRadioButton(master=page1_frame, text="Perempuan", variable=jenis_kelamin_var, value="Perempuan")
radio_laki.grid(row=4, column=1, padx=10, pady=5, sticky="w")
radio_perempuan.grid(row=4, column=2, padx=10, pady=5, sticky="e")

# Tombol Submit
submit_button = ctk.CTkButton(page1_frame, text="Submit", command=submit_data)
submit_button.grid(row=5, column=0, columnspan=3, pady=20)

# Halaman 2
page2_frame = ctk.CTkFrame(app)
page2_label = ctk.CTkLabel(page2_frame, text="Data Mahasiswa")
page2_label.pack(pady=10)
result_label = ctk.CTkLabel(page2_frame, text="")
result_label.pack(pady=10)
page2_button = ctk.CTkButton(page2_frame, text="Kembali ke Halaman 1", command=show_page1)
page2_button.pack(pady=20)
tombol_kirimdb = ctk.CTkButton(page2_frame, text="Kirim data ke database", command=submit_database)
tombol_kirimdb.pack(pady=20)

# Tampilkan halaman 1 saat aplikasi dimulai
show_page1()

# Menjalankan aplikasi
app.mainloop()
