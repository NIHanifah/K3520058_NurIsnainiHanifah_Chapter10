#Membuat file berisi data mahasiswa

myfile = open('e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/dataMhs.txt', "a+")

def inputData():
    nim = input("Masukkan NIM : ")
    nama = input("Masukkan Nama Mhs :")
    alamat = input("Masukkan Alamat : ")
    #memasukkan data
    myfile.write(nim + "|" + nama + "|" + alamat + '\n')
    #pertanyaan perulangan
    ulangi = input("Ulangi input lagi (y/n) :")
    if ulangi == "y" or ulangi == "Y":
        inputData()
    if ulangi == "n" or ulangi == "N":
        myfile.close()

inputData()
