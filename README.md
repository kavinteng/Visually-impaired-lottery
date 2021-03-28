# barcode-lottery
Scan barcode lottery to deploy on website

Step to run:
1. pip install virtualenvwrapper-win //ติดตั้งตัวสร้าง env
2. mkvirtualenv ชื่อ //สร้าง env 
3. workon ชื่อ //เข้าไปใน env ที่สร้าง
4. pip install -r requirements.txt //ติดตั้ง library ที่ใช้
5. python manage.py runserver //จะได้ตัว host server ที่เป็น localhost
6. python opencv_barcode.py // รันตัวกล้องที่จะใช้อ่าน lottery กดตัว q เพื่อออกจากกล้อง


Feature of program:
1. Read lottery barcode
2. data reading in realtime
3. Not repeat value in database
4. Can delete data in database
5. Sound alert when barcode has been scaned
