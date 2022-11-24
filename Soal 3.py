print ("Selamat Datang Di Program Pengurutan Bilangan")
print ("")
print ("Silahkan Pilih Metode Yang Akan Dipakai")
print ("1. Ascending")
print ("2. Descending")
print ("")
pil1 = int(input(">> "))
print ("")
bil1 = int(input("Masukan Bilangan Bulat Pertama >> "))
bil2 = int(input("Masukan Bilangan Bulat Kedua >> "))
bil3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
bil4 = int(input("Masukan Bilangan Bulat Keempat >> "))
list1 = [bil1 , bil2 , bil3 , bil4]
if pil1 == 1:
    print ("Urutan angka anda ", sorted(list1))
elif pil1 == 2:
    print ("Urutan angka anda ", sorted(list1,reverse=True))
else:
    print ("Input anda salah")
