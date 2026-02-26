import time

import cv2
import base64

from datetime import datetime
from pyzbar.pyzbar import decode

#starting the webcam
cap = cv2.VideoCapture(0)
names = []

#function for attendance file
attendance_filename = f'data/attendance/{datetime.now().strftime("%Y%m%d-%H:%M:%S")}.csv'

def enterData(data, plain_data):
    if data in names:
        pass
    else:
        names.append(data)
        with open(attendance_filename , 'a+') as fob:
            fob.write(f'{plain_data},{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

        return names

print("Reading the scanned QR code....")

#function data present or not
def checkData(data):
    plain_data = plain(data)
    data = str(data)
    if data in names:
        print("You have already been marked present..")
    else:
        print('\n'+str(len(names)+1)+'\n'+'You have been marked present')
        enterData(data, plain_data)

def plain(data):
    s = data.decode()
    base64_str = s[2:-1]
    decoded_bytes = base64.b64decode(base64_str)
    decoded_text = decoded_bytes.decode("utf-8")
    return decoded_text


while True:
    _ , frame = cap.read()
    decodeObject = decode(frame)
    for obj in decodeObject:
        checkData(obj.data)
        print("Your roll number: ", plain(obj.data))
        time.sleep(1)
    cv2.imshow('Frame', frame)

    #closing the webcam
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break
