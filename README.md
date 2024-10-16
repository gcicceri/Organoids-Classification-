# Organoids-Classification-

![1691166981456419_class_0 0_5](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/88746677-fb3a-4d3b-a193-0d402ff58a8d)
![1691166999718871_class_1 0_24](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/f981b2db-6dcd-4084-819b-8abe15181237)
![1691166984326195_class_2 0_28](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/bb3635ac-c84e-453a-8a11-b972313c5340)
![1691166997207764_class_3 0_4](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/30914409-ff2c-4768-b314-f9354e3e3164)


This repository contains the implementation of various deep learning models used in our study to classify intestinal organoids. The project evaluates several popular architectures like DenseNet169, MobileNetV2, ResNet50v2, InceptionV3, VGG16, and ViTs to determine which performs best in the organoid classification task. Within this repository, the main Python scripts for pulling the proposed DL models for the multiclassification approach can be found. The aim is to assist researchers in choosing and training a DL model for classifying organoids into appropriate classes.


## Table of Contents

1. [Data Preparation](#data-preparation)
2. [Final Dataset](#final-dataset)
3. [Model Selection and Training](#model-selection-and-training)
4. [Evaluation](#evaluation)
5. [Contact](#contact)


## Data Preparation
Before training the DL models, it's necessary to prepare the data. This includes splitting the data into training, validation, and test sets from the original dataset of intestinal organoid annotated images, available at the zenodo archive **https://zenodo.org/records/6768583#.Y_S9uHbP2Uk**.  
Run **extract.py** and **Extract_Val_from_Train.py** inside the Python scripts folder to perform this step.

## Final Dataset

The **final dataset** built and used in this study is hosted on Google Drive and can be accessed through the following link:

[Download Dataset from Google Drive](https://drive.google.com/drive/folders/1VBfK-1mJI8zpqEfmzp2ShcD2eo5YYMVU?usp=sharing)

Please ensure you comply with the terms of use and citation requirements as described in the associated publication.


## Model Selection and Training 

This repository contains Jupyter Notebook scripts for each of the six deep learning models. To execute the DL models, please navigate to the **Documentation/DL Models** folder. These notebooks are designed to be run in Google Colab, which provides a powerful and interactive cloud-based environment equipped with GPU support to facilitate the training process. Simply open the desired model notebook in Colab and follow the instructions to initiate the training step. To access the Jupyter Notebooks, please contact the corresponding authors for further details and request access.

## Evaluation

Upon completion of the training phase, our experiments allowed for the evaluation of the six deep learning model's performance via the included test dataset. This step was essential for verify the model's proficiency in accurately classifying organoid images.

The trained model weights are an essential part of the deep learning model evaluation process, enabling the replication of our results. We have hosted the weights on Google Drive.
You can download the **DL models weights** from the following link: [Download Models Weights from Google Drive](https://drive.google.com/drive/folders/16fpBoQN1SpueBAWhNcDRJqX526eU-W3k?usp=sharing). Please ensure you comply with any terms of use associated with the data and cite the appropriate paper references when using these weights in your work.  

For an in-depth analysis of the model's predictions, refer to the `Misclassification_Report.xlsx` file.  
This file details the true labels alongside the predicted labels for each image, offering insights into the model's classification patterns and highlighting areas for potential improvement.



## Contact

For any inquiries or further assistance with this project, please reach out to:

**Dr. Giovanni Cicceri**  
Researcher  
University of Palermo  
Email: [giovanni.cicceri@unipa.it](mailto:giovanni.cicceri@unipa.it)




