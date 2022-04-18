from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import csv
msedge_driver_path = r"C:\Users\clementlow.fuxing\OneDrive - PETRONAS\Desktop\RA Job\driver\driver_edge_99\msedgedriver"
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
#driver = webdriver.Chrome(chrome_driver_path)
driver = webdriver.Edge(msedge_driver_path)
quotes=[]

# Add the url on branch feature_01
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=8580f4f0a77944f0a54507b7e9c2f4e8&CONTRACT_TYPE=1&SALARY=A'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=bb2cba52bd7048f8af535904961ec3cf&CONTRACT_TYPE=1&SALARY=B'
url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=438e51a768254eb2ad0173d0d4925d1c&CONTRACT_TYPE=1&SALARY=C'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=2d99d195f5244386b837fee5c173e246&CONTRACT_TYPE=1&SALARY=D'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=d8be012397a148208f2ca36ee6925214&CONTRACT_TYPE=1&SALARY=E'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=ed4f998a2ff04964a73bb8a1b1e1d150&CONTRACT_TYPE=1&SALARY=F'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=9d18719f0c7a4cbfb00b22e6d8565e13&CONTRACT_TYPE=1&SALARY=G'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=6ad1b1ec1d63491ebb00f5d284ccdd5e&CONTRACT_TYPE=1&SALARY=H'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=dc5ee452f4674674a1f56c21b0e6837d&CONTRACT_TYPE=1&SALARY=I'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=f7ff2c002e9d4731ac8a5bb4dbe3a07d&CONTRACT_TYPE=1&SALARY=J'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=4c7a863612df4f0491023a4380784d1f&CONTRACT_TYPE=1&SALARY=K'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=347b0e4da47b4226b2f20b7b0f5adaf4&CONTRACT_TYPE=1&SALARY=L'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=003ee056a00a45ebbc2af43d622249aa&CONTRACT_TYPE=1&SALARY=M'
# url = 'https://candidates.myfuturejobs.gov.my/search-jobs/description?jobId=d4e029c67e93439bac76bfd7f5bbb4e6&CONTRACT_TYPE=1&SALARY=N'

driver.get(url)
print("Extracting job links now...")

myLength = len(WebDriverWait(driver, 1000).until(EC.visibility_of_all_elements_located((By.XPATH,"./html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[1]/div/div[2]/div/a"))))
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    try:
        WebDriverWait(driver, 400).until(lambda driver: len(driver.find_elements_by_xpath("./html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[1]/div/div[2]/div/a")) > myLength)
        quotes = driver.find_elements_by_xpath("./html/body/swipe-root/div[2]/swipe-job-seeker/swipe-search-page-frame/div/div[3]/div[1]/div/div[2]/div/a")
        myLength = len(quotes)      
    except TimeoutException:
        break
joblink_ls=[]

for quote in quotes:
    print(quote.get_attribute("href")) 
    joblink_ls.append(quote.get_attribute("href"))
print("Total extracted job links: ", len(quotes))
print("Completed.")
df = pd.DataFrame(joblink_ls,columns=['job_url'])

#df.to_csv('job_links_LESS_THAN_1200.csv', index=False, header=True)
#df.to_csv('job_links_1200_1499.csv', index=False, header=True)
df.to_csv('job_links_1500_1999_v1.csv', index=False, header=True)
#df.to_csv('job_links_2000_2499.csv', index=False, header=True)
#df.to_csv('job_links_2500_2999.csv', index=False, header=True)
#df.to_csv('job_links_3000_3499.csv', index=False, header=True)
#df.to_csv('job_links_3500_3999.csv', index=False, header=True)
#df.to_csv('job_links_4000_4999.csv', index=False, header=True)
#df.to_csv('job_links_5000_5999.csv', index=False, header=True)
#df.to_csv('job_links_6000_7999.csv', index=False, header=True)
#df.to_csv('job_links_8000_9999.csv', index=False, header=True)
#df.to_csv('job_links_10000_12999.csv', index=False, header=True)
#df.to_csv('job_links_13000_15999.csv', index=False, header=True)
#df.to_csv('job_links_MORE_THAN_16000.csv', index=False, header=True)

time.sleep(1)
driver.quit()



