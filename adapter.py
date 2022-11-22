import firebase_admin
from firebase_admin import credentials,firestore
import time
import pypyodbc
#mongo
class firebase_db:
    def __init__(self):
        cred = credentials.Certificate("servisAccount.json")
        firebase_admin.initialize_app(cred)
        self.db=firestore.client()
    def veri_oku(self):
        goruntule = list(self.db.collection(u'urunler').get())
        for snap in goruntule:
            print(snap.to_dict())
        print(len(goruntule))
    def veri_ekle(self, ):
        doc_len = list(self.db.collection(u'urunler').get())
        i = len(doc_len)
        i += 1
        document_name = 'urun_bilgi' + str(i)
        urun_id = int(input('Urun id giriniz: '))
        urun_adi = input('Urun adi giriniz: ')
        urun_fiyat = int(input('Urun fiyati giriniz: '))
        urun_stok = int(input('Urun stok giriniz: '))
        data = {'urunID': urun_id, 'urunAdi': urun_adi,'urunFiyat': urun_fiyat,'urunStok': urun_stok}
        self.db.collection(u'urunler').document(document_name).set(data)

class mssql_db:
    def  __init__(self):
        yeni_database = pypyodbc.connect(
            'Driver={SQL Server};'
            'Server=DESKTOP-L5EBS4A\SQLEXPRESS;'
            'Database=urun_bilgi;'
            'Trusted_Connection=True;'
        )
        self.imlec = yeni_database.cursor()
    def urun_goster(self):
        self.imlec.execute('Select * from urun_bilgi_t')
        urunler = self.imlec.fetchall()
        if len(urunler) == 0:
            print("Urun bulunmamaktadır.")
        else:
            for i in urunler:
                print(i)
    def urun_ekle(self):
        urun_id = int(input('Urun id giriniz: '))
        urun_adi = input('Urun adi giriniz: ')
        urun_fiyat = int(input('Urun fiyati giriniz: '))
        urun_stok = int(input('Urun stok giriniz: '))
        sorgu = 'Insert into urun_bilgi_t (urunID, urunAdi, urunFiyat, urunStok) Values (?,?,?,?)'
        self.imlec.execute(sorgu,(urun_id,urun_adi,urun_fiyat,urun_stok))
        self.imlec.commit()

class db_adapter(mssql_db):
    fb=firebase_db()
    def urun_goster(self):
        self.fb.veri_oku()
    def urun_ekle(self):
        self.fb.veri_ekle()


if __name__ == '__main__':
    new_db=mssql_db()
    adapter=db_adapter()
    print('* URUN * BILGI * SISTEMI *')
    while True:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        secim = input("Cikis icin Q, \nFirebase islemleri icin F, \nMSSQL islemleri icin S'ye basiniz: ")
        if secim == 'Q' or secim == 'q':
            print('Program sonlandiriliyor...')
            time.sleep(2)
            break
        elif secim == 's' or secim == 'S':
            islem = input('1. Urunleri goster \n2. Urun ekle \nBir secim yapiniz: ')
            if islem == '1':
                new_db.urun_goster()
            elif islem=='2':
                new_db.urun_ekle()
                print('Urun ekleniyor...')
                time.sleep(2)
                print('Urun eklendi...')
            else: print('Hatali islem secimi...')
        elif secim == 'f' or secim == 'F':
            islem = input('1. Urunleri goster \n2. Urun ekle \nBir secim yapiniz: ')
            if islem == '1':
                adapter.urun_goster()
            elif islem=='2':
                adapter.urun_ekle()
                print('Urun ekleniyor...')
                time.sleep(2)
                print('Urun eklendi...')
            else: print('Hatali islem secimi...')
        else: print('Hatali secim yaptiniz...')

