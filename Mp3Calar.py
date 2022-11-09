import random
class MP3calar():
    sarkilar = []
    ses = 5
    CalanSarki = ""
    def __init__(self , Sarkilist = []):
        self.sarkilar = Sarkilist
    def sarkiSec(self , secSarki):
        if(sarkilar.__contains__(secSarki)):
            self.CalanSarki = secSarki
        else:
            print("Girdiğiniz şarkı listede yoktur")
    def sesArtir(self):
        if self.ses>=10:
            print("Ses max düzeyde")
        else:
            self.ses += 1
            print("Ses artırıldı")
    def sesAzalt(self):
        if self.ses<=0:
            print("Ses min düzeyde")
        else:
            self.ses-=1
            print("Ses azaltıldı")
    def rastgeleSec(self):
        ##bu fonksiyonu dene
        self.CalanSarki = str(sarkilar[random.randint(1,len(sarkilar))])
    def sarkiEkle(self , ekSarki):
        sarkilar.append(ekSarki)
    def sarkiSil(self , silSarki):
        if self.sarkilar.__contains__(silSarki):
            self.sarkilar.remove(silSarki)
        else:
            print("Girdiğiniz şarkı listede bulunmamaktadır")
    def kapat(self):
        print("MP3 kapatıldı , iyi günler")
    def menuYazdir(self):
        print("1- Şarkı seç\n2- Ses Artir\n3- Ses azalt\n4- Rastgele şarkı seç\n5- Şarkı Ekle\n6- Şarkı Sil\n7- Çıkış Yap")
    def sarkilariGoster(self):
        print(self.sarkilar)

sarkilar = ["Hümanın uykusu gelmiş" , "Bana bir masal anlat baba" , "Unstoppable" , "I love U" , "Alan Walker" , "Deneme"]
mp3 = MP3calar(sarkilar)
while True:
    print(f"Çalan Şarkı {mp3.CalanSarki} , Ses düzeyi {mp3.ses}")
    mp3.sarkilariGoster()
    mp3.menuYazdir()
    secim = int(input("Seçiminizi giriniz : "))
    if secim == 1:
        calacakSarki = input("Çalacak şarkınızı seçiniz : ")
        mp3.sarkiSec(calacakSarki)
    elif secim == 2:
        mp3.sesArtir()
    elif secim == 3:
        mp3.sesAzalt()
    elif secim == 4:
        mp3.rastgeleSec()
    elif secim == 5:
        ekleSarki = input("Eklenecek şarkıyı giriniz : ")
        mp3.sarkiEkle(ekleSarki)
    elif secim == 6:
        silSarki = input("Silinecek şarkıyı giriniz : ")
        mp3.sarkiSil(silSarki)
    elif secim == 7:
        mp3.kapat()
        break
    else:
        print("Yanlış seçim yaptınız tekrar deneyiniz")

