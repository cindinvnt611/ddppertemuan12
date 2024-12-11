from animal import *

class lumba_lumba(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        
    def cetak_lumba_lumba(self):
        super().cetak()
        print(f"Design \t\t\t\t:", self.warna)
        
lumba = lumba_lumba("Lumba-Lumba", "Ikan kecil", "Laut", "Melahirkan", "Abu-abu")
lumba.cetak_lumba_lumba()