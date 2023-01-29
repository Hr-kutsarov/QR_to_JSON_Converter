# This code will
# 1. Generate a QR code
# 2. Export QR code
# 3. Convert QR code to JSON
# 4. JSON file will unpack into object
# 5. Object will be saved to a database
# 6. Database can be accessed from the browser

import qrcode
from PIL import Image
import cv2 as cv
import json


def input_method():
    # is generated by filling out a form on another device
    # we are returning a string
    return 'Product-ProductName%Quantity-10%Price-1'


def generate_qr_code():
    # gets the input as a string
    string_input = input_method()

    # creates a QR object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    # adds the data to the object
    qr.add_data(string_input)
    qr.make(fit=True)
    img = qr.make_image(
        fill_color="black",
        back_color="white")\
        .convert('RGB')

    img.save('test.png')


def get_image():
    HEIGHT = 300
    LENGTH = 300

    qr_image = Image.open('test.png')
    # set image size - optional
    qr_image.thumbnail((HEIGHT, LENGTH))
    return qr_image

def show_generated_qr_code():
    qr_image = get_image()
    qr_image.show()
    return

# returns a json object
def convert_to_json():
    IMAGE_NAME = 'test2.png'

    image = cv.imread(IMAGE_NAME)
    qrcode_detector = cv.QRCodeDetector()

    retval, decoded_info, points, straight_qrcode = qrcode_detector.detectAndDecodeMulti(image)

    # TODO test here - if retval returns true then QR code is detected

    # decoded_info is a tuple whose elements are strings stored in QR codes. If it can be detected but not decoded,
    # it is an empty string ''

    # points is a numpy.ndarray
    # representing the coordinates of the four corners of the detected QR Code.

    # straight_qrcode is a tuple whose elements are numpy.ndarray.
    # The numpy.ndarray is a binary value of 0 and 255
    # representing the black and white of each cell of the QR code.

    # pack the content of the code into a dictionary
    dict = {'Content': decoded_info}

    # create a JSON file from dictionary
    json_object = json.dumps(dict, indent=4)
    return json_object

def create_product():
    pass

def save_product():
    pass

def read_product():
    pass

def edit_product():
    pass

def delete_product():
    pass


# show_generated_qr_code()

def get_cv_version():
    print(cv.__version__)

# get_cv_version()

print(convert_to_json())