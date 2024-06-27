import requests 
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc=f.read()

soup =  BeautifulSoup(html_doc,'html.parser')
"""print(soup.prettify())
print(soup.title)
print(soup.find_all("div"))"""

"""for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.get_text())"""

s=soup.find(id="link3")

#print(s.get("href"))

#print(soup.select("div.italic"))
#print(soup.select("span#italic"))
#print(soup.span.get("class"))

print(soup.find(class_="italic"))