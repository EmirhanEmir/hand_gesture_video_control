# hand_gesture_video_control
hand_gesture_video_control, bilgisayarla görme ve makine öğrenmesi tekniklerini kullanarak videoları el hareketleriyle kontrol etmenizi sağlayan bir Python projesidir. Gerçek zamanlı kamera görüntüsü üzerinden el hareketlerini algılar ve önceden tanımlanmış hareketlere göre videoyu oynatır, durdurur, ileri veya geri sarar. Böylece videoları tamamen el hareketlerinizle, dokunmaya gerek kalmadan kontrol edebilirsiniz.


## Proje Yapısı
/                     
|-- data/           
|-- dist/proje_run.exe             
|-- frame_processing/ <br>
|-- ornek_video/      <br>
|-- model_training.ipynb <br>
|-- logistic_model.pkl <br>
|-- scaler_model.pkl   <br>
|-- proje_run.py       <br> 
|-- requirements.txt    <br>
|-- .gitignore  <br>
|-- .gitattributes  <br>

## Kurulum ve Çalıştırma

Bu projeyi çalıştırmanın iki yolu vardır:  

### 1️⃣ Kaynak kodu üzerinden (Python ile)
1. Repoyu klonlayın: `git clone https://github.com/EmirhanEmir/hand_gesture_video_control.git && cd hand_gesture_video_control`  
2. (Önerilen) Python 3.10 kullanarak sanal ortam oluşturun: `python -m venv venv && source venv/bin/activate  # Linux/macOS` veya `venv\Scripts\activate  # Windows`
3. Bağımlılıkları yükleyin: `pip install -r requirements.txt`   
4. Ana scripti çalıştırın: `python proje_run.py`  

### 2️⃣ Derlenmiş exe dosyası ile (Python yüklemeye gerek yok)
1. Repoyu indirin.  
2. `dist/` içindeki exe dosyasını çalıştırın.  
3. Dosya yapısını bozmadan çalıştırabilirsiniz; proje Python veya bağımlılıkları yüklemeden hazır şekilde çalışacaktır.

## Kullanım ve İşleyiş
- Sistem, webcam veya video dosyasından kareleri alır ve gerçek zamanlı olarak işler.  
- Model ile tanımlanan el hareketleri, videoyu durdurma, başlatma veya ileri/geri sarma gibi işlemleri tetikler.  
- Hızlı test için `ornek_video/` içindeki videolar kullanılabilir.

## Gereksinimler
- Python 3.8-3.10 (sadece projeyi klonlayıp çalıştırmak isteyenler için gereklidir)  
- `requirements.txt` içindeki bağımlılıklar
- (İsteğe bağlı) Webcam veya video dosyası, gerçek zamanlı test yapmak isteyenler için

## Proje Amacı ve Öğrenilenler
Bu proje, video üzerinde el hareketi ile kontrol uygulamalarını keşfetmek için geliştirilmiştir.  
Projede şunlar öğrenilmiştir:  
- Video karelerinin işlenmesi  
- El hareketlerini sınıflandıran bir makine öğrenmesi modeli eğitimi (scikit-learn ile)  
- Modeli gerçek zamanlı kontrol döngüsüne entegre etme  
- Video girişi, hareket algılama ve kontrol mantığını bir araya getiren çalışan bir script oluşturma



