# Indonesian Abusive and Hate Speech Twitter Text Analysis and API Service

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
In pursuit of deeper insights into the dataset, we conducted exploratory data analysis and visualization. This process involved an in-depth examination of word distribution, identification of abusive tweets, categorization of hate speech tweets, and analysis of various types of hate speech within the dataset. Additionally, we utilized word clouds to visualize tweet data, providing a glimpse into the most frequently occurring words in each category of abusive and hate speech.

#### Tweet Word Distribution
Upon analyzing the distribution of words in tweets, the findings reveal that the average word count per tweet is 16 words.Tweets range from a minimum of 1 word to a maximum of 52 words, showcasing the variability in the length of messages across the dataset.
</p>
<img src="https://github.com/alyahusnachoirunnisa/Twitter-analysis-report-and-API/blob/master/Visualization/distribution.png" alt="drawing" width="400"/>
</p>

#### **Abusive and Non-abusive Tweet Analysis**
This analysis delves into tweets labeled as abusive, comparing the distribution of the number of words in tweets categorized as abusive versus non-abusive. The examination includes an assessment of the proportion and count of both abusive and non-abusive tweets within the dataset.
</p>
<img src="https://github.com/alyahusnachoirunnisa/Twitter-analysis-report-and-API/blob/master/Visualization/Abusive.png" alt="drawing"/>
</p>

#### **Hate Speech and Non-Hate Speech Tweet Analysis**
This analysis delves into tweets labeled as hate speech, comparing the distribution of the number of words in tweets categorized as hate speech versus non-hate speech. The examination includes an assessment of the proportion and count of both hate speech and non-hate speech tweets within the dataset.
</p>
<img src="https://github.com/alyahusnachoirunnisa/Twitter-analysis-report-and-API/blob/master/Visualization/Hate%20Speech.png" alt="drawing"/>
</p>

#### **Hate Speech Tweet Category Poroportion**
This analysis provides insights into the proportion of hate speech categorized by its nature. It examines hate speech directed at groups or individuals, explores hate speech related to specific topics, and gauges the intensity of hate speech.
</p>
<img src="https://github.com/alyahusnachoirunnisa/Twitter-analysis-report-and-API/blob/master/Visualization/Proportion.png" alt="drawing"/>
</p>

#### **Hate Speech Tweet Category Poroportion**
Utilizing a heatmap visualization, this analysis illustrates the correlation among different categories of hate speech, offering a visual representation of their interrelationships.
</p>
<img src="https://github.com/alyahusnachoirunnisa/Twitter-analysis-report-and-API/blob/master/Visualization/Heatmap.png" alt="drawing" width="400"/>
</p>

#### **Visualization of Word Intensity in the Dataset**
Enhancing data comprehension, this analysis employs a word cloud visualization to highlight words with the highest occurrence intensity within the tweet dataset, offering a visually striking representation of prominent terms.
</p>
<img src="https://github.com/alyahusnachoirunnisa/Twitter-analysis-report-and-API/blob/master/Visualization/Wordcloud%20hate%20speech.png" alt="drawing" width="400"/>
</p>

#### **Visualization of Word Intensity in Each Hate Speech Category**
Employing a word cloud visualization, this analysis aims to uncover information on words with the highest frequency of occurrence within each hate speech category, providing an insightful representation of distinct linguistic patterns associated with different forms of hate speech.
</p>
<img src="https://github.com/alyahusnachoirunnisa/Twitter-analysis-report-and-API/blob/master/Visualization/Word%20cloud%20hate%20speech%20category.png" alt="drawing"/>
</p>

## Conclusion
The findings derived from the conducted exploratory data analysis lead to the following conclusions:
- The average word count per tweet falls within the range of 10 to 20 words.
- Tweets categorized as hate speech constitute 42.4% of the dataset, while abusive tweets make up 36.3%.
- Prominent words in hate speech tweets include: Jokowi, Indonesia, PKI, Cebong, Ahok, and Presiden.
- The majority of hate speech is directed towards individuals, accounting for 64.1%.
- The prevailing intensity of hate speech is predominantly low, with 60.6% falling into this category.
- Religion emerges as the most discussed topic within the hate speech category.
- Hate speech targeting groups often delves into discussions on religion and race, displaying a tendency towards moderate intensity.
- Hate speech directed at individuals tends to be characterized by weak intensity.
- Hate speech targeting groups exhibits a tendency towards moderate intensity.
