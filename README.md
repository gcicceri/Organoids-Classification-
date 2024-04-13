# Organoids-Classification-

![1691166981456419_class_0 0_5](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/88746677-fb3a-4d3b-a193-0d402ff58a8d)
![1691166999718871_class_1 0_24](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/f981b2db-6dcd-4084-819b-8abe15181237)
![1691166984326195_class_2 0_28](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/bb3635ac-c84e-453a-8a11-b972313c5340)
![1691166997207764_class_3 0_4](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/30914409-ff2c-4768-b314-f9354e3e3164)


This repository contains the implementation of various deep learning models used in our study to classify intestinal organoids. The project evaluates several popular architectures like DenseNet169, MobileNetV2, ResNet50v2, InceptionV3, VGG16, and ViTs to determine which performs best in the organoid classification task. Within this repository, the main Python scripts for pulling the proposed DL models for the multiclassification approach can be found. The aim is to assist researchers in choosing and training a DL model for classifying organoids into appropriate classes.


## Table of Contents

1. [Data Preparation](#data-preparation)
2. [Model Selection and Training](#model-selection-and-training)
3. [Evaluation](#model-evaluation)
4. [Contacts](#contacts)


## Data Preparation
Before training the DL models, it's necessary to prepare the data. This includes splitting the data into training, validation, and test sets from the original dataset of intestinal organoid annotated images, available at the zenodo archive **https://zenodo.org/records/6768583#.Y_S9uHbP2Uk**. Run **extract.py** and **Extract_Val_from_Train.py** inside the Python scripts folder to perform this step.

## Model Selection and Training 
After preparing the data, select the DL models for the training step. 
This repository includes six DL-model Python scripts (.ipynb). 
Refer to the **documentation/DL Models** folder to run the selected DL model. 


## Evaluation
After training, evaluate your trained DL model with the test dataset. This will help to understand the effectiveness of the DL model in classifying organoids.


## Contacts

Giovanni Cicceri
Researcher
University of Palermo
giovanni.cicceri@unipa.it



