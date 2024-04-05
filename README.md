# Organoids-Classification-

![1691166996093929_class_3 0_3](https://github.com/gcicceri/Organoids-Classification-/assets/13137847/99d8d74e-0494-45cc-b4f5-575bbbf877e4)


Within this repository, the main Python scripts for pulling the proposed DL models for the multiclassification approach can be found. The aim is to assist researchers in choosing and training a DL model for classifying organoids into appropriate classes.


## Step 1 - Data Preparation
Before training the DL models, it's necessary to prepare the data. This includes splitting the data into training, validation, and test sets from the original dataset of intestinal organoid annotated images, available at the zenodo archive **https://zenodo.org/records/6768583#.Y_S9uHbP2Uk**. Run **extract.py** and **Extract_Val_from_Train.py** inside the Python scripts folder to perform this step.
## Step 2 - Model Selection and Training 
After preparing the data, select the DL models for the training step. This repository includes six DL-model Python scripts (.ipynb). Refer to the **documentation/DL Models** folder to train the selected DL model. 

## Step 3 - Evaluation
After training, evaluate your trained DL model with the test dataset. This will help to understand the effectiveness of the DL model in classifying organoids.

