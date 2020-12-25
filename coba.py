myfile = open('e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/dataMhs.txt', "a+")
i = 0
def inputData():
    nim = input("Masukkan NIM : ")
    nama = input("Masukkan Nama Mhs :")
    alamat = input("Masukkan Alamat : ")
    myfile.write(nim + "|" + nama + "|" + alamat + '\n')
    ulangi = input("Ulangi input lagi (y/n) :")
    if ulangi == "y" or ulangi == "Y":
        inputData()

inputData()