from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları
    
    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))
    def __repr__(self):
        return f"Istasyon({self.idx}, {self.ad}, {self.hat})"

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        try:
            # Eğer başlangıç istasyonu ağda yoksa None döndür
            if baslangic_id not in self.istasyonlar:
                print("Başlangıç istasyonu ağda bulunamadı.")
                return None
            
            # Eğer hedef istasyonu ağda yoksa None döndür
            if hedef_id not in self.istasyonlar:
                print("Hedef istasyonu ağda bulunamadı.")
                return None
            
            # Başlangıç ve Hedef istasyonu 
            baslangic = self.istasyonlar[baslangic_id]  
            hedef = self.istasyonlar[hedef_id]

            # Kuyruğa başlangıç istasyonu ve rota listesi eklenir
            kuyruk = deque([(baslangic, [baslangic])])  

            # Ziyaret edilen istasyonları tutmak için dictionary
            ziyaret_edildi = {baslangic}  

            while kuyruk:

                # Kuyruğun başındaki öğeyi al
                mevcut, rota = kuyruk.popleft()

                # Eğer hedefe ulaşmışsak rota döndürülür
                if mevcut == hedef:
                    return rota 
                
                # Mevcut istasyonun komşuları üzerinden gezin
                for komsu, _ in mevcut.komsular:  

                    # Eğer komşu istasyon daha önce ziyaret edilmemişse
                    if komsu not in ziyaret_edildi:

                        # Komşu istasyonu ziyaret edilmemişler listesine ekle
                        ziyaret_edildi.add(komsu)

                        # Komşu istasyonu rotaya ekle ve kuyruğa ekle
                        kuyruk.append((komsu, rota + [komsu]))  
            
            # Eğer hedefe ulaşılamazsa None döndürülür
            print("Hedefe ulaşılamadı!")
            return None
        except Exception as e:
                print(f"Beklenmedik bir hata oluştu: {e}")
                return None  # Herhangi başka bir hata oluşursa, hata mesajı verilir ve None döndürülür


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        try:
            # Eğer başlangıç istasyonu ağda yoksa döndür
            if baslangic_id not in self.istasyonlar:
                print("Başlangıç istasyonu ağda bulunamadı.")
                return None
            
            # Eğer hedef istasyonu ağda yoksa döndür
            if hedef_id not in self.istasyonlar:
                print("Hedef istasyonu ağda bulunamadı.")
                return None
            
            # Eğer başlangıç istasyonu ağda yoksa None döndür
            baslangic = self.istasyonlar[baslangic_id]
            hedef = self.istasyonlar[hedef_id]

            # Ziyaret edilen istasyonlar
            ziyaret_edildi = set()  

            # Öncelik sırasına göre işlem yapmak için min-heap (priority queue) kullanıyoruz. Başlangıç istasyonu kuyruğa alınır.
            pq = [(0, id(baslangic), baslangic, [baslangic])] 

            while pq:

                # Öncelikli kuyruktan en küçük zamanlı öğeyi al
                zaman, _, mevcut, rota = heapq.heappop(pq)

                # Hedef istasyonu bulundu, rota ve süre döndürülür 
                if mevcut == hedef:
                    return rota, zaman  
                
                 # Eğer bu istasyon daha önce ziyaret edildiyse geç
                if mevcut in ziyaret_edildi:
                    continue 

                # İstasyonu ziyaret edilmiş olarak işaretle
                ziyaret_edildi.add(mevcut)  

                # Mevcut istasyonun komşularını geziyoruz
                for komsu, seyahatSüresi in mevcut.komsular:
                    
                    # Eğer komşu istasyon daha önce ziyaret edilmediyse
                    if komsu not in ziyaret_edildi:  
                        # Seyahat süresiyle birlikte komşu istasyonu kuyruğa ekle
                        heapq.heappush(pq, (zaman + seyahatSüresi, id(komsu), komsu, rota + [komsu]))
            # Eğer hedefe ulaşamazsak None döndürülür
            print("Hedefe ulaşılamadı!")
            return None  
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu: {e}")
            return None  # Herhangi başka bir hata oluşursa, hata mesajı verilir ve None döndürülür
    

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 4: Daha az aktarmalı ama daha uzun sürebilecek bir rota
    print("\n4. AŞTİ’den Keçiören’e:")
    rota = metro.en_az_aktarma_bul("K2", "T4")  # Daha az aktarmalı ama daha uzun sürebilecek bir rota
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("K2", "T4")  # Daha fazla aktarma ile ama daha kısa sürede ulaşılabilecek bir rota
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 5: Hedef İstasyonun Bulunmadığı Durum (Geçersiz İstasyon)
    print("\n5. Hedef İstasyon Bulunamadı (Geçersiz İstasyon):")
    rota = metro.en_az_aktarma_bul("M1", "X3")  # X3 geçersiz bir istasyon
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "X3")  # X3 geçersiz bir istasyon
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 6: Geçersiz Başlangıç İstasyonu
    print("\n6. Geçersiz Başlangıç İstasyonu (Başlangıç yok):")
    rota = metro.en_az_aktarma_bul("X1", "K4")  # X1 geçersiz bir başlangıç istasyonu
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("X1", "K4")  # X1 geçersiz bir başlangıç istasyonu
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 7: Aynı İstasyon, Başlangıç ve Hedef Aynı
    print("\n7. Başlangıç ve Hedef Aynı (AŞTİ'den AŞTİ'ye):")
    rota = metro.en_az_aktarma_bul("M1", "M1")  # Aynı istasyona gitmek
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "M1")  # Aynı istasyona gitmek
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 8: Ters Rota (İstasyonlar Arasında Ters Yön)
    print("\n8. Ters Yönle Rota Arama (AŞTİ'den Keçiören'e):")
    rota = metro.en_az_aktarma_bul("M1", "T4")  # AŞTİ'den Keçiören'e, ters yön
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "T4")  # AŞTİ'den Keçiören'e, ters yön
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))