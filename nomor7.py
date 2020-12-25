#menampilkan data yang sudah diubah kode asciinya
#Pergeseran ke kiri

myFile = open("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/textCode.txt")

i = 0
n = int(input("Banyak pergesaran = "))

textCode = open("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/textAsli2.txt", "w+")

#proses pengubahan huruf
for line in myFile:  
   for huruf in line: 
        a = ord(huruf)
        c = a - n
        if a == 32:
            c = a
        #jika kode ascii tidak pada rentan angka alfabet
        elif c <= 65:
            c += 26
            if c > 90:
                c = 64 + (c - 90)
        b = chr(c)
        textCode.write(b)
        i += 1
textCode.close()