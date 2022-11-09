class oyuncu1():
    ad=""
    hamle = "X"


class oyuncu2():
    ad = ""
    hamle = "O"

class Kurallar(oyuncu2 , oyuncu1):
    oyunAlanı = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    def menüYazdır(self):
        print("*** XOX Oyunumuza hoşgeldiniz ***")
        for i in range(0, 3):
            print(self.oyunAlanı[i])
    def oyuncuTanımlama(self):
        print("Oyuncu bilgilerini giriniz : ")
        oyuncu1.ad = str(input("Oyuncu1 adını giriniz : "))
        oyuncu2.ad = str(input("Oyuncu2 adını giriniz : "))

    def oyuncu1Hamle(self):
        hamleSatir = int(input("Oyuncu1 hamleniz için oyun alanından satır değerini seçiniz : "))
        hamleSutun = int(input("{oyuncu2.ad} hamleniz için oyun alanından sutün değerini seçiniz : "))
        self.oyunAlanı[hamleSatir][hamleSutun] = "X"
    def oyuncu2Hamle(self):
        hamleSatır = int(input("{oyuncu2.ad} hamleniz için oyun alanından satır değerini seçiniz : "))
        hamleSutun = int(input("{oyuncu2.ad} hamleniz için oyun alanından sutün değerini seçiniz : "))
        self.oyunAlanı[hamleSatır][hamleSutun] = oyuncu2.hamle
    def yankazanma(self):
        #Aynı satırda kazanma
        kazanan = ""
        for i in range(0,3):
            if(self.oyunAlanı[i] == [oyuncu1.hamle , oyuncu1.hamle , oyuncu1.hamle]):
                kazanan = oyuncu1.ad
            if (self.oyunAlanı[i] == [oyuncu2.hamle, oyuncu2.hamle, oyuncu2.hamle]):
                kazanan = oyuncu2.ad
        return kazanan
    def duzKazanma(self):
        # Aynı sutünda kazanma
        kazanan = ""
        sutun1 = [self.oyunAlanı[0][0], self.oyunAlanı[1][0], self.oyunAlanı[2][0]]
        sutun2 = [self.oyunAlanı[0][1], self.oyunAlanı[1][1], self.oyunAlanı[2][1]]
        sutun3 = [self.oyunAlanı[0][2], self.oyunAlanı[1][2], self.oyunAlanı[2][2]]
        if (sutun1[0] == sutun1[1] == sutun1[2] == oyuncu1.hamle):
            kazanan = oyuncu1.ad
        elif (sutun2[0] == sutun2[1] == sutun2[2] == oyuncu1.hamle):
            kazanan = oyuncu1.ad
        elif (sutun3[0] == sutun3[1] == sutun3[2] == oyuncu1.hamle):
            kazanan = oyuncu1.ad
        elif (sutun1[0] == sutun1[1] == sutun1[2] == oyuncu2.hamle):
            kazanan = oyuncu2.ad
        elif (sutun2[0] == sutun2[1] == sutun2[2] == oyuncu2.hamle):
            kazanan = oyuncu2.ad
        elif (sutun3[0] == sutun3[1] == sutun3[2] == oyuncu2.hamle):
            kazanan = oyuncu2.ad
        else: kazanan=""
        return kazanan
    def duzkazanma2(self):
        kazanan = ""
        for i in range(0,3):
            for j in range(0,3):
                if(self.oyunAlanı[j][i] == oyuncu1.hamle):
                    kazanan = oyuncu1.ad
                    break
                elif(self.oyunAlanı[j][i] == oyuncu2.hamle):
                    kazanan = oyuncu2.ad
                    break
                else: kazanan=""
        return  kazanan
    def caprazKazanma(self):
        #Capraz Kazanma
        kazanan = ""
        for i in range(0,3):
           if (self.oyunAlanı[i][i] == str(oyuncu1.hamle)):
               kazanan = oyuncu1.ad
           elif(self.oyunAlanı[i][i] == str(oyuncu2.hamle)):
               kazanan = oyuncu2.ad
           else:
               kazanan = ""
        return kazanan
    def caprazDigerKazanma(self):
        #Capraz Diğer Taraf
        kazanan = ""
        for i in range(0,3):
            for j in range(0,3):
                if(i+j==2):
                    if(self.oyunAlanı[i][j] == str(oyuncu1.hamle)):
                        kazanan = oyuncu1.ad
                    elif(self.oyunAlanı[i][j] == str(oyuncu2.hamle)):
                        kazanan = oyuncu2.ad
                    else:
                         kazanan = ""
        return kazanan




oyna = Kurallar()

kazanan = ""
oyunSırası = 9
oyna.oyuncuTanımlama()
while len(kazanan)<=0 and oyunSırası >= 0:
    oyna.menüYazdır()
    oyna.oyuncu1Hamle()
    oyna.oyuncu2Hamle()
    kazanan = oyna.caprazKazanma()
    kazanan = oyna.caprazDigerKazanma()
    kazanan = oyna.duzKazanma()
    kazanan = oyna.yankazanma()
    oyunSırası-=1
oyna.menüYazdır()
if(len(kazanan) == 0):
    kazanan = "Beraber"
print(kazanan)

