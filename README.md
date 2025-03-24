# 🎯 Akbank Python ve Yapay Zekaya Giriş Bootcamp Projesi

## 🚇 Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

### 1. Proje Özeti

Bu projede, bir metro ağı simüle edilmiştir. Projenin amacı, kullanıcılar tarafından belirlenen iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı bulmaktır.

Metro ağı, bir **graf veri yapısı** kullanılarak modellenmiş ve **BFS** (Breadth-First Search) ile **A\*** algoritmalarından faydalanılarak, rotalar belirlenmiştir. Kullanıcılar, iki istasyon arasındaki en uygun yol seçeneğini belirleyebilir, metro hattındaki aktarmaları ve seyahat sürelerini göz önünde bulundurabilir.

#### 1.1 Projede Kullanılan Metro Ağı

![alt text](diagrams/istasyonlar.svg)

### 2. Projede Kullanılan Teknolojiler ve Kütüphaneler

- **`collections`**: Python'un standart kütüphanesinden olan bu modül, veri yapılarıyla çalışmayı kolaylaştırmak için kullanılmıştır. `deque` ve `defaultdict` gibi veri yapıları kullanılmaktadır.

- **`heapq`**: Python'da öncelik sırasına göre elemanları sıralamak ve kuyruğa almak için kullanılan bir modüldür. A\* algoritmasında, en düşük maliyetli yolu bulmak için kullanılmıştır.

- **`typing`**: Bu modül, fonksiyonların tip açıklamalarını yapmak için kullanılır. `Dict`, `List`, `Tuple` gibi veri tipi açıklamaları ile kodun anlaşılabilirliği artırılmıştır. Bu sayede, fonksiyonların giriş ve çıkış değerleri hakkında daha fazla bilgi sağlanır.

### 3. Algoritmalar

#### 3.1. BFS Algoritması (Breadth-First Search)

BFS, genişlik öncelikli arama algoritmasıdır. Graf yapısındaki bir başlangıç noktasından başlanarak, her adımda komşu düğümler sırasıyla ziyaret edilir. Bu algoritma, özellikle **en az sayıda adımla** hedefe ulaşmaya odaklanır ve aktarma sayısını minimize etmek için kullanılır.

BFS, her bir komşu istasyonu sırayla kontrol eder ve ilk hedefe ulaşan rotayı döndürür. Bu algoritma, özellikle **en az aktarmalı rotaların** bulunmasında etkilidir.

#### 3.2. A\* Algoritması

A\* algoritması, en kısa yolu bulmak için kullanılan bir arama algoritmasıdır. Hem **gerçek maliyeti** (yani istasyonlar arasındaki mesafeler) hem de **hedefe olan tahmin edilen mesafeyi** dikkate alır. Bu algoritma, BFS'ye kıyasla daha **hızlı ve verimli** çalışır çünkü hedefe daha hızlı yaklaşmak için ekstra bir "öncelik sırası" kullanır.

A\* algoritması, her adımda **öncelikli kuyruğa** (priority queue) ekler ve en düşük maliyetli yolu bulmaya çalışır. Bu da, daha hızlı bir rotanın bulunmasını sağlar.

#### 3.3. Neden Bu Algoritmalar Tercih Edildi

- **BFS**: Basitliği ve doğrudan çözüm arayışı ile en az aktarma gerektiren rotaların hızlıca bulunmasını sağlar. Her iki istasyon arasında **doğrudan** bir yol veya birkaç aktarma ile geçiş gereksinimini en iyi şekilde modelleyebiliriz.

- **A\***: Daha karmaşık, seyahat süresinin daha kritik olduğu senaryolarda, özellikle daha **hızlı rotaların** bulunmasında etkili bir algoritmadır. Hem mesafeyi hem de hedefe olan tahmini yolu dikkate alarak, bir yolun "optimal" olup olmadığını değerlendirir.

### 4. Örnek Kullanım ve Test Sonuçları

Projenin test kısmında, metro ağındaki birkaç farklı istasyon ve hat arasındaki rotalar test edilmiştir. Kullanıcı, belirlediği iki istasyon arasında:

1. **En Az Aktarmalı Rota**: Kullanıcının belirlediği iki istasyon arasında aktarmalarla seyahat eden en hızlı yolu bulur.
2. **En Hızlı Rota**: Aynı iki istasyon arasında, zaman açısından en verimli rotayı bulur.

**Örnek Senaryo:**

- **Başlangıç İstasyonu**: K2 (Ulus)
- **Hedef İstasyon**: Keçiören (T4)

- Beklenen sonuç:
  - **En Az Aktarmalı Rota**: Ulus -> Demetevler -> Demetevler -> Gar -> Keçiören [Toplam Süre: 6+3+9+5=`23 dakika`, `4 aktarma`]
  - **En Hızlı Rota**: Ulus -> Kızılay -> Kızılay -> Sıhhiye -> Gar -> Gar -> Keçiören [Toplam Süre: 4+2+3+4+2+5=`20 dakika`, `6 aktarma`]

BFS algoritması kullanılarak aktarmasız ve minimum aktarma ile gidebileceğiniz bir rota bulunur. A\* algoritması kullanılarak ise zaman açısından en verimli rotalar ortaya çıkar.

Örnek Kullanım:

