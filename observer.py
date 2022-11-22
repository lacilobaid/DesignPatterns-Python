import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from win10toast import ToastNotifier

class selenium_baglan:

        kurlar = []
        kurlar2 = []
        browser_firefox = webdriver.FirefoxOptions()
        browser_firefox.headless = True
        browser = webdriver.Firefox(executable_path=r'C:\pythonProject\venv\Scripts\geckodriver.exe', options=browser_firefox)
        url = "https://www.foreks.com/kripto/"
        browser.get(url)
        for i in range(1, 6):
                div = browser.find_element(By.CSS_SELECTOR,"#definitionsTable > tr:nth-child(" + str(i) + ") > td:nth-child(2) > div")
                div2 = browser.find_element(By.CSS_SELECTOR, "#definitionsTable > tr:nth-child(" + str(i) + ") > td:nth-child(1) > div > a > span:nth-child(3) > span")
                kurlar.append(div.text)
                kurlar2.append(div2.text)


class veri_Foreks:
    kripto_fiyat= set()
    def ekle(self,fiyat):
        self.kripto_fiyat.add(fiyat)
    def bilgi(self,mesaj,ad):
        for i in self.kripto_fiyat:
            i.bilgi_yazdir(mesaj,ad)

class observer:
    bildirim = ToastNotifier()
    def bilgi_yazdir(self,mesaj,ad):
        self.bildirim.show_toast(title=ad, msg= mesaj, duration=5)

if __name__ == '__main__':
    baglan = selenium_baglan()
    foreks = veri_Foreks()
    os = observer()
    foreks.ekle(os)
    for i in range(0, len(baglan.kurlar)):
        foreks.bilgi(baglan.kurlar[i], baglan.kurlar2[i])
    baglan.browser.close()

#*********************************************************

from win10toast import ToastNotifier
import time


class Twitter(object):
    twit = set()
    def ekle(self, twit, ):
        self.twit.add(twit)
    def bilgilendir(self, mesaj):
        for tw in self.twit:
            tw.bildirim_gonder(mesaj)


class Twitter_giris():
    kullanici_adi = 'sgoktas'
    sifre = '123'
    def giris(self):
        print('** Giris **')
        while True:
            inp_kullanici_adi = input('Kullanici adi: ')
            inp_sifre = input('Sifre: ')
            if inp_kullanici_adi == self.kullanici_adi and inp_sifre == self.sifre:
                print('Giris basarili....')
                return True
            else:
                print('Hatali sifre/kullanici adi.')

class Observer():
    bildirim = ToastNotifier()
    def __init__(self, isim):
        self.isim = isim
    def bildirim_gonder(self, mesaj):
        self.bildirim.show_toast(title='Twitter', msg=self.isim + ' tweetledi!\n' + "'" + mesaj + "'",
                                 icon_path=None, duration=5)

if __name__ == '__main__':
    giris_ = Twitter_giris()
    giris_.giris()
    twitter = Twitter()
    atilanTwit = input("Tweet: ")
    os = Observer(giris_.kullanici_adi)
    twitter.ekle(os)
    print('Tweet gonderme basarili...')
    time.sleep(2)
    twitter.bilgilendir(atilanTwit)


