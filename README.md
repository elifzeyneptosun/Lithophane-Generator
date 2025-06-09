# Lithophane-Generator
Bu proje, seçilen bir görseli gri tonlara çevirip her pikselin parlaklık değerine göre bir yükseklik haritası oluşturur. Bu haritaya göre 3D yüzey modelini hesaplayarak STL dosyası üretir ve kullanıcıdan dosya kaydetme konumu ister. 3D baskı için kullanıma uygundur.

# Görselden STL Oluşturucu

Bu Python projesi, yüklenen bir görseli gri tonlamaya çevirerek yükseklik haritası oluşturur ve bu haritaya göre 3D yüzey modeli üretip STL dosyası olarak kaydeder. Özellikle 3D baskıya uygun yüzey modelleri oluşturmak için kullanılabilir.

## Özellikler

- Görselden yükseklik haritası üretimi
- Yükseklik verisine göre 3D modelleme
- STL formatında dışa aktarma
- Tkinter arayüzü ile kullanıcı dostu dosya seçimi

## Gereksinimler

- Python 3.x
- NumPy
- Pillow
- matplotlib
- numpy-stl
- tkinter (Python ile birlikte gelir)

Gerekli kütüphaneleri yüklemek için:
pip install numpy pillow matplotlib numpy-stl

Projeyi Çalıştırmak için:
python main.py


