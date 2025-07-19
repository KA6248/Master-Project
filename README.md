# Arabic Bias Detection - NLP Project

This project aims to build a text classification model to detect bias in Arabic texts. The classification includes various types of political and religious bias. The system is built using transformer-based models from Hugging Face. The project includes data preparation, preprocessing, and model training.

## Project Structure (so far)

- `data_loader.py`: Handles loading, merging, cleaning, and labeling of political and religious bias datasets.
- `preprocessing.py`: Performs text cleaning and normalization specific to Arabic text.
- `models.py`: Loads pre-trained Arabic-compatible transformer models for classification (explained later).
- `runtraining.py`: Training pipeline to be developed in the next step.
- `README.md`: This documentation file.

## Completed Components

### 1. Data Loading and Preparation (`data_loader.py`)

This module merges two datasets:

- A political bias dataset in CSV format
- A religious bias dataset in Excel format

Key steps include:

- Standardizing label names and explicit type annotations
- Mapping textual labels to numerical class IDs
- Dropping rows with missing or invalid data
- Saving the cleaned dataset to a unified CSV file
- Generating descriptive statistics and basic exploratory data analysis

### 2. Text Preprocessing (`preprocessing.py`)

This module provides a cleaning function designed for Arabic language processing. It includes:

- Removing diacritics and Arabic punctuation
- Normalizing different forms of Alef, Yeh, and Teh Marbuta
- Removing digits (both Arabic and English)
- Removing English characters and symbols
- Removing extra spaces and newlines

The output is a standardized, cleaned Arabic text suitable for feeding into transformer-based models.

## Supported Classification Labels

The following classes are currently supported and mapped to numeric labels:

- Unbiased: 0  
- Biased against Palestine: 1  
- Biased against Israel: 2  
- Biased against Muslims: 3  
- Biased against Jews: 4

## Input Data Sources

- Political Bias: `combined_bias_data_with_type_utf8BOM.csv`
- Religious Bias: `extended_religious_bias_dataset_complete_merged_300.xlsx`

## Next Steps

The next component to be implemented is the training pipeline, defined in `runtraining.py`. This will use the cleaned and preprocessed dataset to train a multi-class text classification model using one of several available Arabic transformer models such as AraBERT, CAMeLBERT, or MARBERT.

## Author

This project is part of a broader effort to analyze bias in Arabic media and social content using natural language processing.
