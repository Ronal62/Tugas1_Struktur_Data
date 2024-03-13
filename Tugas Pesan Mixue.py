#Struktur Data
#Kelompok 3
#Nama : Ronald Budi Abdul Wahid   #NIM :23091397142
#Nama : Muhammad Ibnu Nadhif      #NIM :23091397161
#Nama :                           #NIM :

class ItemMenu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Pesanan:
    def __init__(self, item_menu, jumlah):
        self.item_menu = item_menu
        self.jumlah = jumlah

class DaftarPesanan:
    def __init__(self):
        self.pesanan_list = []

    def tambahkan_pesanan(self, pesanan):
        self.pesanan_list.append(pesanan)

    def tampilkan_pesanan(self):
        if not self.pesanan_list:
            print("Daftar Pesanan masih Kosong")
            return

        total_harga = 0
        for pesanan in self.pesanan_list:
            harga_pesanan = pesanan.item_menu.harga * pesanan.jumlah
            print(f"{pesanan.item_menu.nama}: {pesanan.item_menu.harga} x {pesanan.jumlah} = Rp{harga_pesanan}")
            total_harga += harga_pesanan

        print(f"Total Harga Pesanan: Rp{total_harga}")
        return total_harga

# Daftar menu
menu = [
    ItemMenu("Mixue Ice Cream", 5000),
    ItemMenu("Boba Shake", 16000),
    ItemMenu("Mi Gacoan", 14000),
    ItemMenu("Mi Ganas", 11000),
    ItemMenu("Creamy Mango Boba", 22000)
]

def tampilkan_menu():
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item.nama}: {item.harga}")

# Inisialisasi DaftarPesanan
daftar_pesanan = DaftarPesanan()

# Tampilkan menu
tampilkan_menu()

while True:
    pesanan_index = input("Silahkan memesan dari menu (input nomor atau ketik 'done' Untuk Check Out): ")
    
    if pesanan_index.lower() == "done":
        break

    try:
        pesanan_index = int(pesanan_index)
        if 1 <= pesanan_index <= len(menu):
            jumlah_pesanan = int(input("Jumlah pesanan: "))
            pesanan = Pesanan(menu[pesanan_index - 1], jumlah_pesanan)
            daftar_pesanan.tambahkan_pesanan(pesanan)
            print("Item telah dimasukkan ke keranjang")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
    except ValueError:
        print("Input tidak valid, silakan coba lagi.")

# Tampilkan daftar pesanan
total_harga_pesanan = daftar_pesanan.tampilkan_pesanan()

# Pembayaran
while True:
    uang_pembayaran = int(input(f"Total Pembayaran: Rp{total_harga_pesanan}\nMasukkan jumlah uang: "))
    if uang_pembayaran >= total_harga_pesanan:
        kembalian = uang_pembayaran - total_harga_pesanan
        print(f"Terima kasih! Pembayaran berhasil.\nKembalian Anda: Rp{kembalian}")
        break
    else:
        print("Jumlah uang tidak mencukupi. Silakan coba lagi.")
