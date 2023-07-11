#작성자 : 이승헌
#FOG와 가우시안 블러를 같이 넣어서 처리했음.
import cv2
import imgaug.augmenters as iaa

# 이미지 로드
image_path = "path"
image = cv2.imread(image_path)

# 이미지를 RGB 형식으로 변환
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# augmenter 생성
augmenter = iaa.Fog()

# 이미지에 augmenter 적용
augmented_image = augmenter(image=image)

# 수정된 이미지를 다시 BGR 형식으로 변환
augmented_image = cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR)

# 이미지에 가우시안 블러 효과 적용
blurred = cv2.GaussianBlur(augmented_image, (99,99), 30)

# 원본 이미지와 가우시안 블러 이미지를 비율에 맞게 섞기
foggy = cv2.addWeighted(augmented_image, 0.5, blurred, 0.7, 0)
# 수정된 이미지 저장
output_path = "path"
cv2.imwrite(output_path, augmented_image)
