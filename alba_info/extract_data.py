import requests
from bs4 import BeautifulSoup
alba_url = "http://www.alba.co.kr"


def extract_jobObj(job):
  job_locals = job.find_all("td", {"class": "local"})
  job_titles = job.find_all("td", {"class": "title"})
  job_datas = job.find_all("td", {"class": "data"})
  job_pays = job.find_all("td", {"class": "pay"})
  job_regDates = job.find_all("td", {"class": "regDate"})
  jobObj = {}
  for local in job_locals:
    jobObj["job_local"] = local.text
  for title in job_titles:
    jobObj["job_compnay"] = title.find("span", {"class": "company"}).text
    #job_title = title.find("span", {"class": "title"}).text
  for data in job_datas:
    jobObj["job_data"] = data.find("span", {"class": "time"}).text
  for pay in job_pays:
    payIcon, number = pay.find_all("span")
    jobObj["job_pay"] = payIcon.text + number.text
  for regDate in job_regDates:
    jobObj["job_regDate"] = regDate.text
  return jobObj


def extract_jobs(html):
  if "http" in html.attrs["href"]:
    company_url = html.attrs["href"] 
  else:
    company_url = alba_url + html.attrs["href"]
  
  results = requests.get(company_url)
  soup = BeautifulSoup(results.text, "html.parser")
  jobs = soup.find("div", {"id": "NormalInfo"}).find("tbody").find_all("tr")
  return jobs