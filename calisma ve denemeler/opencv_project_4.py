import cv2
import numpy as np
from matplotlib import pyplot as plt

resim4orijinal = cv2.imread("hata ayıklama uygulama fotoğraflar/perde1.jpeg")
resim4gri = cv2.imread("hata ayıklama uygulama fotoğraflar/perde1.jpeg",0)
e,tresh1 = cv2.threshold(resim4gri,127,255,cv2.THRESH_BINARY)
e,tresh2 = cv2.threshold(resim4gri,127,255,cv2.THRESH_BINARY_INV)
e,tresh3 = cv2.threshold(resim4gri,127,255,cv2.THRESH_OTSU)
e,tresh4 = cv2.threshold(resim4gri,127,255,cv2.THRESH_TOZERO)
e,tresh5 = cv2.threshold(resim4gri,127,255,cv2.THRESH_TOZERO_INV)
e,tresh6 = cv2.threshold(resim4gri,127,255,cv2.THRESH_TRUNC)

titlelist4=["binary","binary inv","otsu","tozero","tozero inv","trunc"] 
resimlist4=[tresh1,tresh2,tresh3,tresh4,tresh5,tresh6]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(resimlist4[i],"gray",vmin=0,vmax=255) 
    plt.title(titlelist4[i]) 
    plt.xticks([]),plt.yticks([]) #resimin eksenleri
plt.show()    


cv2.waitKey(0) 
cv2.destroyAllWindows()

 