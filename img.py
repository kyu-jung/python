import cv2
import os
import numpy as np

# 경로 확인 및 파일 위치 찾아오기
cur_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(cur_dir, 'sample.jpg')

print(img_path)

# 이미지 파일 읽기
img_arr = np.fromfile(img_path, np.uint8) # 한글 이름 파일도 읽어 올 수 있게 배열로 받음
img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR) # 배열을 이미지로 변환

cv2.imshow('sample', img)
cv2.waitKey(0)
cv2.destroyAllWindows()