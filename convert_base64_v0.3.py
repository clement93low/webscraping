# Load main packages and libraries
from selenium import webdriver
import pandas as pd
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome_driver_path = r"C:\Users\clementlow.fuxing\Documents\myfuturejob\chromedriver"
#chrome_driver_path = r"C:\Users\clementlow.fuxing\OneDrive - PETRONAS\Desktop\RA Job\chromedriver"
#msedge_driver_path = r"C:\Users\clementlow.fuxing\OneDrive - PETRONAS\Desktop\RA Job\msedgedriver"
msedge_driver_path = r"C:\Users\clementlow.fuxing\OneDrive - PETRONAS\Desktop\RA Job\driver\driver_edge_99\msedgedriver"


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
#driver = webdriver.Chrome(chrome_driver_path)
driver = webdriver.Edge(msedge_driver_path)

import base64
def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

"""
###################  FIRST PATTERN    
job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[2]/ngb-highlight'
job_title_xpath_2 = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/ngb-highlight'
date_posted_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[3]'
job_description_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre/article' 
location_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[2]'
sector_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[1]'
company_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[5]'
"""
"""
###################  SECOND PATTERN    

job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/ngb-highlight'
date_posted_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[2]/ul/li[3]'
job_description_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre/article'
location_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[1]/div[2]/h6[2]'
sector_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[2]/ul/li[4]'
company_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[5]'
"""
"""
###################  THIRD PATTERN (DELETED JOB)    
job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[2]/span'
date_posted_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[3]'
job_description_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre/article'
location_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[2]'
sector_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[4]'
company_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[5]'
"""

"""
###################  FOURTH PATTERN   
job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[2]/ngb-highlight'
date_posted_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[3]'
job_description_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre/article'
location_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[2]'
sector_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[4]'
company_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[5]'
"""
################### AZIM
"""
###################  FIRST PATTERN
job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[2]/ngb-highlight'
date_posted_xpath ='/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath ='/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[5]'
#qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]'
job_description_xpath ='/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre'
location_xpath ='/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[3]'
sector_xpath ='/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[1]'
company_xpath ='/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[5]'

################### SECOND PATTERN -ISSUE_1
job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[2]/ngb-highlight'
date_posted_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[5]'
job_description_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre/article'
location_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[2]'
sector_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[1]'
company_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[5]'


################### THIRD PATTERN -ISSUE_2
job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/ngb-highlight'
date_posted_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[2]/ul/li[5]'
job_description_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre/article'
location_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[3]'
sector_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[1]'
company_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[3]/div[2]/div/div[1]/ul/li[5]'
"""

################### FORTH PATTERN -ISSUE_3_vacancy not available
job_title_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[2]/span'
date_posted_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[1]'
applications_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[3]'
positions_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[4]'
qualification_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[2]/ul/li[5]'
job_description_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/pre/article'
location_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[2]'
sector_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[1]'
company_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[1]/div[2]/h6[1]/ngb-highlight'
company_size_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/swipe-vacancy-description/article[1]/ul/li[2]'
esco_xpath = '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[4]/div[2]/div/div[1]/ul/li[5]' 


# BELOW 40
below_40 = 'TE3IiBmaWxsPSIjRkZDQTA1IiBtYXNrPSJ1cmwoI21hc2stNCkiPjwvcGF0aD4NCiAgICAgICAgICAgIDwvZz4NCiAgICAgICAgPC9nPg0KICAgIDwvZz4NCjwvc3ZnPg=='
# ABOVE 40
above_40 = 'GwtMjEiIGZpbGw9IiNGRkNBMDUiIG1hc2s9InVybCgjbWFzay00KSI+PC9wYXRoPg0KICAgICAgICAgICAgPC9nPg0KICAgICAgICA8L2c+DQogICAgPC9nPg0KPC9zdmc+'
# APPRENTICE
apprentice = 'WFzaz0idXJsKCNtYXNrLTIpIj48L3BhdGg+DQogICAgICAgICAgICAgICAgPC9nPg0KICAgICAgICAgICAgPC9nPg0KICAgICAgICA8L2c+DQogICAgPC9nPg0KPC9zdmc+'
# OKU
oku = 'TE4IiBmaWxsPSIjRkZDQTA1IiBtYXNrPSJ1cmwoI21hc2stNCkiPjwvcGF0aD4NCiAgICAgICAgICAgIDwvZz4NCiAgICAgICAgPC9nPg0KICAgIDwvZz4NCjwvc3ZnPg=='
# NULL
no_incentive = ''

