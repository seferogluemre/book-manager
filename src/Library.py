class Kitap:
    def __init__(self,ad,yazar,fiyat):
        self._ad=ad
        self._yazar=yazar
        self._fiyat=fiyat
    
    # Getter
    def get_ad(self):
        return self._ad
    def get_yazar(self):
        return self._yazar
    def get_fiyat(self):
        return self._fiyat
    
    # Setter
    def set_ad(self,yeni_ad):
        self._ad=yeni_ad
    def set_yazar(self,yeni_yazar):
        self._yazar=yeni_yazar
    def set_fiyat(self,yeni_fiyat):
        if yeni_fiyat >0:
            self._fiyat=yeni_fiyat
        else :
            print("Fiyat negatif Olamaz. Tekrar deneyiniz")
    
    # Polymorphism için temel bilgi gösterimi
    def kitap_bilgisi(self):
        return f"Kitap: {self._ad},\n Yazarı: {self._yazar}, \n Fiyatı: {self._fiyat}"

class Roman (Kitap):
    def __init__(self,ad,yazar,fiyat,tur):
        super().__init__(ad,yazar,fiyat)
        self.tur=tur

    def kitap_bilgisi(self):
        return f"Roman: {self.get_ad()}, Tür: {self.tur}, Yazar: {self.get_yazar()}, Fiyat: {self.get_fiyat()} TL"

class DersKitabi(Kitap):
    def __init__(self, ad, yazar, fiyat, konu):
        super().__init__(ad, yazar, fiyat)
        self.konu = konu
    
    # Polymorphism (Başka bir türde bilgi formatı)
    def kitap_bilgisi(self):
        return f"Ders Kitabı: {self.get_ad()}, Konu: {self.konu}, Yazar: {self.get_yazar()}, Fiyat: {self.get_fiyat()} TL"

    
class KitapYönetim:
    def __init__(self):
        self.kitaplar=[]

    def kitap_ekle(self,kitap):
        self.kitaplar.append(kitap)
         print(f"{kitap.get_ad()} adlı kitap başarıyla eklendi.")

    def kitap_listeleme(self):
        if not self.kitaplar:
            print("Sistemde kitap bulunmamaktadır.")
        else:
            for Kitap in self.kitaplar:
                print(Kitap.kitap_bilgisi())

    def kitap_silme(self,kitap_adi):
        for kitap in self.kitaplar:
            if kitap.get_ad() == kitap_adi:
                self.kitaplar.remove(kitap)
                 print(f"{kitap_adi} adlı kitap başarıyla silindi.")
                return

       print(f"{kitap_adi} adlı kitap bulunamadı.")

# Tests
yonetim = KitapYonetim()

roman1 = Roman("Sefiller", "Victor Hugo", 45, "Klasik")
ders_kitabi1 = DersKitabi("Matematik Analiz", "Ali Veli", 60, "Matematik")

yonetim.kitap_ekle(roman1)
yonetim.kitap_ekle(ders_kitabi1)

print("\nKitap Listesi:")
yonetim.kitaplari_listele()

yonetim.kitap_sil("Sefiller")

print("\nGüncel Kitap Listesi:")
yonetim.kitaplari_listele()