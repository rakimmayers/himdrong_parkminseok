import cv2
import numpy as np

#name, width, height = input().split()
img = cv2.imread("/Users/parkminseok/Desktop/drone/assignment_image.png", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([45,50,50])
upper_green = np.array([70,200,200])
mask = cv2.inRange(hsv, lower_green, upper_green)

for i in range(len(mask)):
    mask[0][i] = 0
    mask[len(mask)-1][i] = 0
    mask[i][0] = 0
    mask[i][len(mask[0])-1] = 0

ret, thr = cv2.threshold(mask, 150, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

contours_length = []
effective = []

for i in range(len(contours)):
    contours_length.append(len(contours[i]))
    if len(contours[i]) > 200:
        effective.append(len(contours[i]))

cv2.drawContours(img, contours, contours_length.index(min(effective)), (0,0,255), 3)

xx = []
yy = []

for k in range(len(contours[contours_length.index(min(effective))])):
    xx.append(contours[contours_length.index(min(effective))][k][0][0])
    yy.append(contours[contours_length.index(min(effective))][k][0][1])

center_x = int(sum(xx)/len(xx))
center_y = int(sum(yy)/len(yy))
cv2.line(img, (center_x, center_y), (center_x, center_y), (0,0,255), 3)

print(f"center_x : {center_x}")
print(f"center_y : {center_y}")

#if width < center_x+10 and width > center_x-10 and height < center_y+10 and height > center_y-10:
#    print(True)
#else:
#    print(False)

cv2.imshow('mask', mask)
cv2.imshow('image with contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()