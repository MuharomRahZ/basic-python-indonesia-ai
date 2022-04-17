#SOAL - 2
#Buatlah sebuah program yang dapat menghitung luas lingkaran.
#Program meminta input dari user berupa angka sebagai jari-jari lingkaran.
#Program menghitung luas lingkaran dengan rumus πr² 
#Π = 22/7
#r = jari - jari lingkaran 
#Lalu tampilkan ke layar dengan format:
#Hint: untuk menampilkan tanda kuadrat gunakan print(“\u00b2”)

#JAWAB
r = input("Masukkan besar jari-jari lingkaran : ")
angka = int(r)
pi = 22/7
luas_lingkaran =  pi * (angka * angka)
print("Luas lingkaran dengan jari-jari ",angka," cm adalah ", f'{luas_lingkaran:.2f}'," cm"+"\u00b2.")