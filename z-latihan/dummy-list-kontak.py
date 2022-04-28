dictx = {} #inisiasi dictionary

while True: #inisiasi looping do-while
    nm = input(f"Masukkan nama : ") #inisiasi variabel input nama
    al = input(f"Masukkan alamat : ") #inisiasi variabel input alamat
    dictx[nm] = al #menambahkan keys & values di dictionary
    tanya = input(f"mau memasukkan data lagi? (jawab dengan 'yes' atau 'no') : ") #inisiasi pertanyaan
    if tanya == 'no': #inisiasi if-else, jika pertanyaan dijawab dengan 'no'
        print(f"Daftar Kontak") #mencetak kalimat
        for x in dictx: #inisiasi looping for, dimana untuk setiap var x di dictionary dictx akan dilakukan,
            print(f"Nama: ",x) #mencetak nama dimana variabel x adalah key pada dictx
            print(f"Alamat: ", dictx[x]) #mencetak alamat dimana variabel dict[x] adalah values pada dictx
            print() 
        break #akan dilakukan break

