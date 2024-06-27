import requests
from bs4 import BeautifulSoup 

def FetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)


url= "https://www.abcconsultants.in/"

FetchAndSaveToFile(url, "ABC.html")