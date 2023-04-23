import numpy as np 
import pandas as pd

dataset = pd.read_excel("finansal_dataset.xlsx")

TUPRS_deger = []
BIST100_deger = []
kur_deger = []
petrol_deger = []
altin_deger = []
tufe_deger = []
arzm2_deger = []
arzm3_deger = []
sue_deger = []
faiz_deger = []

def deger_oku(dizi,metin):
    eleman = dataset[metin].values
    for i in eleman:
        dizi.append(i)
        
deger_oku(TUPRS_deger,"TUPRS")
deger_oku(BIST100_deger,"BIST100")
deger_oku(kur_deger,"USD/TRY")
deger_oku(petrol_deger,"PETROL")
deger_oku(altin_deger,"ALTIN")
deger_oku(tufe_deger,"TUFE")
deger_oku(arzm2_deger,"M2")
deger_oku(arzm3_deger,"M3")
deger_oku(sue_deger,"SUE")
deger_oku(faiz_deger,"FAIZ")
    

TUPRS_getiri = []
BIST100_getiri = []
kur_getiri = []
petrol_getiri = []
altin_getiri = []
tufe_getiri  = []
arzm2_getiri = []
arzm3_getiri = []
sue_getiri = []
faiz = []
faiz_getiri = []

def faiz_aylik(deger,dizi):
    for z in dizi:
        eleman = z/12
        deger.append(eleman)
    
faiz_aylik(faiz,faiz_deger)

# getiri hesaplarının yapılması
def getiri_hesapla(dizi,deger):
    for y in deger:
        if deger.index(y) == 0:
            getiri = 0
        else:
            getiri = (deger[deger.index(y)] - deger[(deger.index(y))-1]) / deger[(deger.index(y))-1]
        dizi.append(getiri)

getiri_hesapla(TUPRS_getiri,TUPRS_deger)
getiri_hesapla(BIST100_getiri,BIST100_deger)
getiri_hesapla(kur_getiri,kur_deger)
getiri_hesapla(petrol_getiri,petrol_deger)
getiri_hesapla(altin_getiri,altin_deger)
getiri_hesapla(tufe_getiri,tufe_deger)
getiri_hesapla(arzm2_getiri,arzm2_deger)
getiri_hesapla(arzm3_getiri,arzm3_deger)
getiri_hesapla(sue_getiri,sue_deger)
getiri_hesapla(faiz_getiri,faiz)

# getirilerin tabloya sutun olarak kaydetme
dataset["rTUPRS"]=np.array(TUPRS_getiri)
dataset["rBIST100"]=np.array(BIST100_getiri)
dataset["rKur"]=np.array(kur_getiri)
dataset["rPetrol"]=np.array(petrol_getiri)
dataset["rAltin"]=np.array(altin_getiri)
dataset["Enflasyon"]=np.array(tufe_getiri)
dataset["rM2"]=np.array(arzm2_getiri)
dataset["rM3"]=np.array(arzm3_getiri)
dataset["rSue"]=np.array(sue_getiri)
dataset["rAyfaiz"]=np.array(faiz_getiri)


# aşırının hesaplanması
BIST100_asiri = []
TUPRS_asiri = []

def asiri_hesapla(getiri,faiz,dizi):
    for j in range(0,154):
        asiri = getiri[j]-faiz[j]
        dizi.append(asiri)
    
asiri_hesapla(BIST100_getiri,faiz_getiri,BIST100_asiri)
asiri_hesapla(TUPRS_getiri,faiz_getiri,TUPRS_asiri)   

# aşırıları tabloya sutun olarak kaydetme
dataset["erBIST100"]=np.array(BIST100_asiri)
dataset["erTUPRS"]=np.array(TUPRS_asiri)

# regresyon
bagimli_degisken=dataset["erTUPRS"]
etkenler = dataset[["erBIST100","rKur","rPetrol","rAltin","Enflasyon","rM2","rM3","rSue","rAyfaiz"]]

sabit = sm.add_constant(etkenler)
model_arb = sm.OLS(bagimli_degisken,sabit).fit()
model_arb.summary()
