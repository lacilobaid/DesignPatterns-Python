import time
from abc import ABC, abstractmethod
from smtplib import SMTP
import mail_login as m
import requests

class mesaj_gonderen(ABC):

    @abstractmethod
    def mesaj_gonder(self, mesaj): pass


class mesaj(ABC):
    mesajgonderen : mesaj_gonderen

    def __init__(self, mesajgonderen: mesaj_gonderen):

        self.mesajgonderen = mesajgonderen

    @abstractmethod
    def mesaj(self): pass

class discord_mesaj(mesaj):

    def mesaj(self):
        self.mesajgonderen.mesaj_gonder(self)

class discord(mesaj_gonderen):

    def mesaj_gonder(self, mesaj):

        try:
            print("** DISCORD **")

            url = 'url'
            token = {'authorization': 'autho'}

            mesaj = input("Gonderilecek mesaj: ")
            gonderilen = {'content': mesaj}
            requests.post(url, headers=token, data=gonderilen)
            time.sleep(3)
            print("Mesaj gönderimi başarılı...")
        except: pass


class outlook_mesaj(mesaj):

    def mesaj(self):
        self.mesajgonderen.mesaj_gonder(self)

class outlook(mesaj_gonderen):
    try:
        def mesaj_gonder(self, mesaj):
            print("** OUTLOOK **")

            konu = input("Konu başlığı girin: ")
            gonderilecek_mesaj = input("Mesaj içeriği girin: ")
            content = f"Subject: {konu}\n\n{gonderilecek_mesaj}"
            from_ = m.from_address
            sifre = m.password
            to_ = m.to_address

            mail = SMTP("smtp.office365.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(from_, sifre)
            mail.sendmail(from_, to_, content.encode("UTF-8"))
            mail.close()

            time.sleep(3)
            print("Mesaj gönderimi başarılı...")
    except: pass

if __name__=='__main__':
    dc_mesaj_gonder = discord()
    dc_mesaj = discord_mesaj(dc_mesaj_gonder)
    dc_mesaj.mesaj()

    ol_mesaj_gonder = outlook()
    ol_mesaj = outlook_mesaj(ol_mesaj_gonder)
    ol_mesaj.mesaj()





