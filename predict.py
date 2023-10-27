from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

def makePrediction(url):
    html_content = getHTML(url)
    title = getData(html_content)
    return title + " is not a scam"

def getData(html_content):
    # declare values as Null
    title = None
    location = None
    departments = None
    salary = None
    company = None
    description = None
    requirements = None
    benefits = None
    telecommuting = None
    has_company_logo = None
    has_questions = None
    employment_type = None
    required_experience = None
    required_education = None
    industry = None
    function = None
    
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

    return title