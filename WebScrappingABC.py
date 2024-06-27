import requests 
from bs4 import BeautifulSoup

with open("sample_company.html","r") as f:
    html_doc=f.read()

soup =  BeautifulSoup(html_doc,'html.parser')

team_section = soup.find('section', class_='team')
if team_section:
    team_members = team_section.find_all('div', class_='member')
    for member in team_members:
        name = member.find('h3', class_='name').text.strip()
        title = member.find('p', class_='title').text.strip()
        print(f"Name: {name}, Title: {title}")

contact_section = soup.find('section', id='contact-us')
if contact_section:
    contact_details = contact_section.find('div', class_='contact-details')
    if contact_details:
        email = contact_details.find('a', class_='email').text.strip()
        phone = contact_details.find('a', class_='phone').text.strip()
        print(f"Email: {email}, Phone: {phone}")