import cv2
import numpy as np

resim3 = cv2.imread("hata ayıklama uygulama fotoğraflar/tekstil3.jpeg")

cv2.line(resim3,(0,0),(500,500),(200,0,100),100)
cv2.rectangle(resim3,(500,500),(2000,3000),(255,100,0),5) #-1 ile içi dolar

cv2.circle(resim3,(1000,1000),200,(100,200,200),10)
cv2.ellipse(resim3,(1500,1500),(400,200),0,0,360,(50,100,200),5) #0,0,360 değ
#erleri açıyı belirler 0 0 180 olursa yarım elips olur (parabol gibi)
cv2.putText(resim3,"YAZI YAZINIZ",(1000,2500),cv2.FONT_HERSHEY_COMPLEX,5,
            (255,0,0),10)





cv2.imshow("orijinal resim 3", resim3) 
cv2.waitKey(0)
cv2.destroyAllWindows()