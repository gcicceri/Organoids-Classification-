# -*- coding: utf-8 -*-

#Mount Google Drive to access files
from google.colab import drive
drive.mount('/content/drive')


# Import libraries for image processing and data handling
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from skimage.feature import greycomatrix, greycoprops
import pandas as pd

# Define the path to the main folder containing the images
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/features_test_images/0'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/train_folder/0'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/val_folder/0'
main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/test_folder/0'
main_folder_path

# Function to list all image files within a directory and its subdirectories
def list_image_files(directory):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_files.append(os.path.join(root, file))
    return image_files

# Get all image files in the main folder and its subdirectories
image_files = list_image_files(main_folder_path)
image_files
len(image_files)

# Function to compute geometric features of an image
import cv2
import numpy as np

def compute_geometric_features(image):
    # Threshold the image
    _, threshold = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize lists to store individual feature values
    areas = []
    perimeters = []
    convex_areas = []
    solidities = []
    equivalent_diameters = []
    irregularity_indices = []


    # Check if any contours were found
    if not contours:
        return {
            'mean_area': 0,
            'max_solidity': 0,
            'mean_equivalent_diameter': 0,
            'mean_perimeter': 0,
            'mean_irregularity_index': 0,
            'mean_convex_area': 0
        }


    # Compute geometric features for each contour
    for contour in contours:


        # Compute contour properties
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        hull = cv2.convexHull(contour)
        hull_area = cv2.contourArea(hull)


        # Compute additional geometric features
        equivalent_diameter = np.sqrt(4 * area / np.pi)
        irregularity_index = perimeter / np.sqrt(4 * np.pi * area)  # Simplified formula
        solidity = area / hull_area if hull_area != 0 else 0

        # Append the feature values to the respective lists
        areas.append(area)
        perimeters.append(perimeter)
        convex_areas.append(hull_area)
        solidities.append(solidity)
        equivalent_diameters.append(equivalent_diameter)
        irregularity_indices.append(irregularity_index)

    # Compute statistics for the features
    feature_stats = {
        'mean_area': np.mean(areas),
        'max_solidity': np.max(solidities),
        'mean_equivalent_diameter': np.mean(equivalent_diameters),
        'mean_perimeter': np.mean(perimeters),
        'mean_irregularity_index': np.mean(irregularity_indices),
        'mean_convex_area': np.mean(convex_areas)
    }

    return feature_stats


# Function to extract texture and geometric features from images
from skimage.feature import greycomatrix, greycoprops

def extract_features_from_images(image_paths):
    all_features = []
    image_number = 0

    # Loop through each image path
    for image_path in image_paths:

        image_number += 1  # Increase the image counter
        print(f"Processing image number: {image_number}, Path: {image_path}")

        # Read the image in grayscale mode
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # If the image is None (the path was invalid), continue to the next image
        if image is None:
            continue

        # Compute basic and texture features
        dimensions = image.shape
        mean_intensity = np.mean(image)
        std_intensity = np.std(image)
        histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
        glcm = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)
        contrast = greycoprops(glcm, 'contrast').flatten()
        dissimilarity = greycoprops(glcm, 'dissimilarity').flatten()
        homogeneity = greycoprops(glcm, 'homogeneity').flatten()
        energy = greycoprops(glcm, 'energy').flatten()
        correlation = greycoprops(glcm, 'correlation').flatten()

        # Compute geometric features
        geometric_features = compute_geometric_features(image)

        # Combine basic, texture, and geometric features into a single dictionary
        image_features = {
            'path': image_path,
            'dimensions': dimensions,
            'mean_intensity': mean_intensity,
            'std_intensity': std_intensity,
            'histogram': histogram,
            'contrast_0': contrast[0],
            'contrast_45': contrast[1],
            'contrast_90': contrast[2],
            'contrast_135': contrast[3],
            'dissimilarity_0': dissimilarity[0],
            'dissimilarity_45': dissimilarity[1],
            'dissimilarity_90': dissimilarity[2],
            'dissimilarity_135': dissimilarity[3],
            'homogeneity_0': homogeneity[0],
            'homogeneity_45': homogeneity[1],
            'homogeneity_90': homogeneity[2],
            'homogeneity_135': homogeneity[3],
            'energy_0': energy[0],
            'energy_45': energy[1],
            'energy_90': energy[2],
            'energy_135': energy[3],
            'correlation_0': correlation[0],
            'correlation_45': correlation[1],
            'correlation_90': correlation[2],
            'correlation_135': correlation[3],
            **geometric_features
        }

        all_features.append(image_features)

    return all_features

# Count the number of image files
print (len(image_files))


# Timing the feature extraction process
import time
start_time = time.time() # Start the timer

features_list = extract_features_from_images(image_files) # Extract features

