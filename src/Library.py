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
        self._fiyat=yeni_fiyat
    
    