```python
metro = MetroAgi()

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


metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

print("\AŞTİ’den Keçiören’e:")
rota = metro.en_az_aktarma_bul("K2", "T4")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("K2", "T4")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
```

```
AŞTİ’den Keçiören’e:
En az aktarmalı rota: Ulus -> Demetevler -> Demetevler -> Gar -> Keçiören
En hızlı rota (20 dakika): Ulus -> Kızılay -> Kızılay -> Sıhhiye -> Gar -> Gar -> Keçiören
```

---

### Farklı Senaryolar Altında Yapılan Testler

**Senaryo 1**:

```python
print("\n1. AŞTİ'den OSB'ye:")
rota = metro.en_az_aktarma_bul("M1", "K4")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("M1", "K4")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
1. AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
```

---

**Senaryo 2**:

```python
print("\n2. Batıkent'ten Keçiören'e:")
rota = metro.en_az_aktarma_bul("T1", "T4")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("T1", "T4")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
2. Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören
```

---

**Senaryo 3**:

```python
print("\n3. Keçiören'den AŞTİ'ye:")
rota = metro.en_az_aktarma_bul("T4", "M1")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("T4", "M1")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
3. Keçiören'den AŞTİ'ye:
En az aktarmalı rota: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (19 dakika): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
```

---

**Senaryo 4**:

```python
print("\n4. AŞTİ’den Keçiören’e:")
rota = metro.en_az_aktarma_bul("K2", "T4")  # Daha az aktarmalı ama daha uzun sürebilecek bir rota
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("K2", "T4")  # Daha fazla aktarma ile ama daha kısa sürede ulaşılabilecek bir rota
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
4. AŞTİ’den Keçiören’e:
En az aktarmalı rota: Ulus -> Demetevler -> Demetevler -> Gar -> Keçiören
En hızlı rota (20 dakika): Ulus -> Kızılay -> Kızılay -> Sıhhiye -> Gar -> Gar -> Keçiören
```

---

**Senaryo 5**:

```python
print("\n5. Hedef İstasyon Bulunamadı (Geçersiz İstasyon):")
rota = metro.en_az_aktarma_bul("M1", "X3")  # X3 geçersiz bir istasyon
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("M1", "X3")  # X3 geçersiz bir istasyon
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
5. Hedef İstasyon Bulunamadı (Geçersiz İstasyon):
Hedef istasyonu ağda bulunamadı.
Hedef istasyonu ağda bulunamadı.
```

---

**Senaryo 6**:

```python
print("\n6. Geçersiz Başlangıç İstasyonu (Başlangıç yok):")
rota = metro.en_az_aktarma_bul("X1", "K4")  # X1 geçersiz bir başlangıç istasyonu
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("X1", "K4")  # X1 geçersiz bir başlangıç istasyonu
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
6. Geçersiz Başlangıç İstasyonu (Başlangıç yok):
Başlangıç istasyonu ağda bulunamadı.
Başlangıç istasyonu ağda bulunamadı.
```

---

**Senaryo 7**:

```python
print("\n7. Başlangıç ve Hedef Aynı (AŞTİ'den AŞTİ'ye):")
rota = metro.en_az_aktarma_bul("M1", "M1")  # Aynı istasyona gitmek
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("M1", "M1")  # Aynı istasyona gitmek
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
7. Başlangıç ve Hedef Aynı (AŞTİ'den AŞTİ'ye):
En az aktarmalı rota: AŞTİ
En hızlı rota (0 dakika): AŞTİ
```

---

**Senaryo 8**:

```python
print("\n8. Ters Yönle Rota Arama (AŞTİ'den Keçiören'e):")
rota = metro.en_az_aktarma_bul("M1", "T4")  # AŞTİ'den Keçiören'e, ters yön
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("M1", "T4")  # AŞTİ'den Keçiören'e, ters yön
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

**Çıktı:**

```
8. Ters Yönle Rota Arama (AŞTİ'den Keçiören'e):
En az aktarmalı rota: AŞTİ -> Kızılay -> Sıhhiye -> Gar -> Gar -> Keçiören
En hızlı rota (19 dakika): AŞTİ -> Kızılay -> Sıhhiye -> Gar -> Gar -> Keçiören
```

---

### 4. Projeyi Geliştirme Fikirleri

- Kullanıcıdan giriş alınabilir: Şu anda test senaryoları üzerinden çalışıyor. Kullanıcıdan başlangıç ve varış noktalarını dinamik olarak alarak daha etkileşimli bir yapı oluşturulabilir.

- Arayüz geliştirilebilir: Kullanıcı deneyimini artırmak için terminal tabanlı menü, masaüstü (Tkinter/PyQt) veya web tabanlı (Flask/Django) bir arayüz eklenebilir.

- Farklı algoritmalar eklenebilir:

  - Dijkstra Algoritması: Ağırlıklı graf yapılarında en kısa mesafeyi bulmada oldukça başarılıdır ve A\* ile kıyaslanabilir.

  - Bellman-Ford Algoritması: Negatif ağırlıklı kenarlarla çalışabilme yeteneği sayesinde belirli özel senaryolar için avantaj sağlayabilir.

  - Floyd-Warshall Algoritması: Tüm çiftler arasındaki en kısa yolları hesaplamak için kullanılabilir ve farklı istasyonlar arasındaki bağlantıları analiz etmekte faydalı olabilir.
