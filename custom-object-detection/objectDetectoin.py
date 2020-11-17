import cv2

################################################################
path = 'haarcascades/pipe.xml'  # PATH OF THE CASCADE
cameraNo = 1                       # CAMERA NUMBER
videoPath = "../videos/789-779-line.mp4"
objectName = 'Pipe'       # OBJECT NAME TO DISPLAY
frameWidth= 640                     # DISPLAY WIDTH
frameHeight = 360                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################


# cap = cv2.VideoCapture(videoPath)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result", 0)
cv2.resizeWindow("Result",frameWidth,frameHeight + 100)
cv2.createTrackbar("Scale","Result",475,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",10000,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)

# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    # cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    # cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    # success, img = cap.read()

    img = cv2.imread("/Users/inger/underground/datasets/obstacle/010018.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray,scaleVal, neig)
    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area >minArea:
            # cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            (x, y), radius = (w/2 + x, h/2 + y), max(w,h)/2
            x = int(x)
            y = int(y)
            center = (x, y)
            radius = int(radius)
            cv2.circle(img, center, radius, color, 3)
            cv2.putText(img,objectName,(x + int(radius*0.75), y+radius),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

            roi_color = img[y:y+h, x:x+w]

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
