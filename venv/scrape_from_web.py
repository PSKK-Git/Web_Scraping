from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://internshala.com/internships/work-from-home-web-development-internships/').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('div', class_ ='container-fluid individual_internship visibilityTrackerItem')

role =  jobs.find('h3', class_='heading_4_5 profile').text
company_name = jobs.find('a', class_='link_display_like_text view_detail_button').text.replace(' ','')
starting= jobs.find('div', class_ ='item_body').text.replace(' ','')
stipend= jobs.find('span', class_='stipend').text
status= jobs.find('div', class_='other_label_container').text
#print(company_name)
#print(jobs)
print(f'''
Role : {role}

Company Name: {company_name}

Starting From: {starting}

Stipend: {stipend}

Status: {status}
''')

