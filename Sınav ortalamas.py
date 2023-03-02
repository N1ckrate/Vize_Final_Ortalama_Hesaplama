final : int = int(input("Final notunuzu giriniz:"))
vize : int = int(input("Vize notunuzu giriniz:"))

ortalama = int(vize + final) /2

if (0 <= final <=100)and(0<= vize <=100):

   if 0 <= ortalama and ortalama <=44:
    print("Kaldınız.")
   elif 45 <= ortalama and ortalama <=69:
       print("Geçtiniz.")
   elif 70 <= ortalama and ortalama <=84:
       print("İyi")
   elif 85 <= ortalama and ortalama <=100:

       print("Çok iyi")
   print(f"ortalamanız:{ortalama}")
else:
    print("Lütfen ortalamanızın hesaplanabilmesi için geçerli bir not giriniz.")









