#!/usr/bin/env python
#-*- coding: iso-8859-9
dosya = open("�iir.txt", "w")
dosya.write("B�t�n g�ne�ler batmadan,\nBi t�rk� daha s�yleyeyim bu yerde\n\t\t\t\t --Orhan Veli--")
dosya.close()

with open("�iir.txt", "r") as dosya:
 a=dosya.read()
 print a

 #dosyay� basa sarma
 dosya.seek(0)
 b=dosya.read()
 print b
 
#dosyan�n bas�na ver� ekleme
with open("�iir.txt", "r+") as f:
    veri = f.read()
    f.seek(0)
    f.write("Selin �zden\t: 0212 222 22 22\n"+veri)

 
#ortaya veya herhang� b�r yere ekleme
with open("�iir.txt", "r+") as f:
     veri = f.readlines()
     veri.insert(2, "Sedat K�z\t: 0322 234 45 45\n")
     f.seek(0)
     f.writelines(veri)


