liste = ["elma", "armut", "karpuz", "kavun", "erik", "�z�m", "�eftali", "muz"]
while True:
    try:
       s = raw_input("L�tfen bir meyve ad� s�yleyiniz: ")
       p = liste.index(s) + 1
       print s, "listemizde", p, "no'lu s�rada bulunuyor"
    except ValueError:
       pass
