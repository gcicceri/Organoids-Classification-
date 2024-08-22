import cv2
#import numpy as np
import os
import time

def extract_objects(image_path, annotations_txt, output_folder):
    # Read the original image
    image = cv2.imread(image_path)

    # Check if the image was read correctly.
    if image is None:
        print(f"Error: unable to read image  {image_path}")
        return

    # Get the size of the image.
    img_height, img_width, _ = image.shape
    
    var_bool = 0

    with open(annotations_txt, 'r') as f:
        annotations = f.readlines()

    for idx, annotation in enumerate(annotations):
        # Dividi l'annotazione in class_id, x_center, y_center, width e height
        data = annotation.strip().split(' ')
        class_id, x_center, y_center, width, height = map(float, data)

        # Calcola le coordinate del rettangolo
        x1 = int((x_center - width / 2) * img_width)
        y1 = int((y_center - height / 2) * img_height)
        x2 = int((x_center + width / 2) * img_width)
        y2 = int((y_center + height / 2) * img_height)
        #print(x1,y1,x2,y2)
        
        # Start coordinate, here (5, 5)
        # represents the top left corner of rectangle
        start_point = (x1, y1)
          
        # Ending coordinate, here (220, 220)
        # represents the bottom right corner of rectangle
        end_point = (x2, y2)
          
        # Blue color in BGR
        color = (255, 0, 0)
          
        # Line thickness of 2 px
        thickness = 2
          
        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        image_draw = cv2.rectangle(image, start_point, end_point, color, thickness)
        

        # Extract the object from the original image.
        object_image = image[y1:y2, x1:x2]
        
        # Check if the object image is empty.
        if object_image.size == 0:
            print(data)
            print(f"Error: extracted object image is empty for {image_path}")
            var_bool =1
            continue

        # Create a folder specific to the current class_id, if it does not exist
        class_folder = os.path.join(output_folder, str(int(class_id)))
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)
            
        # Save the extracted object as a separate image in the class_id folder
        #output_path = f"{class_folder}/{data}_{class_id}_{idx}.png"
        #cv2.imwrite(output_path, object_image)
        if var_bool == 1 :
            # Save the extracted object as a separate image in the class_id folder.
            unique_id = int(time.time() * 1000000)
            # Resize the object image to 224x224 pixels.
            resized_object_image = cv2.resize(object_image, (224, 224))
            output_path = f"{class_folder}/{unique_id}_class_{class_id}_{idx}.png"
            #print(output_path)
            cv2.imwrite(output_path, resized_object_image)
            cv2.imwrite('/img_{unique_id}_class_{class_id}_{idx}_draw1.png',image_draw)

# Input and output folders
images_folder = '/images/'
labels_folder = '/labels/'
output_folder = '/train_folder/'

# List all files in image and annotation folders.
#image_files = sorted(os.listdir(images_folder))
#annotation_files = sorted(os.listdir(labels_folder))

# List all files in image and annotation folders.
image_files = sorted([f for f in os.listdir(images_folder) if f != '.DS_Store'])
annotation_files = sorted([f for f in os.listdir(labels_folder) if f != '.DS_Store'])

print (len(image_files))
print (len(annotation_files))

# Make sure the image and annotation folders contain the same number of files.
assert len(image_files) == len(annotation_files)

# Initialize counter
counter = 0
# Iteration on all pairs of images and annotations
for image_file, annotation_file in zip(image_files, annotation_files):
    image_path = os.path.join(images_folder, image_file)
    annotations_txt = os.path.join(labels_folder, annotation_file)
    
    extract_objects(image_path, annotations_txt, output_folder)
    #print ('ok')
    # Increases the counter and prints its value.
    counter += 1
    #print(f"Process {counter} pairs of images and annotations")
