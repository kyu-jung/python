import cv2

cap = cv2.VideoCapture(0) # 컴퓨터에 연결되어있는 0번째 카메라

if not cap.isOpened(): # 비디오가 연결이 되어있지 않을 때
    print('카메라를 연결할 수 없습니다.')
    exit()

while True:
    ret, frame = cap.read() # 카메라에서 읽어온 정보를 받음
    if not ret:
        print('프레임을 읽을 수 없습니다.')
        break

    cv2.imshow('test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()