#mencari data pada file menggunakan nim

myfile = open('e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/dataMhs.txt', 'r')

file_lines=myfile.readlines()

dataMhs = {}
a = ('')

#funtion untuk memanggil data
def inputData(a, dataMhs, file):
    for ch in file: 
        if ord(ch) != 124:
            a += ch
        if ord(ch) == 124:
            a += " "
    b = a.split()
    dataMhs['nim'] = b[0]
    dataMhs['nama'] = b[1]
    dataMhs['alamat'] = b[2]

i = 0

cari = input("Masukkan NIM yang mau di cari : ")

#perulangan untuk mengecek keberadaan data
while i < 3:
    file = file_lines[i].strip()
    inputData(a, dataMhs, file)
    if cari == dataMhs['nim']:
        print("NIM    : ", dataMhs['nim'])
        print("Nama   : ", dataMhs['nama'])
        print("Alamat : ", dataMhs['alamat'])
        break
    i += 1

if cari != dataMhs['nim']:
    print("Data tidak ditemukan")