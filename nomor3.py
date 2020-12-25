#Menampilkan data pada file yang sebelumnya di buat dalam sebuah dictionari

myfile = open('e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/dataMhs.txt', 'r')

#membaca file berdasarkan baris
file_lines=myfile.readlines()

dataMhs = {}
a = ('')

#function untuk memanggil data
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

print("dataMhs = {", end="")  

i = 0
#perulangan untuk penulisan data
while i < 3:
    file = file_lines[i].strip()
    inputData(a, dataMhs, file)
    if i == 2:
        print(dataMhs, end="")
    else:
        print(dataMhs, ",", end="" )
    i += 1
print("}")