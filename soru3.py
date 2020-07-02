"""Modül'ün kendisi:"""
def giren_cikan(ayrilanlar_listesi, personel_listesi):
    toplam_ayrilan = sum(ayrilanlar_listesi)
    ortalama_personel = sum(personel_listesi) / len(personel_listesi)
    devir_hizi = toplam_ayrilan / ortalama_personel * 100
    return toplam_ayrilan, ortalama_personel, devir_hizi


"""Modülün çalışma örneği:"""
ayrilanlar = [5, 10, 15, 13]
personeller = [100, 95, 110, 120]
ayrilan, ortalama, devir = giren_cikan(ayrilanlar, personeller)
print(ayrilan)
print(ortalama)
print(devir)
