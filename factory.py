from abc import ABCMeta,abstractmethod
import iban_kodlari as ik

class Banka(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def nesne_olustur(self): pass

class Garanti_Bankasi(Banka):

    def nesne_olustur(self):

        print('Bu IBAN numarasi Garanti Bankasina aittir.')

class Kuveytturk_Bankasi(Banka):

    def nesne_olustur(self):

        print('Bu IBAN numarasi Kuveytturk Bankasina aittir.')

class Is_Bankasi(Banka):

    def nesne_olustur(self):

        print('Bu IBAN numarasi Is Bankasina aittir.')

class Kullanici():
    def __init__(self):
        self.iban_no=input('IBAN NO: ')

class Factory:

    @staticmethod
    def nesne_olustur():
        kullanici = Kullanici()
        if len(kullanici.iban_no) == 26 and kullanici.iban_no[4:9] == ik.iban_kodlari['Garanti']:
            return Garanti_Bankasi().nesne_olustur()
        if len(kullanici.iban_no) == 26 and kullanici.iban_no[4:9] == ik.iban_kodlari['Is']:
            return Is_Bankasi().nesne_olustur()
        if len(kullanici.iban_no) == 26 and kullanici.iban_no[4:9] == ik.iban_kodlari['Kuveytturk']:
            return Kuveytturk_Bankasi().nesne_olustur()
        return None

if __name__=='__main__':
    factory= Factory().nesne_olustur()