def get_details_PART_A(job_x,date_x,applications_x,positions_x,qualification_x,description_x,location_x,sector_x,company_x,company_size_x,esco_x):
    job_title = driver.find_element(By.XPATH, job_title_xpath).text
    print('Job vacancy:',job_title)         

    company = driver.find_element(By.XPATH, company_xpath).text
    print("Company: ", company)     

    date_posted = driver.find_element(By.XPATH, date_posted_xpath).text
    date_posted = date_posted.split(': ')[-1]
    print("Date posted: ", date_posted)                           
    
    applications = driver.find_element(By.XPATH, applications_xpath).text
    applications = applications.split(':')[-1]
    print("Number of application: ", applications)                             
    
    positions = driver.find_element(By.XPATH, positions_xpath).text
    positions = positions.split(':')[-1]
    print("Number of position: ", positions)    

    esco = driver.find_element(By.XPATH, esco_xpath).text
    esco = esco.split(':')[-1]
    print("ESCO Code: ", esco)                        
    
    qualification = driver.find_element(By.XPATH, qualification_xpath).text
    print("qualification: ", qualification)

    job_description = driver.find_element(By.XPATH, job_description_xpath).text
    print("Job Description: ", job_description)     
    
    sector = driver.find_element(By.XPATH, sector_xpath).text
    print("Sector: ",sector)                  

    company_size = driver.find_element(By.XPATH, company_size_xpath).text
    print("Company size: ", company_size)  
    
    location = driver.find_element(By.XPATH, location_xpath).text
    print("Location: ",location)                
                    
    

    return job_title, date_posted, applications, positions, qualification, job_description, location, sector, company, company_size, esco


def get_details_incentive(incentive_input):
    incentive_variety = []
    for i in incentive_input:
        if i == below_40:
            incentive_variety.append("below_40")
        else:
            if i == above_40:
                incentive_variety.append("above_40")
            else:
                if i == apprentice:
                    incentive_variety.append("apprentice")
                else:
                    if i == oku:
                        incentive_variety.append("oku")
                    else:
                        break
    print('Incentive: ', incentive_variety)
    return incentive_variety

