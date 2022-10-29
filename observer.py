import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class selenium_baglan:

        kurlar = []
        kurlar2 = []
        browser = webdriver.Firefox(executable_path=r'C:\pythonProject\venv\Scripts\geckodriver.exe')
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

    def bilgi_yazdir(self,mesaj,ad): #  29 kasım 2022deki değerlere göre kosullar belirtildi
        if mesaj < "20.767":
            print(ad+" kriptosu düşmüştür: "+mesaj)
        elif mesaj > "20.767":
            print(ad+" kriptosu yükselmistir: "+mesaj)
        elif mesaj < "1.623":
            print(ad + " kriptosu düşmüştür: " + mesaj)
        elif mesaj > "1.623":
            print(ad + " kriptosu yükselmistir: " + mesaj)
        elif mesaj < "301,7":
            print(ad+" kriptosu düşmüştür: "+mesaj)
        elif mesaj > "301,7":
            print(ad+" kriptosu yükselmistir: "+mesaj)
        elif mesaj < "1":
            print(ad+" kriptosu düşmüştür: "+mesaj)
        elif mesaj > "1":
            print(ad+" kriptosu yükselmistir: "+mesaj)
        elif mesaj < "33,13":
            print(ad+" kriptosu düşmüştür: "+mesaj)
        elif mesaj > "33,13":
            print(ad+" kriptosu yükselmistir: "+mesaj)

if __name__ == '__main__':
    baglan = selenium_baglan()
    print("**************************")
    time.sleep(2)
    foreks = veri_Foreks()
    os = observer()
    foreks.ekle(os)
    for i in range(0,len(baglan.kurlar)):
        foreks.bilgi(baglan.kurlar[i],baglan.kurlar2[i])
    time.sleep(5)
    baglan.browser.close()


