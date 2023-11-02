# Project4


# Rationale
- Create a model to determine the legitimacy of job postings on Indeed
- Using a dataset of 18,000 job posts from Kaggle to predict whether or not future job postings on Indeed are fraudulent or genuine
# Methods and Tools Used
- ETL: Pandas, Numpy, PostgreSQL
- ML:  SkLearn, nltk.tokenize,  tensorflow
- Web UI: Flask, Selenium, Beautiful Soup, Tensor Flow

# Part One: ETL
- Data is loaded into Jupyter Notebook and cleaned of unnecessary information
- Use of Pandas and Numpy to clean and organize the data into many CSV files
- Creation of a DBD to outline the database
- Load data into PostgreSQL to create a database 

# Part Two: Classification Models w/ SkLearn
- KNN vs. Random Forest 
  - KNN: ROC AUC of 70%
    - n_neighbors = 3
  - RNF: ROC AUC of 76%
    ![image](https://github.com/Alahnah/Project4/assets/132726623/0d331811-ddb8-411d-b590-a146d1000bcc)
    ![image](https://github.com/Alahnah/Project4/assets/132726623/d2de6551-123a-41a9-b98c-ee60ec73c22b)



# Part Three: Tensorflow Challenges 
- Data needed to be tokenized
- Majority of data was legitimate
- Common issue when training against fraud
- Fraudulent data gets drowned out
- Model predicts all entries are legit giving high accuracy 
  - Accuracy is not a good measurement here
- Adding class weights and reducing legit entries was key

# Part Three: Continued
- Slight over sensitivity to fraud
- classification accuracy above 80%
- Corrected for in demo by adjusting fraud threshold 

# Part Four: UI, Web Scraping, Making a Prediction
### Web UI:
- Flask
- Bootstrap

### Web Scraping:
- Indeed bot protection
  - selenium (headless)
  - “user-agent” data
- Beautiful Soup
  - get data by id, name, or class
  - search for keywords

### Making a Prediction:
- Import tokenizer model
- Tokenize the scraped data
  - combine data points into a single string before tokenizing
- Import predictive model
- Make a prediction
- Convert the prediction % to a pass fail
- Return the verdict to the user on a new flask page

