import csv

def save_to_file(company_name, job_list):
  print(f"save_file : {company_name}")
  filename = "./files/%s.csv" % company_name
  file = open(filename, mode="w", encoding="utf-8", newline='')
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for job in job_list:
    writer.writerow(list(job.values()))
  return
    