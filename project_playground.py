import IPython
import zipfile
import os
import traceback
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
def get_images(zip_name, debug = False):
    zip_path = zip_name
    if zip_path.endswith(".zip"):
        zip_path = zip_name[0:len(zip_name)-4]
    if debug is True:
        print("Image path: {} exists: {}".format(zip_path, os.path.isdir(zip_path)))
    if os.path.isdir(zip_path) is False:
        zip_ref = zipfile.ZipFile(zip_name, 'r')
        zip_ref.extractall(zip_path)
        zip_ref.close()
    images = []
    for image_filename in sorted(os.listdir(zip_path)):
        image_path = zip_path+'/'+image_filename
        image = Image.open(image_path)
        if debug is True:
            print("Processing file (image to string): {} ...".format(image_filename))
        images.append([image_filename, image_path, pytesseract.image_to_string(image)])
    return images


def get_faces(pil_image, scale_factor = 1.3, min_neighbors = 5):
    cv_image = cv.imread(pil_image)
    cv_image_color = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
    return face_cascade.detectMultiScale(cv_image_color, scale_factor, min_neighbors)


def search(image_zip_name, search_text, debug = False):
    for image_tuple in get_images(image_zip_name, debug):
        search_idx = image_tuple[2].find(search_text)
        if debug is True:
            print("Index result {} of finding search text '{}' in image text '{}'".format(
                search_idx, search_text, image_tuple[2]))
        if -1 < search_idx:
            print("Results found in file {}".format(image_tuple[0]))
            try:
                if debug is True:
                    print("Generating final faces image...")
                image = Image.open(image_tuple[1])
                faces_raw = get_faces(image_tuple[1])
                if debug is True:
                    print("get_faces result: ", faces_raw)
                if 0 < len(faces_raw):
                    if debug is True:
                        print("{} faces found in image file {}".format(len(faces_raw), image_tuple[0]))
                    faces_refined = []
                    face_size = 110
                    for x, y, w, h in faces_raw:
                        faces_refined.append(image.crop((x, y, x + w, y + h)))
                    faces_final = Image.new(image.mode, (550, face_size*int(np.ceil(len(faces_refined)/5))))
                    x, y = 0, 0
                    for face in faces_refined:
                        face.thumbnail((face_size, face_size))
                        faces_final.paste(face, (x, y))
                        if x + face_size == faces_final.width:
                            x = 0
                            y = y + face_size
                        else:
                            x = x + face_size
                    IPython.display(faces_final)
                else:
                    print('But there were no faces in that file!')
            except Exception as ex:
                print("Failed to detect and process faces...")
                print(traceback.format_exc(ex))


# search('readonly/small_img.zip', 'Christopher', False)
search('readonly/images.zip', 'Mark', False)