# [2021 MINI DRONE Autonomous Flight Contest](http://mini-drone.co.kr/notice)
![원정수 3](https://user-images.githubusercontent.com/82248453/125403162-29549f80-e3f0-11eb-9a23-253508428cb6.PNG)
## B League
## Team Himdrong
![image](https://user-images.githubusercontent.com/82248453/125475093-42a3cebd-0f56-472d-96fc-b91358330ff1.png)
<img src="https://user-images.githubusercontent.com/82248453/125419171-f349a667-80c5-4e91-9021-9e64930b9b83.jpg" width="400" height="300"></br>
![License](https://img.shields.io/badge/license-MIT-blue.svg) ![License](https://img.shields.io/badge/Raspberry%20Pi%20Zero-pass-blue) ![License](https://img.shields.io/badge/python-v3.9.2-brightgreen) ![License](https://img.shields.io/badge/opencv-v4.5.2-brightgreen) 
---
# Contents
## I. Progress Strategies
1. Development Environment Construction</br>
2. Hardwares</br>
3. Raspberry Pi OS Installation
4. PC Softwares</br>
5. Drone Operation</br>
6. Track Making</br></br>
## II. Algorithms
1. Track Analysis</br>
2. Modes Depending on Image</br>
3. Total Algorithms</br></br>
## III. Codes
1. Image Processing</br>
2. Controlling Drone</br>
3. Full Code</br></br>
## IV. Team Members
<br/>

# I. Progress Strategies
## __I-1. Development Environment Construction__
* <img src="https://user-images.githubusercontent.com/82248453/125612432-5fc3402e-1fa4-4966-ba2f-65a92fd3aa5b.png" width="20" height="20"> Python Installation</br>
 [Downloads](https://www.python.org/downloads/)</br></br>
* <img src="https://user-images.githubusercontent.com/82248453/125473710-f3ad6de2-7c29-4670-8808-577a3ed86872.png" width="20" height="20"> VSCode Installation</br>
 [Downloads](https://code.visualstudio.com)</br></br>
* <img src="https://user-images.githubusercontent.com/82248453/125612432-5fc3402e-1fa4-4966-ba2f-65a92fd3aa5b.png" width="20" height="20"> Python VSCode Extension Installation</br>
 [Downloads](https://marketplace.visualstudio.com/items?itemName=ms-python.python)</br>
<br/>

## __I-2. Hardwares__
 ![라즈베리파이](https://user-images.githubusercontent.com/82248453/125445132-93ec672f-4bd6-4e39-bffe-80c28faefd42.PNG)

- __Model__ : [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) 
- __Processor__ : BCM2835 @ 1GHz
- __Memory__ : 512MB RAM
- __Operating Power__ : 0.5-0.7V
</br></br></br>

<img src="https://user-images.githubusercontent.com/82248453/125569015-ea6c82c7-decb-4308-a0f6-337140f61346.jpg" width="400" height="300"> 

- __Model__ : [Frank-S01-V1.0 (SZH-EK104)](
https://www.devicemart.co.kr/goods/view?no=1376528)
- __Chipset__ : OV5647
- __Size__ : 60mm × 11.5mm × 5mm
- __Resolution of Image__ : 2592×1944p
- __Resolution of Video__ : 1080p30, 720p60, 640×480p60/90
- __Angle of View__ : 72.4°
- __Focus__ : Adjustable fixed lens
</br></br></br></br>

<img src="https://user-images.githubusercontent.com/82248453/125468403-b4299950-2080-4c7c-bbe6-4d728b988656.PNG" width="400" height="300"> 

- __Model__ : [CoDrone DIY](http://www.robolink.co.kr/web/cate02/product03.php)   
- __Size__ : 191mm x 191mm x 55mm
- __Weight__ : 127g     
- __Communication Type__ : RF  
- __Sensors__ : Optical flow sensor, Triaxial gyro sensor, Triaxial acceleration sensor, Barometric pressure sensor, Temperature sensor, Altitude sensor 
- __Modes__ :  Mode 1, Mode 2
</br></br></br>

## I-3. Raspberry Pi OS Installation
### 1. <img src="https://user-images.githubusercontent.com/82248453/125610457-3bde1b44-f55f-4abe-8397-5a522fdedbfc.jpg" width="20" height="20"> Download Raspberry Pi OS Lite
[Downloads](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit)

### 2. Install Raspberry Pi imager
[Downloads](https://www.raspberrypi.org/software/)

### 3. Install Raspberry Pi OS on SD Card
* Connect the SD card to the PC and install Raspberry Pi OS.
<img src="https://user-images.githubusercontent.com/82248453/125612251-514795d4-c74c-4849-9317-b554948dce30.png" width="400" height="300">


</br></br>

## I-4. PC Softwares
* ### Edit Python codes</br>
  <img src="https://user-images.githubusercontent.com/82248453/125473710-f3ad6de2-7c29-4670-8808-577a3ed86872.png" width="20" height="20"> [VSCode](https://code.visualstudio.com/Download)


* ### File transfer to Raspberry Pi</br>
  <img src="https://user-images.githubusercontent.com/57785792/87244655-9221d880-c479-11ea-9f17-bd71250f5528.jpg" width="20" height="20"> [Win SCP](https://winscp.net/eng/docs/lang:ko)

* ### Communicate with Raspberry Pi</br>
  <img src="https://user-images.githubusercontent.com/57785792/87244362-a95fc680-c477-11ea-9a8d-75ccf17f3cb1.png" width="20" height="20"> [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/)
<br/>

## __I-5. Drone Operation__
* Control drones with Python codes.
<table>
  <tr>
    <th></th>
    <th>object</th>
    <th>Drone()</th>
  </tr>
  <tr>
    <td rowspan="2">takeoff / landing </td>
    <td>takeoff</td>
    <td>sendTakeOff()</td>
  </tr>
  <tr>
    <td>landing</td>
    <td>sendLanding()</td>
  </tr>
  <tr>
    <td rowspan="2">direction / velocity</td>
    <td rowspan="2">moving</td>
    <td>sendControlPosition16()</td>
  </tr>
  <tr>
    <td>sendControlWhile()</td>
  </tr>
</table>
<br/></br>

```python
def sendControlPosition(self, positionX, positionY, positionZ, velocity, heading, rotationalVelocity):
   ```
   
 | variable | type | range | unit | explanation |
   |:---------:|:----:|:----:|:---:|:---:|
   |position X|Int16|-100 ~ 100(-10.0 ~ 10.0)|meter x 10|forward(+), back(-)|
   |position Y|Int16|-100 ~ 100(-10.0 ~ 10.0)|meter x 10|left(+), right(-)|
   |position Z|Int16|-100 ~ 100(-10.0 ~ 10.0)|meter x 10|up(+), down(-)|
   |velocity|Int16|5~200(0.5 ~ 2.0)|m/s x 10|moving velocity|
   |heading|Int16|-360 ~ 360|degree|left rotate(+), right rotate(-)|
   |rotationalVelocity|Int16|10 ~ 360|degree/s|rotational velocity|


<br/></br>

## __I-6. Track Making__
* <b style="font-size:20px; font-weight:450;">Specifications for Contest</b>

<img src="https://user-images.githubusercontent.com/82248453/125471207-707e75a5-1718-474f-b1ae-1175ddf4ef5b.png" width="400" height="500">
</br>
</br>

* <b style="font-size:20px; font-weight:450;">Parts</b>

[Chroma key cloth](http://prod.danawa.com/info/?pcode=6236910&keyword=촬영+배경천+크로마키천&cate=12237571) x 3</br>
[Tripod](https://smartstore.naver.com/tentosix/products/5235400713?) x 6</br>
[Crossbar](http://shopping.interpark.com/product/productInfo.do?prdNo=7793992496&dispNo=016001&bizCd=P01397&NaPm=ct%3Dkmw2mo80%7Cci%3Dacf29c276c2b6716805b8868a1494b6bf00965fa%7Ctr%3Dslsl%7Csn%3D3%7Chk%3D3d37d1ee7ba040be32a802a26768c0d771db0c84&utm_medium=affiliate&utm_source=naver&utm_campaign=shop_p11714_p01397&utm_content=price_comparison) x 3
</br>
</br>

* <b style="font-size:20px; font-weight:450;">Making Tracks</b>

<img src="https://user-images.githubusercontent.com/82248453/125423603-8e42aab3-ac43-460d-a8ef-b855bdb75acf.jpg" width="400" height="300"> <img src="https://user-images.githubusercontent.com/82248453/125424121-7023391c-4bf7-4415-9a2b-db634b1b25a1.jpg" width="400" height="300">

<img src="https://user-images.githubusercontent.com/82248453/125424674-a3ae7c92-cec5-49f4-9ed3-9425fe3c7a5d.jpg" width="400" height="300"> <img src="https://user-images.githubusercontent.com/82248453/125552424-a0a81180-219f-455b-9814-2a131f44d6c0.jpg" width="400" height="300">
</br>


Made after renting a classroom on campus.
</br></br>


# II. Algorithms
<img src="https://user-images.githubusercontent.com/82248453/125609037-c0ed67d0-ef91-45c4-8cc5-6942ed9ce419.png" width="700" height="800">
</br>
</br>
</br>

## II-1. Track Analysis

<img src="https://user-images.githubusercontent.com/82248453/125550832-74bab068-4126-4fe5-976d-f1f772bc3fa4.png" width="500" height="300">

1. Determine straight distance according to distance from ring.
2. Position drones at specific points.
3. Detect the color after passing through the ring.
4. Run action according to color determined.</br></br></br>

## II-2. Modes Depending on Image
* Change straight moving modes according to number of pixels detected depending on the distance from the ring.

<img src="https://user-images.githubusercontent.com/82248453/125550769-cb07fd81-3a4e-478d-9170-f26e9d4041fa.png" width="500" height="300"></br></br></br>



## II-3. Total Algorithms

<img src="https://user-images.githubusercontent.com/82248453/125550607-1123ca6e-55e3-4d26-a711-a60f86313144.png" width="500" height="300"></br></br></br>
# III. Codes
* ## Module Specifications for Contest

      e-drone==21.1.6
      numpy==1.16.2
      Pillow==5.4.1
      opencv==3.2.0
<br/>

* ## Codes

### III-1. __Image Processing__

1-a) Original image
* Original images taken with the camera connected to Raspberry Pi on drone at each point.</br>
<img src="https://user-images.githubusercontent.com/82248453/125552837-f332c92c-dbec-4803-bd4f-3e6221016143.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125553173-6612c8a7-3600-43f6-8b59-7497ce783d87.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125553629-76d5b75a-4cbf-4784-9f06-99bbc3484a56.jpg" width="250" height="200">
</br>
1-b) Setting threshold value

* Use the toolbar code to find appropriate threshold values.
<img src="https://user-images.githubusercontent.com/82248453/125587887-ffa033d9-4012-444c-85ec-87c314f692a5.jpg" width="800" height="400"></br>
</br>

* Set threshold values.
```python
lower_blue = (95, 0, 50)  
upper_blue = (110, 255, 250)

lower_red = (0, 0, 5)  
upper_red = (17, 255, 240)

lower_purple = (110, 0, 5)
upper_purple = (140, 255, 50)

```

</br></br>

1-c) Converting to HSV
* Convert the original images at each point to HSV.
```python 
img = frame.array
img = cv2.flip(img, 0)
img = cv2.flip(img, 1)
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```
<img src="https://user-images.githubusercontent.com/82248453/125552923-85a17d88-fdd7-454c-b7de-7e265bf5aab0.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125561490-7002e91e-b9f7-4ec0-af60-f0c3b3fcb1c7.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125561509-66364cd8-4eef-4c5a-9792-1de0ab5c5275.jpg" width="250" height="200">


</br></br>


1-d) Applying threshold value
* Apply each threshold value to images converted to HSV.
```python
imgH_B = cv2.inRange(imghsv, lower_blue, upper_blue)
imgH_R = cv2.inRange(imghsv, lower_red, upper_red)
imgH_P = cv2.inRange(imghsv, lower_purple, upper_purple)
```
<img src="https://user-images.githubusercontent.com/82248453/125552991-d0c0d227-8467-49d0-840e-fb9797eadf63.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125553194-2fddd243-2867-4914-a37a-e71728d6cbf5.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125555697-200ff218-ff6c-482e-a4da-cf5b930dc436.jpg" width="250" height="200">

</br></br>

1-e) Applying MedianBlur
* Use MedianBlur to remove noise.
```python
tmpB = cv2.medianBlur(imgH_B, 21)
tmpR = cv2.medianBlur(imgH_R, 7)
tmpP = cv2.medianBlur(imgH_P, 7)
```

<img src="https://user-images.githubusercontent.com/82248453/125553021-667ac56c-0d60-45e6-b6d5-c79778647c0b.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125553184-32ad7384-902a-4d25-97b5-e669905ec840.jpg" width="250" height="200"> <img src="https://user-images.githubusercontent.com/82248453/125555708-32025ccf-d351-4c88-b174-3e98a70593d7.jpg" width="250" height="200">

</br></br></br>

### III-2. __Controlling Drone__

2-a) Modes depending on blue pixel value.

* Determine the distance from the ring and define modes by sum of blue pixels
```python
mode = {1:[range(100, 30000), range(30000, 100000), range(100000, 150000), 150000], 
        2:[range(100, 50000), range(50000, 120000), range(120000, 170000), 170000], 
        3:[range(100, 70000), range(70000, 140000), range(140000, 200000), 200000]}
```
</br></br>
2-b) Straight move
* Detemine moving velocity and distance according to the distance to the ring.

```python
def moveLarge(drone, BlueSum):
    #이동 11
    print(f"move Large / BlueSum : {BlueSum}")            
    drone.sendControlPosition16(11, 0, 0, 6, 0, 0)
    sleep(4)
        

def moveSoso(drone, BlueSum):
    #이동 8
    print(f"move soso / BlueSum : {BlueSum}")
    drone.sendControlPosition16(8, 0, 0, 5, 0, 0)
    sleep(4)

```

</br></br>

2-c) Close to the ring
* Position and move according to the close distance to the ring.
```python
def moveSmall(drone, BlueSum, dist_x, dist_y):
    #이동 6
    print(f"move small / BlueSum : {BlueSum}")
    if (dist_x == 0 and dist_y == 0):
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)
                
    elif (dist_x != 0 and dist_y == 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)
    
    elif (dist_x == 0 and dist_y != 0):
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)
                    
    elif (dist_x != 0 and dist_y != 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)


def move2Small(drone, BlueSum, dist_x, dist_y):
    #속도 4
    print(f"move 2 Small / BlueSum : {BlueSum}")
    if (dist_x == 0 and dist_y == 0):
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)
                
    elif (dist_x != 0 and dist_y == 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)
    
    elif (dist_x == 0 and dist_y != 0):
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)
                    
    elif (dist_x != 0 and dist_y != 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)
```

</br></br>

2-d) Determining location of drone
* Detect difference in blue pixel number after split the image into four(top, bottom, left, right).

```python
def detectDist(tmpB):
    tmpB_div_1 = tmpB[:240, :320]
    tmpB_div_2 = tmpB[240:, :320]
    tmpB_div_3 = tmpB[:240, 320:]
    tmpB_div_4 = tmpB[240:, 320:]

    tmpB_div_1 = np.sum(tmpB_div_1 == 255, axis = None)
    tmpB_div_2 = np.sum(tmpB_div_2 == 255, axis = None)
    tmpB_div_3 = np.sum(tmpB_div_3 == 255, axis = None)
    tmpB_div_4 = np.sum(tmpB_div_4 == 255, axis = None)
    
    dist_x = (tmpB_div_3 + tmpB_div_4) - (tmpB_div_1 +tmpB_div_2)
    dist_y = (tmpB_div_4 + tmpB_div_2) - (tmpB_div_3 +tmpB_div_1)
    
    return (dist_x, dist_y)
```

</br></br>

2-e) Inside the ring
* Move forward and operate(rotate 90/landing) after color detection(red/purple) inside the ring.
```python
if (BlueSum < Dmode[0][0]):
    #링 내부로 들어왔다는 뜻
    print(f"inside ring / BlueSum : {BlueSum}")
    
    imgH_R = cv2.inRange(imghsv, lower_red, upper_red)
    imgH_P = cv2.inRange(imghsv, lower_purple, upper_purple)
    tmpR = cv2.medianBlur(imgH_R, 7) # 좌회전을 판단할 점 요소
    tmpP = cv2.medianBlur(imgH_P, 7)
    RedSum = np.sum(tmpR == 255, axis = None)
    PurpleSum = np.sum(tmpP == 255, axis = None)

    if (RedSum != 0 and level_cnt != 3):
        if (RedSum < 200):
            print(f"detect red / BlueSum : {BlueSum}")
            drone.sendControlPosition16(4, 0, 0, 4, 0, 0)
            sleep(4)
            drone.sendControlPosition16(0, 0, 0, 0, 90, 20)
            sleep(6)
            level_cnt += 1
            print("red, rotate complete, now level_cnt:", level_cnt)
            Dmode = mode[level_cnt]
            no_trap = True
            drone.sendControlPosition16(10,0,0,5,0,0)
            sleep(5)
            continue

        else:
            print(f"detect red / BlueSum : {BlueSum}")
            drone.sendControlPosition16(3, 0, 0, 3, 0, 0)
            sleep(4)
            drone.sendControlPosition16(0, 0, 0, 0, 90, 20)
            sleep(6)
            level_cnt += 1
            print("red, rotate complete, now level_cnt:", level_cnt)
            Dmode = mode[level_cnt]
            no_trap = True
            drone.sendControlPosition16(10,0,0,5,0,0)
            sleep(5)
            continue

        
    elif (RedSum == 0 and PurpleSum != 0 or level_cnt == 3):
        print("purple")
        drone.sendLanding()
        drone.close()
        break



    else:
        #둘다 노이즈로 판명난 경우엔 다시 검출을 합니다
        continue
```

</br></br>

2-f) Out of ring

* Run straight moving functions according to the distance to the ring.
```python
if (BlueSum < Dmode[0][0]):...
else:
    # 링 외부에 있다는 뜻
    print(f"out of ring / BlueSum : {BlueSum}")

    (dist_x, dist_y) = detectDist(tmpB)
    
    if (BlueSum in Dmode[0]):               
	#링 경계   
        if (BlueSum - lastBluesum >= 0 and no_trap):
            #현재 - 과거 픽셀이며, 양수면 매우 멀리있는 경우이므로 moveLarge 모드로 더 다가가야 함
            moveLarge(drone, BlueSum)

        else:
            #음수면 링과 매우 근접한 경우이므로, 조금만 움직여야 함.
            move2Small(drone, BlueSum, dist_x, dist_y)
        lastBluesum = BlueSum
        continue
    
    elif (BlueSum in Dmode[1]):
        if (BlueSum - lastBluesum >= 0):
            moveSoso(drone, BlueSum)
            no_trap = False
        else:
            moveSoso(drone, BlueSum)
            no_trap = False

        lastBluesum = BlueSum
        continue

    
    elif (BlueSum in Dmode[2]):
        if (BlueSum - lastBluesum >= 0):
            moveSmall(drone, BlueSum, dist_x, dist_y)
            no_trap = False
        else:
            move2Small(drone, BlueSum, dist_x, dist_y)
            no_trap = False
        
        lastBluesum = BlueSum
        continue


    elif (BlueSum >= Dmode[3]):
        moveSmall(drone, BlueSum, dist_x, dist_y)
        lastBluesum = BlueSum
        continue

    else:
        continue
```
</br></br>
### III-3. __Full Code__
* Run `main.py` code in Raspberry Pi.
```python
from e_drone.drone import *
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import numpy as np
import cv2



lower_blue = (95, 0, 50)  
upper_blue = (110, 255, 250)

lower_red = (0, 0, 5)  
upper_red = (17, 255, 240)

lower_purple = (110, 0, 5)
upper_purple = (140, 255, 50)


level_cnt = 1
no_trap = True

mode = {1:[range(100, 30000), range(30000, 100000), range(100000, 150000), 150000], 
        2:[range(100, 50000), range(50000, 120000), range(120000, 170000), 170000], 
        3:[range(100, 70000), range(70000, 140000), range(140000, 200000), 200000]}  # [min,max]

lastBluesum = 0

def moveLarge(drone, BlueSum):
    #이동 11
    print(f"move Large / BlueSum : {BlueSum}")            
    drone.sendControlPosition16(11, 0, 0, 6, 0, 0)
    sleep(4)
        

def moveSoso(drone, BlueSum):
    #이동 8
    print(f"move soso / BlueSum : {BlueSum}")
    drone.sendControlPosition16(8, 0, 0, 5, 0, 0)
    sleep(4)
   
                    
def moveSmall(drone, BlueSum, dist_x, dist_y):
    #이동 6
    print(f"move small / BlueSum : {BlueSum}")
    if (dist_x == 0 and dist_y == 0):
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)
                
    elif (dist_x != 0 and dist_y == 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)
    
    elif (dist_x == 0 and dist_y != 0):
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)
                    
    elif (dist_x != 0 and dist_y != 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(6, 0, 0, 4, 0, 0)
        sleep(3)


def move2Small(drone, BlueSum, dist_x, dist_y):
    #속도 4
    print(f"move 2 Small / BlueSum : {BlueSum}")
    if (dist_x == 0 and dist_y == 0):
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)
                
    elif (dist_x != 0 and dist_y == 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)
    
    elif (dist_x == 0 and dist_y != 0):
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)
                    
    elif (dist_x != 0 and dist_y != 0):
        drone.sendControlPosition16(0, dist_x//abs(dist_x), 0, 1, 0, 0)
        sleep(3)
        drone.sendControlPosition16(0, 0, 2*(dist_y//abs(dist_y)), 2, 0, 0)
        sleep(3)
        drone.sendControlPosition16(4, 0, 0, 3, 0, 0)
        sleep(3)

def detectDist(tmpB):
    tmpB_div_1 = tmpB[:240, :320]
    tmpB_div_2 = tmpB[240:, :320]
    tmpB_div_3 = tmpB[:240, 320:]
    tmpB_div_4 = tmpB[240:, 320:]

    tmpB_div_1 = np.sum(tmpB_div_1 == 255, axis = None)
    tmpB_div_2 = np.sum(tmpB_div_2 == 255, axis = None)
    tmpB_div_3 = np.sum(tmpB_div_3 == 255, axis = None)
    tmpB_div_4 = np.sum(tmpB_div_4 == 255, axis = None)
    
    dist_x = (tmpB_div_3 + tmpB_div_4) - (tmpB_div_1 +tmpB_div_2)
    dist_y = (tmpB_div_4 + tmpB_div_2) - (tmpB_div_3 +tmpB_div_1)
    
    return (dist_x, dist_y)


drone = Drone()
drone.open()

try:
    drone.sendTakeOff()
    sleep(5)
    drone.sendControlPosition16(11,0,0,5,0,0)
    sleep(5) 

    camera = PiCamera() 
    camera.resolution = (640, 480) 
    camera.framerate = 32 
    rawCapture = PiRGBArray(camera, size=(640, 480))
    Dmode = mode[level_cnt] 

    for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
        img = frame.array
        img = cv2.flip(img, 0)
        img = cv2.flip(img, 1)
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        imgH_B = cv2.inRange(imghsv, lower_blue, upper_blue)

        rawCapture.truncate(0)

        tmpB = cv2.medianBlur(imgH_B, 21) # 파란색 링에 medianBlur 적용한 이미지
        
        BlueSum = np.sum(tmpB == 255, axis = None) # 파란색링의 이미지
        print(f"first BlueSum : {BlueSum}")
        
        if (BlueSum < Dmode[0][0]):
            #링 내부로 들어왔다는 뜻
            print(f"inside ring / BlueSum : {BlueSum}")
            
            imgH_R = cv2.inRange(imghsv, lower_red, upper_red)
            imgH_P = cv2.inRange(imghsv, lower_purple, upper_purple)
            tmpR = cv2.medianBlur(imgH_R, 7) # 좌회전을 판단할 점 요소
            tmpP = cv2.medianBlur(imgH_P, 7)
            RedSum = np.sum(tmpR == 255, axis = None)
            PurpleSum = np.sum(tmpP == 255, axis = None)


            if (RedSum != 0 and level_cnt != 3):
                #일단 노이즈 없이 검출 되는 경우
                if (RedSum < 200):
                    print(f"detect red / BlueSum : {BlueSum}")
                    drone.sendControlPosition16(4, 0, 0, 4, 0, 0)
                    sleep(4)
                    drone.sendControlPosition16(0, 0, 0, 0, 90, 20)
                    sleep(6)
                    level_cnt += 1
                    print("red, rotate complete, now level_cnt:", level_cnt)
                    Dmode = mode[level_cnt]
                    no_trap = True
                    drone.sendControlPosition16(10,0,0,5,0,0)
                    sleep(5)
                    continue

                else:
                    print(f"detect red / BlueSum : {BlueSum}")
                    drone.sendControlPosition16(3, 0, 0, 3, 0, 0)
                    sleep(4)
                    drone.sendControlPosition16(0, 0, 0, 0, 90, 20)
                    sleep(6)
                    level_cnt += 1
                    print("red, rotate complete, now level_cnt:", level_cnt)
                    Dmode = mode[level_cnt]
                    no_trap = True
                    drone.sendControlPosition16(10,0,0,5,0,0)
                    sleep(5)
                    continue

                
            elif (RedSum == 0 and PurpleSum != 0 or level_cnt == 3):
                print("purple")
                drone.sendLanding()
                drone.close()
                break



            else:
                #둘다 노이즈로 판명난 경우엔 다시 검출을 합니다
                continue  

        else:
            # 링 외부에 있다는 뜻
            print(f"out of ring / BlueSum : {BlueSum}")

            (dist_x, dist_y) = detectDist(tmpB)
            
            if (BlueSum in Dmode[0]):               
                #링 경계   
                if (BlueSum - lastBluesum >= 0 and no_trap):
                    #현재 - 과거 픽셀이며, 양수면 매우 멀리있는 경우이므로 moveLarge 모드로 더 다가가야 함
                    moveLarge(drone, BlueSum)

                else:
                    #음수면 링과 매우 근접한 경우이므로, 조금만 움직여야 함.
                    move2Small(drone, BlueSum, dist_x, dist_y)
                lastBluesum = BlueSum
                continue
            
            elif (BlueSum in Dmode[1]):
                if (BlueSum - lastBluesum >= 0):
                    moveSoso(drone, BlueSum)
                    no_trap = False
                else:
                    moveSoso(drone, BlueSum)
                    no_trap = False

                lastBluesum = BlueSum
                continue

            
            elif (BlueSum in Dmode[2]):
                if (BlueSum - lastBluesum >= 0):
                    moveSmall(drone, BlueSum, dist_x, dist_y)
                    no_trap = False
                else:
                    move2Small(drone, BlueSum, dist_x, dist_y)
                    no_trap = False
                
                lastBluesum = BlueSum
                continue


            elif (BlueSum >= Dmode[3]):
                moveSmall(drone, BlueSum, dist_x, dist_y)
                lastBluesum = BlueSum
                continue

            else:
                continue

except Exception as e:
    print("exception")
    drone.sendLanding()
    drone.close()
```

</br></br>
# IV. Team Members
* **Leader** : [Minseok Park](https://github.com/rakimmayers/himdrong_parkminseok)

* **Members** : [Wonwoo Lee](https://github.com/wwonoo/himdrong_leewonwoo), [Seoyeon Jang](https://github.com/OREOCHIZ/miniDrone2021HW.git) 