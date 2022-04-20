#deklarasi variabel dictionary
kontak = {
    "zaki" : "085279212056",
    "tono" : "081234567890"
}

print(f"Selamat Datang!") #menampilkan sambutan
print(f"---Menu---\n1. Daftar Kontak\n2. Tambah Kontak\n3. Keluar\n") #menampilkan pilihan menu
menu = int(input(f"Pilih Menu:")) #membuat variabel input

#memulai deklarasi if-else untuk pemilihan menu (manual switch case)
if menu == 1:
    print(f"Daftar Kontak")
    for x in kontak:
      print(f"Nama: ",x)
      print(f"No Telepon: ", kontak[x])
elif menu == 2:
    nama = input(f'Masukkan Nama: ')
    telp = input(f'Masukkan No Telepon: ')
    kontak[nama] = telp
    print(f"Kontak berhasil ditambahkan")
    print()
    print(f"Daftar Kontak")
    for x in kontak:
      print(f"Nama: ",x)
      print(f"No Telepon: ", kontak[x])
elif menu == 3:
    print(f"Program selesai, sampai jumpa!")
else:
    print(f"Menu tidak tersedia")