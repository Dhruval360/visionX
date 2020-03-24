#QR_Scanner:
import cv2
import requests
import numpy as np
import pyzbar.pyzbar as pyzbar
import imutils
#url1 = "http://192.168.43.1:8080/shot.jpg"
#cap = cv2.VideoCapture("http://192.168.43.1:8080/video")
def scan():
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    mes = cv2.imread('ent_ex.png')
    while True:
        '''
        img_ = requests.get(url1)
        img_a = np.array(bytearray(img_.content), dtype = np.uint8)
        frame = cv2.imdecode(img_a, -1)
        '''
        cv2.putText(mes, "Scan your QR code here".upper(), (30,100), font, 2, (255,255,255))
        cv2.imshow("", mes)
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            [p1,p2,p3,p4] = list(obj.polygon)
            #centroid = ((p1[0]+p2[0]+p3[0]+p4[0])//4, (p1[1]+p2[1]+p3[1]+p4[1])//4)
            centroid = (p1[0], (p1[1]+p2[1]+p3[1]+p4[1])//4)
            cv2.line(frame, p1, p3,(255, 0, 0), 3)
            cv2.line(frame, p2, p4,(255, 0, 0), 3)
            global output
            output = str(obj.data[0:])
            cv2.putText(frame, output , centroid, font, 1, (0,0,255))
        #cv2.imshow("Frame", frame)
        cv2.waitKey(1)
        if decodedObjects:
            print("Entry done")
            print(output)
            #entry(output)
            cv2.destroyAllWindows()
            cap.release()
            return output
            break
if __name__ == '__main__':
    scan()
