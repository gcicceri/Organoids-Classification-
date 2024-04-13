# Organoids-Classification-

![1691166981456419_class_0 0_5](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/88746677-fb3a-4d3b-a193-0d402ff58a8d)
![1691166999718871_class_1 0_24](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/f981b2db-6dcd-4084-819b-8abe15181237)
![1691166984326195_class_2 0_28](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/bb3635ac-c84e-453a-8a11-b972313c5340)
![1691166997207764_class_3 0_4](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/30914409-ff2c-4768-b314-f9354e3e3164)


This repository contains the implementation of various deep learning models used in our study to classify intestinal organoids. The project evaluates several popular architectures like DenseNet169, MobileNetV2, ResNet50v2, InceptionV3, VGG16, and ViTs to determine which performs best in the organoid classification task. Within this repository, the main Python scripts for pulling the proposed DL models for the multiclassification approach can be found. The aim is to assist researchers in choosing and training a DL model for classifying organoids into appropriate classes.


## Table of Contents

1. [Getting Started](#getting-started)
2. [Building a Dataset](#building-a-dataset)
   - [Additional data](#additional-data)
3. [Model Training](#model-training)
4. [Contacts](#contacts)

## Getting Started
(Explain how to get the project up and running.)

## Building a Dataset
(Describe how to build the dataset needed for the project.)
### Additional data
(Detail any additional data that might be needed.)

## Model Training
(Instructions on how to train the models.)

## Contacts
(Your contact information or instructions on how to get in touch for help.)



## Step 1 - Data Preparation
Before training the DL models, it's necessary to prepare the data. This includes splitting the data into training, validation, and test sets from the original dataset of intestinal organoid annotated images, available at the zenodo archive **https://zenodo.org/records/6768583#.Y_S9uHbP2Uk**. Run **extract.py** and **Extract_Val_from_Train.py** inside the Python scripts folder to perform this step.
## Step 2 - Model Selection and Training 
After preparing the data, select the DL models for the training step. This repository includes six DL-model Python scripts (.ipynb). Refer to the **documentation/DL Models** folder to train the selected DL model. 

## Step 3 - Evaluation
After training, evaluate your trained DL model with the test dataset. This will help to understand the effectiveness of the DL model in classifying organoids.

