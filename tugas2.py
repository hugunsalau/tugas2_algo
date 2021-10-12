total = int(input("Masukkan total harga belanjaan Anda: Rp. "))
bayar = int(input("Masukkan jumlah uang Anda: Rp. "))
kembalian = bayar - total
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
sisa = kembalian
print("\nKembalian Anda sejumlah: Rp.", kembalian, "\nPecahan uang yang dibutuhkan: ")
for pecahan in uang_pecahan:
    if sisa < pecahan:
        continue
  
