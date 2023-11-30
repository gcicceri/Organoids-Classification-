import cv2
import numpy as np
import os
import time

def extract_objects(image_path, annotations_txt, output_folder):
    # Read the original image
    image = cv2.imread(image_path)

    # Check if the image was read correctly.
    if image is None:
        print(f"Errore: impossibile leggere l'immagine {image_path}")
        return

    # Get the size of the image.
    img_height, img_width, _ = image.shape

    with open(annotations_txt, 'r') as f:
        annotations = f.readlines()

    for idx, annotation in enumerate(annotations):
        # Split the annotation into class_id, x_center, y_center, width e height
        data = annotation.strip().split(' ')
        class_id, x_center, y_center, width, height = map(float, data)

        # Calculate the coordinates of the rectangle
        x1 = int((x_center - width / 2) * img_width)
        y1 = int((y_center - height / 2) * img_height)
        x2 = int((x_center + width / 2) * img_width)
        y2 = int((y_center + height / 2) * img_height)

        # Extract the object from the original image.
        object_image = image[y1:y2, x1:x2]
        
        # Check if the object image is empty.
        if object_image.size == 0:
            print(f"Errore: l'immagine dell'oggetto estratta è vuota per {image_path}")
            continue

        # Create a folder specific to the current class_id, if it does not exist.
        class_folder = os.path.join(output_folder, str(int(class_id)))
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)

        # Save the extracted object as a separate image in the class_id folder.
        #output_path = f"{class_folder}/{data}_{class_id}_{idx}.png"
        #cv2.imwrite(output_path, object_image)
        
        # Save the extracted object as a separate image in the class_id folder.
        unique_id = int(time.time() * 1000000)
        # Resize the object image to 224x224 pixels.
        resized_object_image = cv2.resize(object_image, (224, 224))
        output_path = f"{class_folder}/{unique_id}_class_{class_id}_{idx}.png"
        cv2.imwrite(output_path, resized_object_image)

# Input and output folders
images_folder = '/Users/giovannicicceri/Desktop/organoids_experiments/images/'
labels_folder = '/Users/giovannicicceri/Desktop/organoids_experiments/labels/'
output_folder = '/Users/giovannicicceri/Desktop/organoids_experiments/output/'

# List all files in image and annotation folders.
image_files = sorted(os.listdir(images_folder))
annotation_files = sorted(os.listdir(labels_folder))

# Make sure the image and annotation folders contain the same number of files.
assert len(image_files) == len(annotation_files)

counter = 0
# Iteration on all pairs of images and annotations.
for image_file, annotation_file in zip(image_files, annotation_files):
    image_path = os.path.join(images_folder, image_file)
    annotations_txt = os.path.join(labels_folder, annotation_file)
    
    extract_objects(image_path, annotations_txt, output_folder)
    print ('ok')
    # Increases the counter and prints its value.
    counter += 1
    print(f"Process {counter} pairs of images and annotations.")

