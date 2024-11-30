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