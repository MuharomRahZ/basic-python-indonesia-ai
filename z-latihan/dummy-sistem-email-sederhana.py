receiver = {}

while True:
    print("===Selamat Datang di email!===")
    receiver_name = input(f"Silakan masukkan nama penerima : ")
    receiver_email = input(f"Silakan masukkan email penerima : ")
    subjek = input(f"Silakan tulis subjek email : ")    
    isi = input(f"Silakan tulis isi pesan email : ")
    receiver[receiver_name] = receiver_email
    ask = input(f"Mau memasukkan alamat receiver email lagi? (jawab dengan 'yes' atau 'no') : ")
    if ask == 'no':
        print("===POS KOTAK EMAIL===")
        for x in receiver:
            print(f"Subjek: ",subjek)
            print(f"Isi pesan email : ")
            print(f"Dear", x, ", email - ", receiver[x])
            print(isi)
            print()
        break