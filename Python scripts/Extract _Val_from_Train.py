import os
import random
import shutil

# Set the source directory where the image folders are located
source_dir = "/output"
#print (source_dir)


# Set the destination directory where the train, val, and test folders will be created
dest_dir = "/val_folder"

# Set the percentages for train, val, and test splits
train_percent = 0.7
val_percent = 0.1
#test_percent = 0.2

# Create the train, val, and test directories in the destination directory
train_dir = os.path.join(dest_dir, "train_folder")
val_dir = os.path.join(dest_dir, "val_folder")
test_dir = os.path.join(dest_dir, "test_folder")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)


# Iterate over the class folders
for class_name in os.listdir(source_dir):
    class_dir = os.path.join(source_dir, class_name)

    # Check if the current item is a directory
    if not os.path.isdir(class_dir):
        continue

    # Create the label folders in train, val, and test directories
    train_class_dir = os.path.join(train_dir, class_name)
    val_class_dir = os.path.join(val_dir, class_name)
    test_class_dir = os.path.join(test_dir, class_name)

    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)

    # Get the list of image files in the current class folder
    image_files = os.listdir(class_dir)

    # Shuffle the image files randomly
    random.shuffle(image_files)

    # Calculate the number of images for each split
    num_images = len(image_files)
    num_train = int(num_images * train_percent)
    num_val = int(num_images * val_percent)

    # Split the image files into train, val, and test sets
    train_files = image_files[:num_train]
    val_files = image_files[num_train:num_train + num_val]
    test_files = image_files[num_train + num_val:]

    # Move the train files to the train class folder
    for train_file in train_files:
        src_path = os.path.join(class_dir, train_file)
        dest_path = os.path.join(train_class_dir, train_file)
        shutil.copy(src_path, dest_path)

    # Move the val files to the val class folder
    for val_file in val_files:
        src_path = os.path.join(class_dir, val_file)
        dest_path = os.path.join(val_class_dir, val_file)
        shutil.copy(src_path, dest_path)

    # Move the test files to the test class folder
    for test_file in test_files:
        src_path = os.path.join(class_dir, test_file)
        dest_path = os.path.join(test_class_dir, test_file)
        shutil.copy(src_path, dest_path)
    print ('go!')

print("Splitting and copying of images completed.")
