from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text=requests.get('https://internshala.com/internships/work-from-home-web-development-internships/').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_ ='container-fluid individual_internship visibilityTrackerItem')
    for job in jobs:
        stipend= job.find('span', class_='stipend').text
        if '10,000' in stipend:

            role =  job.find('h3', class_='heading_4_5 profile').text
            company_name = job.find('a', class_='link_display_like_text view_detail_button').text.replace(' ','')
            starting= job.find('div', class_ ='item_body').text.replace(' ','')
            status= job.find('div', class_='other_label_container').text
            #more_info=job.div.h3.a['herf ']
            # print(f'''
            #  Role : {role}
            #
            #  Company Name: {company_name}
            #
            #  Starting From: {starting}
            #
            #  Stipend:  {stipend}
            #
            #  Status:  {status}
            #
            #  NEXT
            #  ''')
            print(f"Role : {role.strip()}")
            print(f"Company Name: {company_name.strip()}")
            print(f"Stipend:  {stipend.strip()}")
           # print(f'More Info: {more_info}')
            print('')

if __name__ == '__scrape_from_web__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)