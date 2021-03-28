Scan barcode lottery to deploy on website

Step to run:

pip install virtualenvwrapper-win //ติดตั้งตัวสร้าง env
mkvirtualenv //สร้าง env แทนชื่อที่ต้องการ
workon //เข้าไปใน env ที่สร้าง
pip install -r requirements.txt //ติดตั้ง library ที่ใช้
python manage.py runserver //จะได้ตัว host server ที่เป็น localhost
python opencv_barcode.py // รันตัวกล้องที่จะใช้อ่าน lottery กดตัว q เพื่อออกจากกล้อง
Feature of program:

Read lottery barcode
data reading in realtime
Not repeat value in database
Can delete data in database
Sound alert when barcode has been scaned