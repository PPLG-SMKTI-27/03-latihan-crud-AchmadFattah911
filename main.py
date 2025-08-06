# data buku
from tabulate import tabulate

books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":None},
]

def tampilkan_data():
    print(tabulate(books, headers='keys', tablefmt='psql'))
def tambah_data():
    print("Menambahkan data")
    isbn = input("Masukkan isbn :")
    judul = input("Masukkan nama Judul Buku : ")
    pengarang = input("Masukkan Nama Pengarang :")
    jumlah = int(input("Masukkan Jumlah Buku : "))
    terpinjambuku = 0
    item = {"isbn" : isbn , "judul": judul ,"pengarang": pengarang,"jumlah": jumlah,"terpinjam": terpinjambuku}
    books.append(item)
    print("berhasil di tambahkan")

def edit_data():
    ganti = int(input("Massukkan nomor buku yang ingin di ubah :"))
    books[ganti]["isbn"] = input("Masukkan Isbn baru :")
    books[ganti]["judul"] = input("Masukkan judul baru :")
    books[ganti]["pengarang"] = input("Masukkan pengarang baru :")
    books[ganti]["jumlah"] = int(input("Masukkan jumlah baru :"))
    books[ganti]["terpinjam"] = int(input("Masukkan terpinjam baru :"))

def hapus_data():
    hapusdata = int(input("Masukkan nomor buku yang ingon dihapus:"))
    books.pop(hapusdata)

def tampilkan_peminjaman():
    print(tabulate(records, headers='keys', tablefmt='psql'))

def tampilkan_belum():
    print(tabulate([records for records in records if records["tanggal_kembali"] is None] , headers='keys', tablefmt='psql'))

def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for book in books:
        if book['isbn'] == isbn:
            if book['jumlah'] > book['terpinjam']:
                book['terpinjam'] += 1
                records.append({"isbn": isbn, "status": "Belum", "tanggal_pinjam": "2025-03-21", "tanggal_kembali": ""})
                print("Buku berhasil dipinjam.")
            else:
                print("Buku sudah habis dipinjam.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
    balik_buku = input("tanggal buku pas mau di kembalikan:")
    for book in books:
        if book['isbn'] == isbn:
            if book['terpinjam'] > 0:
                book['terpinjam'] -= 1
                for record in records:
                    if record['isbn'] == isbn and record['status'] == "Belum":
                        record['status'] = "Selesai"
                        record['tanggal_kembali'] = balik_buku
                        break
                print("Buku berhasil dikembalikan.")
            else:
                print("Buku ini tidak sedang dipinjam.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")


while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    
    status = True
    match menu:
        case "1":
            tampilkan_data()
            
        case "2":
            tambah_data()
            
        case "3":
            edit_data()
            
        case "4":
            hapus_data
        
        case "5":
            tampilkan_peminjaman()
        
        case "6":
            tampilkan_belum()
        
        case "7":
            peminjaman()
        
        case "8":
            pengembalian()
            
        case "x"|"X":
            status = False
        