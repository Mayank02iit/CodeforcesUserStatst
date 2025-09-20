from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from collections import Counter
import re
options = Options()
options.add_argument("--headless=new")
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"')      

def findData(linksFile,InfoFile,destinationpath):
    count = Counter()
    special = 0
    driver = webdriver.Chrome(options)
    with open(destinationpath+linksFile, 'r') as file:
        for line in file:
            link = line.strip()
            driver.get(link)
            sideboxes = driver.find_elements(By.CSS_SELECTOR, ".roundbox.sidebox.borderTopRound")
            box = False
            if len(sideboxes)>1:
                box = re.split(r'[\s]+', sideboxes[-2].text)
            elif len(sideboxes)==1:
                box = re.split(r'[\s]+', sideboxes[-1].text)
            else :
                pass
            if box:
                Flag = False
                for element in box:
                    if element[0]=='*':
                        if element[1:] != "special":
                            count[int(element[1:])]+=1
                        else:
                            special+=1
                        Flag = True
                if not Flag :
                    count[0]+=1
                    
    count = dict(sorted(count.items()))
    with open(destinationpath+InfoFile , 'a') as f:
        for key ,value in count.items():
            f.write(f"The number of questions solved whose rating {key} is {value}\n")
        f.write(f"the number of special questions solved is {special}")
    print(f"Information is successfully written in the file {destinationpath+InfoFile}")

