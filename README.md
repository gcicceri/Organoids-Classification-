# Organoids-Classification-

Within this repository, the main python scripts for pulling the proposed DL models for the multiclassification approach can be found. The aim is to assist researchers in choosing and training the a DL model for classifying organoids into appropriate classes.


## Step 1 - Data Preparation
Before training the DL models, it's necessary to prepare the data. This includes splitting the data into training, validation, and test sets from the original dataset of intestinal organoid annotated images, available at the zenodo archive doi:10.5281/zenodo.6768583. Run **Extract_Val_from_Train.py** and **extract.py** inside Python scripts folder to perform this step.

## Step 2 - Model Selection and Training 
After preparing the data, select the DL models to the training step. This repository includes 6 DL model python scripts. Refer to the **documentation** of each model to understand its features and to train the selected DLmodel. This script will take the training and validation sets.

## Step 3 - Evaluation
After training, evaluate the DL model with the test set data. This will help to understand the effectiveness of the DL model in classifying organoids.

