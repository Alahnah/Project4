# libaries for the webscraping
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# libaries for machine learning
import numpy as np

import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

def getHTML(url):
    chrome_options = Options()
    # bypasses bot detection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    # prevents the browser from actually opening
    chrome_options.add_argument("--headless")
    # create webdriver instance
    driver = webdriver.Chrome(chrome_options)
    # go to the url
    driver.get(url)
    html_content = driver.page_source
    # close the webdriver
    driver.quit()
    # return the pages html
    return html_content

def getData(html_content):
    # declare values as Null
    title = " "
    location = " "
    departments = " "
    salary = " "
    company = " "
    description = " "
    requirements = " "
    benefits = " "
    telecommuting = " "
    has_company_logo = " "
    has_questions = " "
    employment_type = " "
    required_experience = " "
    required_education = " "
    industry = " "
    function = " "
    
    # create bs4 object
    soup = BeautifulSoup(html_content, 'html.parser')

    # collect data
        # title
    try:
        title_element = soup.find('h1', class_='jobsearch-JobInfoHeader-title')
    except:
        title_element = None
    if title_element:
        title = title_element.text
        # location
    try:
        location_element = soup.find('div', {'data-testid': 'inlineHeader-companyLocation'})
    except:
        location_element = None
    if location_element:
        location = location_element.text
        # departments
        # salary
        # company
    try:
        company_element = soup.find('div', {'data-testid': 'inlineHeader-companyName'})
    except:
        company_element = None
    if company_element:
        company = company_element.text
        # description
    try:
        description_element = soup.find('div', class_='jobsearch-jobDescriptionText')
    except:
        description_element = None
    if description_element:
        description = description_element.text
        # requirements
        # benefits
    try:
        benefits_element = soup.find('div', id='benefits').find_all('ul')
    except:
        benefits_element = None
    if benefits_element:
        benefits = ""
        for ul in benefits_element:
            list_items = ul.find_all('li')
            for li in list_items:
                benefits += li.get_text()+", "
        # telecommuting
        # has_company_logo
        # has_questions
        # employment_type
    Full_occurrences = soup.find_all(string="Full-time")
    Part_occurrences = soup.find_all(string="Part-time")
    Temp_occurrences = soup.find_all(string="Temporary")
    Contract_occurrences = soup.find_all(string="Contract")
    if Full_occurrences:
        employment_type = "Full-Time"
    elif Part_occurrences:
        employment_type = "Part-Time"
    elif Temp_occurrences:
        employment_type = "Temporary"
    elif Contract_occurrences:
        employment_type = "Contract"
        # required_experience
        # required_education
        # industry
        # function

    # return the data as a dict
    return {
        "title" : title,
        "location" : location,
        "departments" : departments,
        "salary" : salary,
        "company" : company,
        "description" : description,
        "requirements" : requirements,
        "benefits" : benefits,
        "telecommuting" : telecommuting,
        "has_company_logo" : has_company_logo,
        "has_questions" : has_questions,
        "employment_type" : employment_type,
        "required_experience" : required_experience,
        "required_education" : required_education,
        "industry" : industry,
        "function" : function
    }

def makePredictionTF(url):
    # collect the raw html
    html_content = getHTML(url)
    # extract usable info from the html
    allData = getData(html_content)

    # combine description and benedits into a single string
    selectedData = (allData["description"] + " " + allData["title"]+ " " + allData["location"]+ " " + allData["employment_type"]).strip().replace('\xa0', '')
    # convert the data into a list

    selectedData = [selectedData]

    # use tf to tokenize the webpage data for ML
    tokenizer = tf.keras.models.load_model('pretrainedModels/tf_model/tokenizer_finial.tf')
    tokened_data = tokenizer.predict(selectedData)

    # load the pre-trained model
    model = tf.keras.models.load_model('pretrainedModels/tf_model/Tensorflow_model_finial.keras')

    # Make a prediction on whether the scraped data is from a fraudulent job post or not
    prediction = model.predict(tokened_data)
    
    #Fraud = 1 and legitimate = 0
    prediction =np.where(prediction > .9, 1,0)

    # return a dict
    return {
        "predict" : prediction,
        "title" : allData["title"]
    }