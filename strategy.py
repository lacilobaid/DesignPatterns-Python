# oklid uzakligi:  De(p, q) = [(x-s)2 + (y-t)2]1/2
# sehir-blok uzakligi: D4(p, q) = |x-s| + |y-t|
# satranc tahtasi uzakligi: D8(p, q) = max(|x-s|, |y-t|)
import time
from abc import ABCMeta,abstractmethod

class yol_stratejisi(metaclass=ABCMeta):

    @abstractmethod
    def kullan(self,x,y,s,t): pass


class oklid_stratejisi(yol_stratejisi):

    def __str__(self):

        return 'Oklid Uzakligi Stratejisi'

    def kullan(self,x,y,s,t):

        return round(((((x-s)**2) + (y-t)**2)**(1/2)),3)


class sehir_blok_stratejisi(yol_stratejisi):
    
    def __str__(self):

        return 'Sehir-Blok Stratejisi'

    def kullan(self,x,y,s,t):

        return abs(x-s) + abs(y-t)

class satranc_tahtasi_stratejisi(yol_stratejisi):
    
    def __str__(self):

        return 'Satranc Tahtasi Stratejisi'

    def kullan(self,x,y,s,t):

        return max(abs(x-s),abs(y-t))


class yolcu:

    def __init__(self,suan_x,suan_y,gidilecek_s,gidilecek_t):
        self.suan_x=suan_x
        self.suan_y=suan_y
        self.gidilecek_s=gidilecek_s
        self.gidilecek_t=gidilecek_t

        self.oklid = oklid_stratejisi()
        self.satranc = satranc_tahtasi_stratejisi()
        self.sehir_blok = sehir_blok_stratejisi()

        self.strnc_str = satranc_tahtasi_stratejisi().kullan(suan_x, suan_y, gidilecek_s, gidilecek_t)
        self.shrblk_str = sehir_blok_stratejisi().kullan(suan_x, suan_y,gidilecek_s,gidilecek_t)
        self.oklid_str = oklid_stratejisi().kullan(suan_x, suan_y, gidilecek_s,gidilecek_t)

    def koordinat_yazdir(self):
        
        print('----------------------------')
        
        print (f'Bulunulan koordinat: ({self.suan_x},{self.suan_y})\nGidilecek koordinat: ({self.gidilecek_s},{self.gidilecek_t})')

    def sec(self):

        print('*****************************')
        
        time.sleep(2)
        
        print("Guzergah seciminiz Oklid Uzakligi Stratejisine gore secilirse gidilecek mesafe:", self.oklid_str, " KM'dir.")
        
        time.sleep(2)
        
        print("Guzergah seciminiz Satranc Tahtasi Stratejisine gore secilirse gidilecek mesafe:", self.strnc_str, " KM'dir.")
        
        time.sleep(2)
        
        print("Guzergah seciminiz Sehir-Blok Stratejisine gore secilirse gidilecek mesafe:", self.shrblk_str, " KM'dir.")
        
    def onerilen(self):
        
        print('----------------------------')
        
        time.sleep(3)
        
        if self.strnc_str==self.oklid_str==self.shrblk_str:
            
            print('Butun stratejiler aynidir.')
            
        elif min(self.strnc_str,self.oklid_str,self.shrblk_str) == self.strnc_str:
            
            print('Onerilen strateji:', self.satranc)
            
        elif min(self.strnc_str,self.oklid_str,self.shrblk_str) == self.oklid_str:
            
            print('Onerilen strateji:', self.oklid)
            
        else:
            
            print('Onerilen strateji:', self.sehir_blok)


if __name__ == '__main__':
    
    x = int(input('Bulunulan x koordinat giriniz: '))
    y = int( input('Bulunulan y koordinat giriniz: '))
    s = int(input('Gidilecek s koordinati giriniz: '))
    t = int(input('Gidilecek t koordinati giriniz: '))
    
    yolcu = yolcu(x,y,s,t)
    yolcu.koordinat_yazdir()
    yolcu.sec()
    yolcu.onerilen()
