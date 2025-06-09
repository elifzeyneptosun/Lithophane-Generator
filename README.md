# Lithophane Generator – Görselden STL Oluşturucu

Bu Python projesi, yüklenen bir görseli gri tonlamaya çevirerek her pikselin parlaklık değerine göre bir yükseklik haritası oluşturur. Bu haritaya dayanarak 3D yüzey modeli oluşturulur ve STL formatında kaydedilir. 3D yazıcılar için baskıya uygun modeller üretmek amacıyla tasarlanmıştır.

## Özellikler

- Görselden otomatik yükseklik haritası oluşturma  
- Parlaklığa göre 3D yüzey modelleme  
- STL formatında dışa aktarma  
- Tkinter tabanlı dosya seçme ve kaydetme arayüzü  

## Gereksinimler

- Python 3.x  
- NumPy  
- Pillow  
- matplotlib  
- numpy-stl  
- Tkinter (Python ile birlikte gelir)

- # Gelişmiş XOX (Tic Tac Toe) Oyunu

Bu Python projesi, klasik XOX oyununu gelişmiş özelliklerle sunar. Farklı tahta boyutları, zorluk seviyeleri ve isteğe bağlı debug paneli ile kullanıcı dostu bir deneyim sunar. Bilgisayar, minimax algoritması ve alfa-beta budama ile stratejik hamleler yapar.

## Özellikler

- Tahta boyutu seçimi (3x3 ile 10x10 arası)
- Zorluk seviyesi: Kolay, Orta, Zor
- İlk hamleyi yapacak oyuncunun seçimi (Kullanıcı / Bilgisayar)
- Gelişmiş yapay zeka (Minimax + Alfa-Beta Budama)
- Gerçek zamanlı debug paneli (hamle puanları ve kararlar)
- Oyun sonu bildirimi ve yeniden başlatma özelliği

## Kurulum

Bu projeyi çalıştırmak için Python 3.x yüklü olmalıdır. Gerekli modüller:

- `tkinter` (Python ile birlikte gelir)
- `ttk` (Tkinter içinden gelir)
- `math`, `os`, `sys` (standart kütüphanelerdir)

Ekstra kurulum gerekmez.

## Kullanım

1. Proje klasöründe terminal veya komut satırını açın.
2. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install numpy pillow matplotlib numpy-stl
