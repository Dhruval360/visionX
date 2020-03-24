#Empty spot finder
import cv2
import numpy as np
import imutils
#Because : Darkness
flag1 = 1
def empty():
    def nothing(x):
        pass

    #cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture("http://192.168.43.1:8080/video") #Dhruval's phone
    #cap2 = cv2.VideoCapture("http://192.168.43.182:8080/video")#Pranav's phone
    cap2 = cap1
    cams = [cap1, cap2]

    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("Lower H", "Trackbars", 0, 180, nothing)
    cv2.createTrackbar("Lower S", "Trackbars", 155, 255, nothing)
    cv2.createTrackbar("Lower V", "Trackbars", 153, 255, nothing)
    cv2.createTrackbar("Upper H", "Trackbars", 180, 180, nothing)
    cv2.createTrackbar("Upper S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("Upper V", "Trackbars", 255, 255, nothing)

    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        outs = []
        l_h = cv2.getTrackbarPos("Lower H", "Trackbars")
        l_s = cv2.getTrackbarPos("Lower S", "Trackbars")
        l_v = cv2.getTrackbarPos("Lower V", "Trackbars")
        u_h = cv2.getTrackbarPos("Upper H", "Trackbars")
        u_s = cv2.getTrackbarPos("Upper S", "Trackbars")
        u_v = cv2.getTrackbarPos("Upper V", "Trackbars")

        lower_red = np.array([l_h, l_s, l_v])
        upper_red = np.array([u_h, u_s, u_v])

        kernel = np.ones((5, 5), np.uint8)
        
        for cam in cams:
            _, frame = cam.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_red, upper_red)
            mask = cv2.erode(mask, kernel)

            # Contours detection
            if int(cv2.__version__[0]) > 3:
                # Opencv 4.x.x
                contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            else:
                # Opencv 3.x.x
                _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
                x = approx.ravel()[0]
                y = approx.ravel()[1]

                if area > 300: #Was 400 earlier
                    cv2.drawContours(frame, [approx], 0, (0, 255, 0), 10)

                    if len(approx) == 3:
                        cv2.putText(frame, "Empty", (x, y), font, 1, (0, 255, 0))

            image = imutils.resize(frame, width=300)
            outs.append(image)
        #cv2.imshow("Frame", frame)
        #cv2.imshow("Mask", mask) 
        
        output = np.vstack(outs)
        loc =  output.shape
        cv2.circle(output, (loc[0]//2+125, loc[1]//2+15), 4, (255,255,255), -1)
        cv2.putText(output, "You are here-->", (loc[0]//2-75, loc[1]//2+19), font, 0.7, (255, 255, 255), 2)
        cv2.putText(output, "Empty spots are marked", (0,15), font, 0.7, (255,255,255), 2)
        cv2.putText(output, "green", (0,30), font, 0.7, (0,255,0), 2)
        cv2.imshow('Numpy Vertical', output)
        if flag1:
            cv2.imwrite('out.jpg',output) 
            global flag
            flag = 0
        
        key = cv2.waitKey(1) #Take input from sensor
        if key == 27:
            break
    for cam in cams:
        cam.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    empty()
