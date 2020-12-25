#Melakukan penjumlahan data pada file yang sudah di buat

open_file=open("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/bahanPenjumlahan.txt", "r")
file_lines=open_file.readlines()
a = 0

print("Hasil Penjumlahan")

#perulangan untuk menjumlahkan data
while a < 4:
    file = file_lines[a].strip()
    b = file[0] + file[1]
    c = file[3] + file[4]
    print("Bari ke-", a, "=", int(b) + int(c))
    a += 1