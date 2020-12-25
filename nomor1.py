#Mengihtung jumlah bilangan genap dan ganjil pada suatu file
myfile = open('e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter10/dataBilangan.txt')

a = list(myfile)
#mengubah data pada file menjadi integer
aInteger = [int(i) for i in a]
c = 0
d = 0
e = 0
#mengitung banyak bilangan genap dan ganjil
while c < len(aInteger):
    if aInteger[c] % 2 == 0:
        d += 1
    if aInteger[c] % 2 == 1:
        e += 1
    c += 1

print("Banyaknya bilangan genap : ", d)
print("Banyaknya bilangan ganjil : ", e)