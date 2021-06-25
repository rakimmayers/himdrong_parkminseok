import cv2
import numpy as np

name, width, height = input().split()
width = int(width)
height = int(height)
img = cv2.imread(name, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_copy = img.copy()

lower_green = np.array([45,50,50])
upper_green = np.array([70,255,255])
mask = cv2.inRange(hsv, lower_green, upper_green)
canny = cv2.Canny(mask, 150, 255)

for i in range(len(mask)):
    mask[0][i] = 0
    mask[len(mask)-1][i] = 0

for i in range(len(mask)):
    mask[i][0] = 0
    mask[i][len(mask[0])-1] = 0

ret, thr = cv2.threshold(mask, 150, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(canny, contours, 1, (0,0,255), 3)
#cv2.drawContours(canny, contours, 2, (0,0,255), 3)
#cv2.drawContours(img, contours, 0, (0,0,255), 3)

effective = []

for i in range(len(contours)):
    effective.append(len(contours[i]))
#print(len(contours))


eeffective = []

for j in effective:
    if j > 200:
        eeffective.append(j)



xx = []
yy = []

for k in range(len(contours[effective.index(min(eeffective))])):
    xx.append(contours[effective.index(min(eeffective))][k][0][0])
    yy.append(contours[effective.index(min(eeffective))][k][0][1])

center_x = int(sum(xx)/len(xx))
center_y = int(sum(yy)/len(yy))

if width < center_x+10 and width > center_x-10 and height < center_y+10 and height > center_y-10:
    print(True)
else:
    print(False)