# Stop the timer
end_time = time.time()

#  Calculate and print the total processing time
total_processing_time = end_time - start_time
print(f"Tempo totale di processamento: {total_processing_time} secondi")

# Calculate and print the average processing time per image
average_processing_time = total_processing_time / len(image_files)
print(f"Tempo medio di processamento per immagine: {average_processing_time} secondi")

# Convert the list of features into a pandas DataFrame
features_df = pd.DataFrame(features_list)

# # Prepare the DataFrame for export to Excel by removing the histogram column
features_df_export_0 = features_df.drop('histogram', axis=1)
features_df_export_0

# Assign a label '0' to each image in the dataset
features_df_export_0['label'] = 0

# Save the DataFrame to an Excel file
excel_path = 'test_image_features_0.xlsx'
features_df_export_0.to_excel(excel_path, index=False)

print (features_df_export_0)
print (len(features_df_export_0))

# Define the path to the main folder
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/features_test_images/1'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/train_folder/1'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/val_folder/1'
main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/test_folder/1'

# Function to list all image files within a directory and its subdirectories
def list_image_files(directory):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_files.append(os.path.join(root, file))
    return image_files

# Get all image files in the main folder and its subdirectories
image_files = list_image_files(main_folder_path)
image_files


# Extracting features for the image list
features_list = extract_features_from_images(image_files)

# Convert the list of features into a pandas DataFrame
features_df = pd.DataFrame(features_list)

# # Prepare the DataFrame for export to Excel by removing the histogram column
features_df_export_1 = features_df.drop('histogram', axis=1)
features_df_export_1

# # Assign a label '1' to each image in the dataset
features_df_export_1['label'] = 1

## Save the DataFrame to an Excel file
excel_path = 'test_image_features_1.xlsx'
features_df_export_1.to_excel(excel_path, index=False)

print (features_df_export_1)

print (features_df_export_1.shape)

# Define the path to the main folder
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/features_test_images/2'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/train_folder/2'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/val_folder/2'
main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/test_folder/2'

# Function to list all image files within a directory and its subdirectories
def list_image_files(directory):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_files.append(os.path.join(root, file))
    return image_files

# Get all image files in the main folder and its subdirectories
image_files = list_image_files(main_folder_path)
image_files


# # Extracting features for the image list
features_list = extract_features_from_images(image_files)

# # Convert the list of features into a pandas DataFrame
features_df = pd.DataFrame(features_list)

#Prepare the DataFrame for export to Excel by removing the histogram column
features_df_export_2 = features_df.drop('histogram', axis=1)
features_df_export_2

# # Assign a label '2' to each image in the dataset
features_df_export_2['label'] = 2

# # Save the DataFrame to an Excel file
excel_path = 'test_image_features_2.xlsx'
features_df_export_2.to_excel(excel_path, index=False)

print (features_df_export_2)

# Define the path to the main folder
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/features_test_images/3'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/train_folder/3'
#main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/val_folder/3'
main_folder_path = '/content/drive/MyDrive/ORGANOIDS_EXPERIMENTS/Final_Organoids_Dataset/test_folder/3'

# Function to list all image files within a directory and its subdirectories
def list_image_files(directory):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_files.append(os.path.join(root, file))
    return image_files

# Get all image files in the main folder and its subdirectories
image_files = list_image_files(main_folder_path)
image_files


# Extracting features for the image list
features_list = extract_features_from_images(image_files)

# Convert the list of features into a pandas DataFrame
features_df = pd.DataFrame(features_list)

# Prepare the DataFrame for export to Excel by removing the histogram column
features_df_export_3 = features_df.drop('histogram', axis=1)
features_df_export_3

# Assign a label '3' to each image in the dataset
features_df_export_3['label'] = 3

# Save the DataFrame to an Excel file
excel_path = 'test_image_features_3.xlsx'
features_df_export_3.to_excel(excel_path, index=False)
print (features_df_export_3)

print (features_df_export_0.shape)
print (features_df_export_1.shape)
print (features_df_export_2.shape)
print (features_df_export_3.shape)

#concatenate all 4 classes
concatenated_df = pd.concat([features_df_export_0, features_df_export_1, features_df_export_2, features_df_export_3], axis=0)

# Index reset
concatenated_df.reset_index(drop=True, inplace=True)
concatenated_df.info()  # Displays concatenated DataFrame information for verification

#concatenated_df.to_excel('dataset_train.xlsx', index=False)
#concatenated_df.to_excel('dataset_val.xlsx', index=False)
concatenated_df.to_excel('dataset_test.xlsx', index=False)
concatenated_df

#df = pd.read_excel('/content/dataset_train.xlsx')
#df = pd.read_excel('/content/dataset_val.xlsx')
df = pd.read_excel('/content/dataset_test.xlsx')
print (df)
