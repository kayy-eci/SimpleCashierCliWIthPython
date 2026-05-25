menu = [
    ["Pecel Ayam", 15000],
    ["Pecel Lele", 15000],
    ["Nasi Goreng", 10000]
]

daftar_pesanan = []


def menu_kasir():
    print("\n==== MENU KASIR ==== ")
    print("1. Lihat Menu")
    print("2. Tambah Pesanan")
    print("3. Cetak Struk")
    print("4. Keluar")


def lihat_menu():
    print("\n==== LIST MENU ====")
    for makanan, harga_makanan in menu:
        print(f"- {makanan}: Rp {harga_makanan:,}")


def tambah_pesanan():
    print("\n==== TAMBAH PESANAN ====")
    nama_makanan = input("Masukkan nama makanan: ")
    ditemukan = False
    for makanan, harga in menu:
        if nama_makanan.lower() == makanan.lower():
            jumlah = int(input("Masukkan jumlah: "))
            subtotal = harga * jumlah
            daftar_pesanan.append([
                makanan,
                harga,
                jumlah,
                subtotal
            ])
            print(f"{makanan} berhasil ditambahkan!")
            ditemukan = True
            break
    if not ditemukan:
        print("Makanan tidak ada di menu!")


def cetak_struk():
    print("\n======= STRUK =======")
    if len(daftar_pesanan) == 0:
        print("Belum ada pesanan.")
        return
    total = 0
    for makanan, harga, jumlah, subtotal in daftar_pesanan:
        print(f"{makanan}")
        print(f"  {jumlah} x Rp {harga:,} = Rp {subtotal:,}")
        total += subtotal

    print("----------------------")
    print(f"TOTAL BAYAR : Rp {total:,}")
    print("======================")


def main():
    while True:
        menu_kasir()
        
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            lihat_menu()
        elif pilihan == "2":
            tambah_pesanan()
        elif pilihan == "3":
            cetak_struk()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi kasir sederhana!")
            break
        else:
            print("Pilihan tidak valid.")
main()