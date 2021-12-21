import cv2

img = cv2.imread('wannaone.jpg')
img2 = cv2.resize(img, (1000,800))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge선 추출
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('wannaone',img)
cv2.imshow('wannaone2', img2)
cv2.imshow('GRAY',gray)
cv2.imshow('edge1',edge1)
cv2.imshow('edge2',edge2)
cv2.imshow('edge3',edge3)

# ENTER: 13, ESC: 27
while True:
    if cv2.waitKey() == 13:
        break

# 파일 저장하기
cv2.imwrite('wannaone_GRAY.jpg',gray)

cv2.destroyAllWindows()
