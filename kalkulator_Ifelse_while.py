on = True
total = 0
while on :
    button = True
    print("Pilih operasi yang mau digunakan")
    print("1.Pertambahan")
    print("2.Pengurangan")
    print("3.perkalian")
    print("4.Pembagian")
    print("5.Reset angka")
    pil = int(input("Masukan angka yang sesuai untuk memilih operasi : "))
    if pil == 1:
        while button:
            angka = float(input("Masukan angka (0 untuk keluar ): "))
            if angka == 0:
                button=False
                break
            elif angka !=0:
                total+=angka
    if pil == 2 :
        while button:
            angka = float(input("Masukan angka (0 untuk keluar ): "))
            if angka == 0:
                button=False
                break
            angka1 = float(input("Masukan angka (0 untuk keluar ): "))
            if angka1 == 0:
                total-=angka
                button = False
                break
            elif total==0:
                total=angka-angka1
            elif total>0:
                total-=angka
                total-=angka1
    if pil == 3 :
        while button:
            angka = float(input("Masukan angka (0 untuk keluar ): "))
            if angka == 0:
                button=False
                break
            angka1 = float(input("Masukan angka (0 untuk keluar ): "))
            if angka1 == 0:
                total*=angka
                button = False
                break
            elif total==0:
                total=angka*angka1
            elif total>0:
                total*=angka
                total*=angka1
    if pil == 4 : 
        while button:
            angka = float(input("Masukan angka (0 untuk keluar ): "))
            if angka == 0:
                button = False
                break
            angka1 = float(input("Masukan angka (0 untuk keluar ): "))
            if angka1==0:
                total/=angka
                button= False
                break
            elif total==0:
                total=angka/angka1
            elif total>0:
                total/=angka
                total/=angka1
    if pil == 5 :
        total=0
    print(f"total = {total}\n" )


            
