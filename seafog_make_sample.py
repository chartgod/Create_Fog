import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('C:/C2PNet-main/data/CUSTOM/C2PNet_2.jpg')

# 이미지에 가우시안 블러 효과 적용
blurred = cv2.GaussianBlur(image, (99,99), 30)

# 원본 이미지와 가우시안 블러 이미지를 비율에 맞게 섞기
foggy = cv2.addWeighted(image, 0.5, blurred, 0.7, 0)

# 결과 이미지 출력
cv2.imshow('Foggy', foggy)
cv2.waitKey(0)
cv2.destroyAllWindows()
