# hand_gesture_video_control
hand_gesture_video_control, bilgisayarla görme ve el hareketi tanıma kullanarak video oynatma ve kontrol işlemleri yapmanızı sağlayan bir Python projesidir. Gerçek zamanlı veya video dosyası üzerinden el hareketlerini algılar ve önceden tanımlanmış hareketlere göre videoyu durdurur, başlatır veya ileri/geri sarar.

## Proje Yapısı
/               – root  
|-- data/             – (isteğe bağlı) veri setleri veya önceden kaydedilmiş videolar  
|-- dist/             – build / dağıtım dosyaları (varsa)  
|-- frame_processing/ – video karelerini işleme ve el hareketlerini algılama kodları  
|-- ornek_video/      – test için örnek video(lar)  
|-- model_training.ipynb – el hareketi tanıma modelinin eğitildiği notebook  
|-- logistic_model.pkl – eğitimli hareket tanıma modeli  
|-- scaler_model.pkl   – giriş verisi ölçekleme modeli  
|-- proje_run.py       – ana çalıştırma scripti  
|-- requirements.txt   – bağımlılıklar  
|-- .gitignore  
|-- .gitattributes  

## Kurulum ve Çalıştırma
1. Repoyu klonlayın:  
git clone https://github.com/EmirhanEmir/hand_gesture_video_control.git
cd hand_gesture_video_control

2. Bağımlılıkları yükleyin:
pip install -r requirements.txt

3. Ana scripti çalıştırın:
python proje_run.py
