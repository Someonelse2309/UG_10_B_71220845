print ("Alat penghitung volume bangun ruang")
print ("")
print ("Silahkan Pilih Bidang ruang apa yang mau dihitung")
print ("1. Limas")
print ("2. Bola")
print ("3. Prisma")
print ("4. Kerucut")
print ("")
pil1 = int(input(">> "))
if pil1 == 1:
    print ("")
    print ("masukan dalam satuan cm")
    SisiLimas = int(input("Masukan Sisi Alas Limas >> "))
    TinggiLimas = int(input("Masukan Tinggi Limas >> "))
    VolumLimas = ((TinggiLimas * SisiLimas * SisiLimas)/3)
    print ("Volume Limas Anda ", VolumLimas , " cm^3")
elif pil1 == 2:
    print ("")
    print ("masukan dalam satuan cm")
    Rusuk = int(input("Masukan Jari-Jari Bola >> "))
    VolumBola = (4/3*(3.14*(Rusuk*Rusuk*Rusuk)))
    print ("Volume Bola Anda ", VolumBola , " cm^3")
elif pil1 == 3:
    print ("")
    print ("Silahkan Pilih Bidang ruang apa yang mau dihitung")
    print ("1. Prisma Segitiga")
    print ("2. Prisma Segiempat")
    print ("3. Prisma Segilima")
    print ("")
    pil2 = int(input(">> "))
    if pil2 == 1:
        print ("")
        print ("masukan dalam satuan cm")
        SisiAlasPrisma = int(input("Masukan Sisi Alas Prisma Segitiga >> "))
        TinggiAlasPrisma = int(input("Masukan Tinggi Alas Prisma Segitiga >> "))
        TinggiPrisma = int(input("Masukan Tinggi Prisma Segitiga >> "))
        VolumePrisma = ((1/2 * SisiAlasPrisma * TinggiAlasPrisma)* TinggiPrisma)
        print ("Volume Prisma Segitiga Anda ", VolumePrisma , " cm^3")
    elif pil2 == 2:
        print ("")
        print ("masukan dalam satuan cm")
        SisiAlasPrisma = int(input("Masukan Sisi Alas Prisma Segiempat >> "))
        TinggiAlasPrisma = int(input("Masukan Tinggi Alas Prisma Segitiga >> "))
        TinggiPrisma = int(input("Masukan Tinggi Prisma Segiempat >> "))
        VolumePrisma = ((SisiAlasPrisma * TinggiAlasPrisma)*TinggiPrisma)
        print ("Volume Prisma Segiempat Anda ", VolumePrisma , " cm^3")
    elif pil2 == 3:
        SisiAlasPrisma = int(input("Masukan Sisi Alas Prisma Segilima >> "))
        TinggiAlasPrisma = int(input("Masukan Tinggi Alas Prisma Segilima >> "))
        TinggiPrisma = int(input("Masukan Tinggi Prisma Segilima >> "))
        VolumePrisma = (((5 * TinggiAlasPrisma * SisiAlasPrisma)/2)*TinggiPrisma )
        print ("Volume Prisma Segilima Anda ", VolumePrisma , " cm^3")
    else:
        print ("Prisma yang anda cari belum terdaftar di kalkulator ini")
elif pil1 == 4 :
    print ("")
    print ("masukan dalam satuan cm")
    Rusuk = int(input("Masukan Jari-Jari Alas >> "))
    TinggiKerucut = int(input("Masukan Tinggi Kerucut >> "))
    VolumKerucut = (1/3*(3.14*(Rusuk*Rusuk))*TinggiKerucut)
    print ("Volume Bola Anda ", VolumKerucut , " cm^3")
else
    print("Maaf Bangun Luas Yang Anda Cari Belum Tersedia")
