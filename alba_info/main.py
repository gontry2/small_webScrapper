import os

import requests
from bs4 import BeautifulSoup
from extract_data import extract_jobs, extract_jobObj
from save import save_to_file

os.system("clear")
alba_url = "http://www.alba.co.kr"

results = requests.get(alba_url)
soup = BeautifulSoup(results.text, "html.parser")
company_box = soup.find("div", {"id": "MainSuperBrand"}).find_all("a", {"class": "goodsBox-info"})
for company in company_box:
  company_name = company.find("span", {"class":"company"}).text
  job_list = []
  jobs = extract_jobs(company)
  for job in jobs:
    jobObj = extract_jobObj(job)
    job_list.append(jobObj)
  
  save_to_file(company_name, job_list)

