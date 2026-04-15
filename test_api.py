import requests

url = "http://127.0.0.1:5000/predict"

data = {
 "Age": 30,
 "Experience_Years": 5,
 "Gender_Male": 1,
 "Department_Finance": 1,
 "Department_HR": 0,
 "Department_Marketing": 0,
 "Department_Product": 0,
 "Department_Sales": 0,
 "Job_Title_Engineer": 1,
 "Job_Title_Executive": 0,
 "Job_Title_Intern": 0,
 "Job_Title_Manager": 0,
 "Education_Level_Master": 0,
 "Education_Level_PhD": 0,
 "Location_Chicago": 1,
 "Location_New York": 0,
 "Location_San Francisco": 0,
 "Location_Seattle": 0
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())