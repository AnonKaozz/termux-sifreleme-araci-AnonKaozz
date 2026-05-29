print("--- HACKER ANA MENÜ ---")
print("1. Mesaj Şifrele")
print("2. Şifreli Mesajı Çöz")

secim = input("Seçimini yap (1/2): ")

if secim == '1':
    mesaj = input("Şifrelenecek mesaj: ")
    print("Şifreli hali:", sifrele(mesaj, 3))
elif secim == '2':
    mesaj = input("Çözülecek mesaj: ")
    print("Çözülmüş hali:", coz(mesaj, 3))
else:
    print("Geçersiz seçim!")
  
