#SOAL - 3
#Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. 
#Program menerima input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal.

#RULES
#1. Jika nilai ujian teori dan praktek minimal 70,  maka program akan menampilkan:
# "Selamat, anda lulus!"

#2. Jika nilai ujian teori minimal 70 dan nilai ujian praktek kurang dari 70:
# "Anda harus mengulang ujian praktek."

#3. Jika nilai ujian teori kurang dari 70 dan nilai ujian praktek minimal 70:
# "Anda harus mengulang ujian teori."

#4. Jika nilai ujian teori dan ujian praktek kurang dari 70:
# "Anda harus mengulang ujian teori dan praktek."

#JAWAB
x = input(f"Masukkan Nilai Ujian Teori Anda : ")
teori = int(x)
y = input(f"Masukkan Nilai Ujian Praktek Anda : ")
praktek = int(y)

print(f"Nilai Ujian Teori Anda: {teori}")
print(f"Nilai Ujian Praktek Anda: {praktek}")
print(f"Status Kelulusan Anda:")
if teori >= 70 and praktek >= 70:
    print(f"Selamat, anda lulus!")
elif teori >= 70 and praktek < 70:
    print(f"Anda harus mengulang ujian praktek.")
elif teori < 70 and praktek >= 70:
    print(f"Anda harus mengulang ujian teori.")
else:
    print(f"Anda harus mengulang ujian teori dan praktek.")
