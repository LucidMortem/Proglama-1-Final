import matplotlib.pyplot as plt
import numpy as np
birim_degisken_gider = 425
birim_satis_fiyati = 660

miktar = np.random.randint(3000,size=10)
sabit_gider = [470000 for _ in range(len(miktar))]
satis_gelirleri = birim_satis_fiyati * miktar
degisken_giderler = birim_degisken_gider * miktar
toplam_giderler = sabit_gider + degisken_giderler

plt.plot(miktar, sabit_gider, label = "Sabit Gider")
plt.plot(miktar, satis_gelirleri, label = "Satış Gelirleri")
plt.plot(miktar, degisken_giderler, label  ="Degisken Giderler")
plt.plot(miktar, toplam_giderler, label = "Toplam  Gider")
plt.ylabel("Gelir-Gider")
plt.xlabel("Miktar")
plt.title("Başa Baş Grafiği")
plt.legend()
plt.show()
