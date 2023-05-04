import numpy as np 
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

dataset = pd.read_excel("finansal_dataset.xlsx")
dataset_manuel = pd.read_excel("manuel_finansal_dataset.xlsx")

class analiz:
    
    def deger_oku(self,dizi,metin,dataset):
        eleman = dataset[metin].values
        for i in eleman:
            dizi.append(i)
        
    def getiri_hesapla(self,dizi,deger): # pct_change()
        for y in deger:
            if deger.index(y) == 0:
                getiri = 0
            else:
                getiri = np.log(deger[deger.index(y)] / deger[(deger.index(y))-1])
            dizi.append(getiri)
    
    def faiz_aylik(self,deger,dizi):
        for z in dizi:
            eleman = z/12
            deger.append(eleman)
            
    def asiri_hesapla(self,getiri,faiz,dizi):
        for j in range(0,154):
            asiri = (getiri[j]-faiz[j])*100
            dizi.append(asiri)
            
class model:
    
    def stats_model(self,bagimli,bagimsiz):
        sabit = sm.add_constant(bagimsiz)
        model_arb = sm.OLS(bagimli,sabit).fit()
        return model_arb.summary()
        
    def sk_model(self,bagimli,bagimsiz): 
        lm = LinearRegression()
        return lm.fit(bagimsiz,bagimli)
    

model = model() 
analiz = analiz()

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

analiz.deger_oku(TUPRS_deger,"TUPRS",dataset)
analiz.deger_oku(BIST100_deger,"BIST100",dataset)
analiz.deger_oku(kur_deger,"USD/TRY",dataset)
analiz.deger_oku(petrol_deger,"PETROL",dataset)
analiz.deger_oku(altin_deger,"ALTIN",dataset)
analiz.deger_oku(tufe_deger,"TUFE",dataset)
analiz.deger_oku(arzm2_deger,"M2",dataset)
analiz.deger_oku(arzm3_deger,"M3",dataset)
analiz.deger_oku(sue_deger,"SUE",dataset)
analiz.deger_oku(faiz_deger,"FAIZ",dataset)
    

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

analiz.faiz_aylik(faiz,faiz_deger)

# getiri hesaplarının yapılması
analiz.getiri_hesapla(TUPRS_getiri,TUPRS_deger)
analiz.getiri_hesapla(BIST100_getiri,BIST100_deger)
analiz.getiri_hesapla(kur_getiri,kur_deger)
analiz.getiri_hesapla(petrol_getiri,petrol_deger)
analiz.getiri_hesapla(altin_getiri,altin_deger)
analiz.getiri_hesapla(tufe_getiri,tufe_deger)
analiz.getiri_hesapla(arzm2_getiri,arzm2_deger)
analiz.getiri_hesapla(arzm3_getiri,arzm3_deger)
analiz.getiri_hesapla(sue_getiri,sue_deger)
analiz.getiri_hesapla(faiz_getiri,faiz)

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

analiz.asiri_hesapla(BIST100_getiri,faiz_getiri,BIST100_asiri)
analiz.asiri_hesapla(TUPRS_getiri,faiz_getiri,TUPRS_asiri)   

# aşırıları tabloya sutun olarak kaydetme
dataset["erBIST100"]=np.array(BIST100_asiri)
dataset["erTUPRS"]=np.array(TUPRS_asiri)

# regresyon
# stats ile model kurma
bagimli_degisken = dataset[["erTUPRS"]]
etkenler = dataset[["erBIST100","rKur","rPetrol","rAltin","Enflasyon","rM2","rM3","rSue","rAyfaiz"]]
smodel = model.stats_model(bagimli_degisken,etkenler)


# manuel 
bagimli_degisken_manuel =hazir_dataset["ERTUPRS"]
etkenler_manuel = hazir_dataset[["ERBIST100","RKUR","RPETROL","RALTIN","RTUFE","RM2","RM3","RSUE","RFAIZ"]]
smodel_manuel = model.stats_model(bagimli_degisken_manuel,etkenler_manuel)


# sklearn ile model kurma
skmodel= model.sk_model(bagimli_degisken,etkenler)

# manuel
skmodel_manuel = model.sk_model(bagimli_degisken_manuel,etkenler_manuel)
