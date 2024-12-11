from animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
        
    def cetak_ular(self):
        super().cetak()
        print(f"Design \t\t\t\t:", self.design,"\nRacun \t\t\t\t:", self.racun)
        
anaconda = ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik", "Tidak berbisa")
anaconda.cetak_ular()