def getJobDetails(url):
    driver.get(url)
    local_df = pd.DataFrame(columns=['job_url','salary','job_title','date_posted','applications','positions','qualification','job_description','location','sector','company','company_size','esco','incentive','penjana?'])
    job_title = None
    date_posted = None
    applications = None
    positions = None
    qualification = None
    job_description = None
    location = None
    sector = None
    company = None
    company_size = None
    esco = None
    incentive_variety = None
    penjana_list = None

    try:
        time.sleep(5)
        # TODO to capture apprentice, create one MORE BLOCK OF TRY AND EXCEPT
        try:
            incentives = []
            incentive_element_00 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[3]')
            print("incentive element 00:", incentive_element_00)
            incentive_src_00 = incentive_element_00.get_attribute('src')
            incentive_src_00 = incentive_src_00[-131:]
            print("incentive src:",incentive_src_00)
            incentives.append(incentive_src_00)

            incentive_element_01 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[2]')
            print("incentive element 01:", incentive_element_01)
            incentive_src_01 = incentive_element_01.get_attribute('src')
            incentive_src_01 = incentive_src_01[-131:]
            print("incentive src:",incentive_src_01)
            incentives.append(incentive_src_01)
            
            incentive_element_02 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[1]')
            print("incentive element 02:", incentive_element_02)
            incentive_src_02 = incentive_element_02.get_attribute('src')
            incentive_src_02 = incentive_src_02[-131:]
            print("incentive src:",incentive_src_02)
            incentives.append(incentive_src_02)

            incentive_element_03 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[4]')
            print("incentive element 03:", incentive_element_03)
            incentive_src_03 = incentive_element_03.get_attribute('src')
            incentive_src_03 = incentive_src_03[-131:]
            print("incentive src:",incentive_src_03)
            incentives.append(incentive_src_03)

            print("how many pictures: ", len(incentives))
            #print("this is the content of find elements:",incentives)

            incentive_variety = get_details_incentive(incentives)

            penjana_list = incentive_variety
            
            
            ############
            ############
            job_title, date_posted, applications, positions, qualification, job_description, location, sector, company, company_size, esco = get_details_PART_A(job_title_xpath, 
                                    date_posted_xpath, applications_xpath, positions_xpath, qualification_xpath, job_description_xpath,
                                    location_xpath, sector_xpath, company_xpath, company_size_xpath, esco_xpath)

        except:
            try:
                incentives = []
                incentive_element_00 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[3]')
                print("incentive element 00:", incentive_element_00)
                incentive_src_00 = incentive_element_00.get_attribute('src')
                incentive_src_00 = incentive_src_00[-131:]
                print("incentive src:",incentive_src_00)
                incentives.append(incentive_src_00)

                incentive_element_01 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[2]')
                print("incentive element 01:", incentive_element_01)
                incentive_src_01 = incentive_element_01.get_attribute('src')
                incentive_src_01 = incentive_src_01[-131:]
                print("incentive src:",incentive_src_01)
                incentives.append(incentive_src_01)
                
                incentive_element_02 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[1]')
                print("incentive element 02:", incentive_element_02)
                incentive_src_02 = incentive_element_02.get_attribute('src')
                incentive_src_02 = incentive_src_02[-131:]
                print("incentive src:",incentive_src_02)
                incentives.append(incentive_src_02)

                print("how many pictures: ", len(incentives))
                #print("this is the content of find elements:",incentives)

                incentive_variety = get_details_incentive(incentives)

                penjana_list = incentive_variety
                
                
                ############
                ############
                job_title, date_posted, applications, positions, qualification, job_description, location, sector, company, company_size, esco = get_details_PART_A(job_title_xpath, 
                                        date_posted_xpath, applications_xpath, positions_xpath, qualification_xpath, job_description_xpath,
                                        location_xpath, sector_xpath, company_xpath, company_size_xpath, esco_xpath)
                
            except:
                try:
                    incentives = []
                    incentive_element_01 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[2]')
                    print("incentive element 01:", incentive_element_01)
                    incentive_src_01 = incentive_element_01.get_attribute('src')
                    incentive_src_01 = incentive_src_01[-131:]
                    print("incentive src:",incentive_src_01)
                    incentives.append(incentive_src_01)
                    
                    incentive_element_02 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[1]')
                    print("incentive element 02:", incentive_element_02)
                    incentive_src_02 = incentive_element_02.get_attribute('src')
                    incentive_src_02 = incentive_src_02[-131:]
                    print("incentive src:",incentive_src_02)
                    incentives.append(incentive_src_02)

                    print("how many pictures: ", len(incentives))
                    #print("this is the content of find elements:",incentives)

                    incentive_variety = get_details_incentive(incentives)

                    penjana_list = incentive_variety
                    
                    
                    ############
                    ############
                    job_title, date_posted, applications, positions, qualification, job_description, location, sector, company, company_size, esco = get_details_PART_A(job_title_xpath, 
                                            date_posted_xpath, applications_xpath, positions_xpath, qualification_xpath, job_description_xpath,
                                            location_xpath, sector_xpath, company_xpath, company_size_xpath, esco_xpath)
                    

                except:
                    try:
                        incentives = []
                        incentive_element_01 = driver.find_element(By.XPATH, '/html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[2]/swipe-vacancy-details/div/section/article/div[1]/img[1]')
                        print("incentive element 01:", incentive_element_01)
                        incentive_src_01 = incentive_element_01.get_attribute('src')
                        incentive_src_01 = incentive_src_01[-131:]
                        print("incentive src:",incentive_src_01)
                        incentives.append(incentive_src_01)

                        print("how many pictures: ", len(incentives))
                        #print("this is the content of find elements:",incentives)

                        incentive_variety = get_details_incentive(incentives)
                        penjana_list = incentive_variety

                        ############
                        ############
                        job_title, date_posted, applications, positions, qualification, job_description, location, sector, company, company_size, esco = get_details_PART_A(job_title_xpath, 
                                            date_posted_xpath, applications_xpath, positions_xpath, qualification_xpath, job_description_xpath,
                                            location_xpath, sector_xpath, company_xpath, company_size_xpath, esco_xpath)

                    except:
                        try:
                            incentive_variety = None
                            penjana_list = None
                            print("see if it reach penjana: ", penjana_list)

                            ############
                            ############
                            job_title, date_posted, applications, positions, qualification, job_description, location, sector, company, company_size, esco = get_details_PART_A(job_title_xpath, 
                                                date_posted_xpath, applications_xpath, positions_xpath, qualification_xpath, job_description_xpath,
                                                location_xpath, sector_xpath, company_xpath, company_size_xpath, esco_xpath)

                        except:    
                            #print("No information. Please update all the xpath.")
                            job_title = None
                            date_posted = None
                            applications = None
                            positions = None
                            qualification = None
                            job_description = None
                            location = None
                            sector = None
                            company = None
                            company_size = None
                            esco = None
                            incentive_variety = None
                            penjana_list = None
    except:
        print("Something went wrong with WAIT")
    
    # Saving each variables that we created into the Data Frame
    d = {'job_url':job_url,'salary':salary,'job_title':job_title,'date_posted':date_posted,'applications':applications, 'positions':positions,'qualification':qualification,'job_description': job_description,'location':location,'sector':sector, 'company':company, 'company_size':company_size,'esco':esco,'incentive':incentive_variety,'penjana?':penjana_list}
    local_df = local_df.append(d, ignore_index=True)
    return (local_df)

