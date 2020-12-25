#Menyamarkan data melalui kode Caesar
#Pergeseran ke kanan

myFile = open("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/textAsli.txt")
i = 0

n = int(input("Banyak pergesaran = "))

textCode = open("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/textCode.txt", "w+")

#proses pengubahan huruf
for line in myFile:  
   for huruf in line: 
        a = ord(huruf)
        c = a + n
        if a == 32:
            c = a
        #jika angka ascii tidak pada rentan angka pada bilangan alfabet
        if c > 90:
            c = 64 + (c - 90)
        b = chr(c)
        textCode.write(b)
        i += 1
textCode.close()
