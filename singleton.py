import random
import time
import firebase_admin
from firebase_admin import credentials,firestore

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class member(metaclass=Singleton):
    def __init__(self):
        try:
            cred = credentials.Certificate("singletonServer.json")
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
        except:
            print("Baglantı basarısız...")

    def login(self):
        print("** Kayit **")
        doc_len = list(self.db.collection('uyeler').get())
        i = len(doc_len)
        doc_name = 'hesap' + str(i+1)
        kullanici_adi = input("Kullanıcı adı giriniz: ")
        sifre = input("Sifre giriniz: ")
        telefon = input("Telefon numaranızı giriniz: ")
        if len(telefon) == 10 and telefon.startswith("5"):
            kod= random.randint(1000,9999)
            print("Doğrulama kodunuz:",kod)
            dogrulama=int(input(telefon + " Nolu telefona gelen kodu giriniz: "))
            if kod==dogrulama:
                data = {'kullanici_Adi': kullanici_adi, 'Sifre': sifre, 'telefon_Numarasi': telefon}
                print("Kaydolunuyor...")
                time.sleep(2)
                try:
                    self.db.collection('uyeler').document(doc_name).set(data)
                    print("Kayıt işlemi basarili. Giriş yapabilirsiniz...")
                    self.signin()
                except:
                    print("Kayıt basarısız...")
            else:
                print("Hatali kod girdiniz.")
        else:
            print("Hatali bir telefon numarası girdiniz.")

    def signin(self):
        print("** Giris **")
        while True:
            kullanici_adi = input("Kullanıcı adı giriniz: ")
            sifre = input("Sifre giriniz: ")
            doc_kullaniciAdi = self.db.collection('uyeler').where("kullanici_Adi", "==", kullanici_adi).get()
            if doc_kullaniciAdi:
                doc_sifre = self.db.collection('uyeler').where("Sifre", "==", sifre).get()
                if doc_sifre:
                    print("Giriş başarılı", kullanici_adi)
                    break
                else:
                    print("Sifre yanlıs.")
            else:
                print("Bu isimde bir kullanıcı yoktur.")
                return False


if __name__ == '__main__':

   while True:
       m1 = member()
       m2 = member()
       print("**************************************")
       giris = input("1. Web Kayıt/Giris\n2. Mobil Kayıt/Giris \nQ. Cıkıs ")
       if giris == "q" or giris == "Q":
           print("Cikis yapiliyor...")
           time.sleep(2)
           break
       elif giris == "1":
           kontrol=m1.signin()
           if kontrol==False:
               time.sleep(2)
               m1.login()
       elif giris=="2":
           kontrol = m2.signin()
           if kontrol==False:
               time.sleep(2)
               m2.login()


