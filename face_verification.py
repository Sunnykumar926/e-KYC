import face_recognition
from deepface import DeepFace
import numpy as np
import cv2
import os
import logging
from utils import file_exists, read_yaml

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir,"ekyc_logs.log"), level=logging.INFO, format=logging_str, filemode="a")


config_path = "config.yaml"
config = read_yaml(config_path)

artifacts = config['artifacts']
cascade_path = artifacts['HAARCASCADE_PATH']
output_path = artifacts['INTERMIDEIATE_DIR']

def detect_and_extract_face(img):
    
    # convert the image into grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # intialize the haar cascade classifier
    cascade_clf = cv2.CascadeClassifier(cascade_path)

    # detect the faces in the image
    faces, confidence = cascade_clf.detectMultiScale2(gray_img, minNeighbors=5, scaleFactor=1.1)

    # find the faces with the large area
    max_area = 0
    largest_face=None
    for (x, y, w, h) in faces:
        area = w*h
        if max_area < area:
            max_area = area
            largest_face = (x, y, w, h)
            
    # Extract the largest face
    if largest_face is not None:
        x, y, w, h = largest_face

        # extracted_face = img[y:y+h, x:x+w]

        # Increased dimensions by 15%
        new_w = int(w*1.5)
        new_h = int(h*1.5)

        # Calculate the new (x, y) coordinates to keep the center of the face the same
        new_x = max(0, x-int((new_w-w)/2))
        new_y = max(0, y-int((new_h-h)/2))

        # Extract the enlarge image
        # print(f"{x}, {y}")
        extract_face = img[new_y:new_y+new_h, new_x:new_x+new_w]


        pwd = os.getcwd()
        filename = os.path.join(pwd, output_path, 'extacted_face.jpg')

        if os.path.exists(filename):
            os.remove(filename)

        cv2.imwrite(filename, extract_face)
        print(f'Extracted Face saved at: {filename}')
        return filename
    else:
        return None

def face_recog_face_comparison(image1_path="data/02_intermediate_data/extacted_face.jpg", image2_path = "data/02_intermediate_data/face_image.jpg"):

    img1_exists = file_exists(image1_path)
    img2_exists = file_exists(image2_path)

    if img1_exists:
        print('Yep! image1 exist')
    if img2_exists:
        print('Yep! image2 exist')
    
    if not (img1_exists and img2_exists):
        print("Check the path for the images provided")
        return False

    image1 = face_recognition.load_image_file(image1_path)
    image2 = face_recognition.load_image_file(image2_path)

    if image1 is not None and image2 is not None:
        face_encodings1 = face_recognition.face_encodings(image1)
        face_encodings2 = face_recognition.face_encodings(image2)

    else:
        print("Image is not loaded properly")
        return False


    # Check if faces are detected in both images
    if len(face_encodings1) == 0 or len(face_encodings2) == 0:
        print("No faces detected in one or both images.")
        return False
    else:
    # Proceed with comparing faces if faces are detected
        matches = face_recognition.compare_faces(np.array(face_encodings1), np.array(face_encodings2))
    # Print the results
    print(matches)
    if matches[0]:
        print("Faces are verified")
        return True
    else:
        # print("The faces are not similar.")
        return False
    
def deepface_face_comparison(image1_path="data/02_intermediate_data/extracted_face.jpg", image2_path = "data/02_intermediate_data/face_image.jpg"):
    img1_exists = file_exists(image1_path)
    img2_exists = file_exists(image2_path)

    if not(img1_exists or img2_exists):
        print("Check the path for the images provided")
        return False
    
    verfication = DeepFace.verify(img1_path=image1_path, img2_path=image2_path)

    if len(verfication) > 0 and verfication['verified']:
        print("Faces are verified")
        return True
    else:
        return False

def face_comparison(image1_path, image2_path, model_name = 'facerecognition'):

    is_verified = False
    if model_name == 'deepface':
        is_verified = deepface_face_comparison(image1_path, image2_path)
    elif model_name ==  'facerecognition':
        is_verified = face_recog_face_comparison(image1_path, image2_path)
    else:
        print("Mention proper model name for face recognition")

    return is_verified

def get_face_embeddings(image_path):

    img_exists = file_exists(image_path)

    if not(img_exists):
        print("Check the path for the images provided")
        return None
    
    embedding_objs = DeepFace.represent(img_path = image_path, model_name = "Facenet")
    embedding = embedding_objs[0]["embedding"]

    if len(embedding) > 0:
        return embedding
    return None

