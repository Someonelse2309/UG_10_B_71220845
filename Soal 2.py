print ("Alat penghitung volume bangun ruang")
print ("")
bil1 = int(input("Masukan Bilangan Bulat Pertama >> "))
bil2 = int(input("Masukan Bilangan Bulat Kedua >> "))
bil3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
jmlh = ((bil1**2)+(bil2**2))
if jmlh == (bil3**2):
    print ("Ini Merupakan Phytagoras")
else:
    print ("Ini Bukan Merupakan Phytagoras")