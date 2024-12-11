class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembang_biak
        
    def cetak(self):
        print(f"nama \t\t\t\t:", self.nama,
              "\nmakanan \t\t\t:", self.makanan,
              "\nHidup \t\t\t\t:", self.hidup,
              "\nberkembang biak\t\t\t:", self.berkembangbiak)
        
buaya = Animal("buaya", "daging", "Amphibi", "bertelur")
# buaya.cetak()

