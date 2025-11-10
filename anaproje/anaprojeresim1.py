import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fotoğrafı oku
resim = cv2.imread("hata ayıklama uygulama fotoğraflar/perde1.jpeg")


# Grileştirme + Kontrast artırma
gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
gri_kontrast = cv2.equalizeHist(gri)

# Gaussian Blur 
blur = cv2.GaussianBlur(resim, (21, 21), 10)

# Canny Kenar Bulma 
kenar = cv2.Canny(gri, 80, 180)

# Sharpening 
kernel = np.array([[0, -1, 0],
                   [-1, 6, -1],
                   [0, -1, 0]])
sharpen = cv2.filter2D(resim, -1, kernel)

# Thresholding 
_, thresh = cv2.threshold(gri_kontrast, 120, 255, cv2.THRESH_BINARY)

# Görselleri listele
titlelist = ["Orijinal", "Grileştirme + Kontrast", "Gaussian Blur",
             "Canny Kenar", "Sharpening", "Thresholding"]
resimlist = [resim, gri_kontrast, blur, kenar, sharpen, thresh]

# Görselleri ekranda göster
plt.figure(figsize=(12,8))
for i in range(6):
    plt.subplot(2,3,i+1)
    if len(resimlist[i].shape) == 3:
        plt.imshow(cv2.cvtColor(resimlist[i], cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(resimlist[i], cmap="gray")
    plt.title(titlelist[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
