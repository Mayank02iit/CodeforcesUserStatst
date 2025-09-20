from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from collections import Counter
options = Options()
options.add_argument("--headless=new")
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"')

def findLinks(linksFile,username,destinationpath):      
    passed = {}
    driver = webdriver.Chrome(options)
    driver.get(f'https://codeforces.com/submissions/{username}/page/1')
    pageNumbers = driver.find_element(By.XPATH, '//*[@class="pagination"]')
    count_page_numbers = int(pageNumbers.text.split(" ")[-2])
    for i in range(1,count_page_numbers+1):
        driver.get(f'https://codeforces.com/submissions/{username}/page/{i}')
        datatable_div  = driver.find_element(By.CLASS_NAME, "datatable")
        links = datatable_div.find_elements(By.TAG_NAME, "a")
        rows = datatable_div.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            links = row.find_elements(By.TAG_NAME, "a")
            if len(links)==0:
                continue
            if links[-1].get_attribute('href') not in passed and "Accepted" in row.text:
                    passed[links[-1].get_attribute('href')]=True
                    with open(destinationpath+linksFile,'a') as f:
                        f.write(f"{links[-1].get_attribute('href')}\n")
