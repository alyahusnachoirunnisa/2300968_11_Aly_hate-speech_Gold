# Indonesian Abusive and Hate Speech Twitter Text Analysis and API

## Project Overview
In this project, We've developed an API tailored to cleanse text data (focusing on *Indonesian Abusive and Hate Speech Twitter Text*) and analyze sentiment text data. The API incorporates a text classification model sourced from [huggingface (ayameRushia)](https://huggingface.co/ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa). Additionally, We conducted a comprehensive analysis of Indonesian Abusive and Hate Speech Twitter Text, presenting the findings in a detailed report formatted as a PowerPoint presentation (pptx).

## Project Objectives
In this kernel, our primary goals include:
1. **API Service for Cleansing and Sentiment Analysis:**
   - Provide a robust API for text cleansing, ensuring the sanitization of your text data.
   - Implement an API capable of predicting the sentiment of input text, distinguishing between positive and negative sentiments.
2. **Indonesian Abusive and Hate Speech Twitter Text Analysis and Report:**
   - Conduct a comprehensive analysis of Indonesian abusive and hate speech in Twitter text data.
   - Generate an insightful report based on this analysis, serving as the foundation for the text cleansing service API.

# API SERVICE

## Prerequisites & Installing
1. **Environment Setup**. 
   To create the environment, you can utilize Conda and execute the following commands:
   ```bash
   conda create --n twitteranalysis_env python=3.9
   ```
   Activate the environment with:
   ```bash
   conda activate twitteranalysis_env
   ```
2. **Dependencies**. 
   All required dependencies to run this kernel are outlined in the `requirements.txt` file. These include FastAPI, uvicorn, pandas, asyncpy, tokenizers, torch,   transformers, torchaudio, and torchvision. Install them using:
   ```bash
   pip install -r requirements.txt
   ```
3. **Running the Kernel**.
  To run this kernel, use uvicorn. It will redirect you to the Swagger documentation, allowing you to access the text cleaning and sentiment analysis services:
    ```bash
    uvicorn main:app --reload --log-level debug --port 8200
    ```

# Indonesian Abusive and Hate Speech Twitter Text Analysis
The analysis was conducted through a meticulous process involving the cleaning of text data and exploratory data analysis. The primary objective was to unearth valuable insights from the data, leading to the creation of a comprehensive report based on the obtained analysis results. The entirety of this analytical endeavor took place within the Google Colab environment. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KHyayCvFggPJk-jM7hZPt54LRA7-vo7f?usp=drive_link)

## Dataset
The dataset employed in this analysis is sourced from [Indonesian Abusive and Hate Speech Twitter](https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection). Comprising 13,023 tweets, each tweet is associated with categorization labels that encompass various dimensions of hate speech and abusive language. The labels are defined as follows:
- **HS**: Hate speech label
- **Abusive**: Abusive language label
- **HS_Individual**: Hate speech targeted to an individual
- **HS_Group**: Hate speech targeted to a group
- **HS_Religion**: Hate speech related to religion/creed
- **HS_Race**: Hate speech related to race/ethnicity
- **HS_Physical**: Hate speech related to physical/disability
- **HS_Gender**: Hate speech related to gender/sexual orientation
- **HS_Other**: Hate related to other invective/slander
- **HS_Weak**: Weak hate speech
- **HS_Moderate**: Moderate hate speech
- **HS_Strong**: Strong hate speech

## Data Cleaning
The data cleaning process encompasses both text and duplicate cleaning. Text cleaning is executed using the RegEx library, incorporating the following commands:
```bash
# Separate words after the hashtag
# Remove the words 'user', 'rt', 'amp', '/n', and 'X'
# Delete symbols
# Convert all letters to lowercase
# Remove non-alphanumeric characters
```
These commands collectively contribute to the refinement and preparation of the dataset for subsequent analysis.

## Expalatory Data Analysis
In pursuit of deeper insights into the dataset, we conducted exploratory data analysis and visualization. This process involved an in-depth examination of word distribution, identification of abusive tweets, categorization of hate speech tweets, and analysis of various types of hate speech within the dataset. Additionally, we utilized word clouds to visualize tweet data, providing a glimpse into the most frequently occurring words in each category of abusive and hate speech. The results of this analysis are presented in the attached document for reference.

### Tweet Word Distribution
Upon analyzing the distribution of words in tweets, the findings reveal that the average word count per tweet is 16 words. Tweets range from a minimum of 1 word to a maximum of 52 words, showcasing the variability in the length of messages across the dataset.
