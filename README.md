# Bilgisayarlı Görü ile Parmak Sayma Uygulaması

## Proje Hakkında

Bu proje, **i2i Academy Computer Vision** ödevi kapsamında geliştirilmiştir.

Uygulama, bilgisayar kamerasından alınan gerçek zamanlı görüntü üzerinde bir eli algılar ve açık olan parmakların sayısını hesaplayarak ekranda gösterir.

---

##  Projenin Amacı

Bu projenin amacı, bilgisayarlı görü teknolojilerini kullanarak gerçek zamanlı el algılama ve parmak sayma işlemini gerçekleştirmektir. Uygulama, OpenCV ve CVZone kütüphaneleri kullanılarak geliştirilmiştir.

---

## Kullanılan Teknolojiler

* Python 3.12
* OpenCV
* CVZone

---

## Özellikler

* Gerçek zamanlı kamera görüntüsü alma
* El algılama
* Açık parmakları tespit etme
* Parmak sayısını canlı olarak ekranda gösterme
* Basit ve kullanıcı dostu arayüz

---

## Proje Yapısı

```text
ComputerVision/
│
├── main.py
├── README.md
└── .gitignore
```

---

## Kurulum

Gerekli kütüphaneleri yükleyin.

```bash
pip install opencv-python cvzone
```

---

## Çalıştırma

Programı aşağıdaki komut ile çalıştırabilirsiniz.

```bash
python main.py
```

Program çalıştırıldıktan sonra kamera açılır. Elinizi kameraya gösterdiğinizde açık parmak sayısı gerçek zamanlı olarak ekranda görüntülenir.

Programdan çıkmak için **Q** tuşuna basmanız yeterlidir.

---

## Çalışma Mantığı

1. Kamera açılır.
2. El gerçek zamanlı olarak algılanır.
3. Parmakların açık veya kapalı olduğu belirlenir.
4. Açık parmak sayısı hesaplanır.
5. Sonuç video ekranında gösterilir.

---

## Sonuç

Bu proje ile bilgisayarlı görü teknolojileri kullanılarak gerçek zamanlı el algılama ve parmak sayma uygulaması başarıyla geliştirilmiştir. Proje sayesinde OpenCV ve CVZone kütüphanelerinin temel kullanımı öğrenilmiş ve gerçek zamanlı görüntü işleme konusunda deneyim kazanılmıştır.

---

## Geliştirici

**Gamze Canpolat**

Bilgisayar Mühendisliği Öğrencisi
