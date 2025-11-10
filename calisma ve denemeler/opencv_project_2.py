import cv2
import numpy as np

resim2 = cv2.imread("hata ayıklama uygulama fotoğraflar/tekstil2.jpeg")

#kernel = np.ones((3,3),np.float32)/5
#blur = cv2.filter2D(resim2,-1,kernel)

#blur = cv2.blur(resim2,(5,5))
#cv2.imshow("blurred resim 2", blur)
#-----------------------------------
#kernel = np.array([[-1,-1,-1],
#                   [-1,9,-1],
#                  [-1,-1,-1]])

#keskinleştirme = cv2.filter2D(resim2,-1,kernel)
#cv2.imshow("keskinleştirilmiş resim 2", keskinleştirme)
#-----------------------------------

#gaus = cv2.GaussianBlur(resim2,(5,5),0)
#cv2.imshow("gaussian blur resim 2", gaus)
#-----------------------------------

#biletral = cv2.bilateralFilter(resim2,9,75,75)
#cv2.imshow("biletral filtrelenmiş resim 2", biletral)
#-----------------------------------

#median = cv2.medianBlur(resim2,11)
#cv2.imshow("median blur resim 2", median)
#-----------------------------------
 
#canny = cv2.Canny(resim2,100,200)
#cv2.imshow("canny edge detection resim 2", canny)
#-----------------------------------
 

cv2.imshow("orijinal resim 2", resim2)



cv2.waitKey(0)
cv2.destroyAllWindows()

