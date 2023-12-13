class Veritabani:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
        self.veritabani_olustur()

    def veritabani_olustur(self):
        with open(self.dosya_adi, "w") as file:
            file.write("kullanıcı1,123456\n")
            file.write("kullanıcı2,654321\n")

    def kullanici_dogrula(self, kullanici_adi, sifre):
        with open(self.dosya_adi, "r") as file:
            for line in file:
                kullanici_bilgi = line.strip().split(",")
                if kullanici_adi == kullanici_bilgi[0] and sifre == kullanici_bilgi[1]:
                    return True
            return False

    def kullanici_ekle(self, kullanici_adi, sifre):
        with open(self.dosya_adi, "a") as file:
            file.write(f"{kullanici_adi},{sifre}")

    def kullanici_listele(self):
        with open(self.dosya_adi, "r") as file:
            for sayac, line in enumerate(file, start=1):
                kullanici_bilgi = line.strip().split(",")
                print(f"{sayac}.Kullanıcı Adı: {kullanici_bilgi[0]}, Şifre: {kullanici_bilgi[1]}")


veritabani1 = Veritabani("kullanıcılar.txt")
veritabani1.kullanici_dogrula("salimu", "1923")
veritabani1.kullanici_ekle("salimu", "1234")
veritabani1.kullanici_dogrula("salimu", "1234")
veritabani1.kullanici_listele()