#READING JOB LINKS
#df = pd.read_csv('job_links_LESS_THAN_1200.csv')
#df = pd.read_csv('job_links_1200_1499.csv')
#df = pd.read_csv('job_links_1500_1999_v1.csv')
#df = pd.read_csv('job_links_2000_2499.csv')
#df = pd.read_csv('job_links_2500_2999.csv')
#df = pd.read_csv('job_links_3000_3499.csv')
#df = pd.read_csv('job_links_3500_3999.csv')
#df = pd.read_csv('job_links_4000_4999.csv')
#df = pd.read_csv('job_links_5000_5999.csv')
#df = pd.read_csv('job_links_6000_7999.csv')
#df = pd.read_csv('job_links_8000_9999.csv')
#df = pd.read_csv('job_links_10000_12999.csv')
#df = pd.read_csv('job_links_13000_15999.csv')
#df = pd.read_csv('job_links_MORE_than_16000.csv')
#df = pd.read_csv('job_links_issue_1.csv')
df = pd.read_csv('job_links_issue_3.csv')

## TESTING
#df = pd.read_csv('job_links_MORE_than_16000_test.csv')
#df = pd.read_csv('job_links_issue_1_test.csv')

# Creating "job details" Data Frame and setting column names
job_details_dataframe = pd.DataFrame(columns=['job_url','salary','job_title','date_posted','applications','positions','qualification','job_description','location','sector','company','company_size','esco','incentive','penjana?'])

print("Extracting job details now...")
for index, row in df.iterrows():
    myDf = pd.DataFrame(columns=['job_url','salary','job_title','date_posted','applications','positions','qualification','job_description','location','sector','company','company_size','esco','incentive','penjana?'])
    job_url = (row['job_url'])
    #job_url = job_url.split('distance=1&')[-1]
    job_url = job_url.split('/description?')[-1]
    id = job_url.split('&CONTRACT_TYPE')[0]
    new_job_url= "https://candidates.myfuturejobs.gov.my/search-jobs/description?" + id
    #new_job_url= "https://candidates.myfuturejobs.gov.my/search-jobs/description?" + job_url

    #new_job_url = "https://candidates.myfuturejobs.gov.my/search-jobs?what=&where=&distance=1&" + id
    #print("This is new job url: ", new_job_url)
    print('\n')
    print("JOB ", index)

    #Duplicate the 'job_url' column for 'salary_category' column
    #job_details_dataframe['salary_category'] = job_details_dataframe['job_url']
    salary = (row['job_url']).split('SALARY=')[-1]

    time.sleep(1)
    myDf = getJobDetails(new_job_url)
    print('SALARY: ', salary)
    job_details_dataframe = job_details_dataframe.append(myDf, ignore_index=True)


# Assign yes/no to 'penjana?' column
job_details_dataframe.loc[job_details_dataframe['penjana?'].str.len()>0,'penjana?']='Yes'
job_details_dataframe.loc[job_details_dataframe['penjana?'].str.len()==0,'penjana?']='No'


# Fill value '0' in rows with NA 
job_details_dataframe = job_details_dataframe.fillna(0)
print(job_details_dataframe)

print("Total jobs extracted: ", len(job_details_dataframe["job_url"]))
print("Completed.")

#Reading data into CSV file
#job_details_dataframe.to_csv('job_details_less_than_1200.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_1200_1499.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_1500_1999_v1.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_2000_2499.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_2500_2999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_3000_3499.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_3500_3999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_4000_4999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_5000_5999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_6000_7999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_8000_9999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_10000_12999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_13000_15999.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_MORE_than_16000.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_issue_1.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_issue_2.csv',index=False,header=True)
job_details_dataframe.to_csv('job_details_issue_3.csv',index=False,header=True)


## TESTING 
#job_details_dataframe.to_csv('job_details_deletedjobs.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_issue_2.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_MORE_than_16000_test.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_MORE_than_16000_test_v2.csv',index=False,header=True)
#job_details_dataframe.to_csv('job_details_MORE_than_16000_test_v3.csv',index=False,header=True)


#Closing web browser
time.sleep(2)
driver.quit()