import cv2
from pyzbar import pyzbar
import numpy as np
import os, sys
import sqlite3

def decode(image):
    num = 0
    type = 0
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        # print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        num = obj.data
        type = obj.type
        # print("Type:", obj.type)
        # print("Data:", obj.data)
        # print()

    return image, num, type

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def main():
    cap = cv2.VideoCapture(0)
    i = 0
    num1,num2,num3 = 0,0,0
    array = []
    array2 = []
    while True:
        ret, frame_read = cap.read()
        frame_read,data, type = decode(frame_read)

        if type == 'I25':
            if data not in array and data != 0:
                mydata = data.decode('utf-8')
                if i == 0:
                    num1 = mydata
                    i += 1
                elif i == 1:
                    num2 = mydata
                    i += 1
                elif i == 2:
                    num3 = mydata
                    array.append(data)
                    i = 0
                if len(mydata) == 16 and num1 == num2 == num3:
                    print(mydata,'\007')
                    array2.append(mydata)
            elif data in array:
                pass

        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        sql_cmd = '''select * from database_lottery'''
        value_database = []

        for row in c.execute(sql_cmd):
            value_database.append(row[1])

        for data in array2:
            if data not in value_database:
                c.execute('''insert into database_lottery(num) values (?)''', (data,))
        conn.commit()

        cv2.imshow('Demo', frame_read)
        k = cv2.waitKey(1)
        if k == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            delete = input("Do you want to delete data (y/n) : ")
            if delete == 'y':
                c.execute('''delete from database_lottery where num ''')
                conn.commit()
            elif delete == 'n':
                pass
            break


if __name__ == '__main__':
    main()