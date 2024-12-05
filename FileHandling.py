import os

def buat_file():
    nama_file = input("Masukkan nama file (tanpa ekstensi): ") + ".txt"
    nama = input("Nama Anda: ")
    nim = input("NIM Anda: ")
    tahun = input("Tahun Angkatan: ")

    with open(nama_file, 'w') as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"NIM: {nim}\n")
        file.write(f"Tahun: {tahun}\n")

    print(f"\nFile {nama_file} berhasil dibuat!\n")

def baca_file():
    nama_file = input("Masukkan nama file (tanpa ekstensi): ") + ".txt"

    if os.path.exists(nama_file):
        with open(nama_file, 'r') as file:
            print("\nIsi file:")
            print(file.read())
    else:
        print("\nFile tidak ditemukan!\n")

def edit_file():
    nama_file = input("Masukkan nama file (tanpa ekstensi): ") + ".txt"

    if os.path.exists(nama_file):
        with open(nama_file, 'a') as file:
            nama_sahabat = input("Masukkan Nama Sahabatmu: ")
            note = input("Masukkan Note Tambahan: ")
            file.write(f"Nama Sahabat: {nama_sahabat}\n")
            file.write(f"Note: {note}\n")
        print(f"\nFile {nama_file} berhasil diperbarui!\n")
    else:
        print("\nFile tidak ditemukan!\n")

def main():
    while True:
        print("----------File Handling----------")
        print("1. Membuat File Baru")
        print("2. Membaca File")
        print("3. Mengedit File")
        print("9. Keluar")

        pilihan = input("Pilihan (1/2/3/9): ")

        if pilihan == '1':
            buat_file()
        elif pilihan == '2':
            baca_file()
        elif pilihan == '3':
            edit_file()
        elif pilihan == '9':
            print("Bye Bye :3")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.\n")

if __name__ == "__main__":
    main()
