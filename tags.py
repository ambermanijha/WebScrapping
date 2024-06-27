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

#print(soup.find(class_="italic"))
#for child in soup.find(class_="container").children:
#    print(child)

#for parent in soup.find(class_="box").parents:
#    print(parent)

"""ulTag=soup.new_tag("ul")
LiTag=soup.new_string("li")
ulTag.append(LiTag)

LiTag=soup.new_tag("li")
LiTag.string="About"
ulTag.append(LiTag)

soup.html.body.insert(0,ulTag)
with open("modified.html","w") as f:
    f.write(str(soup))"""

#cont=soup.find(class_="container")
#print(cont.has_attr("class"))

def has_class_but_not_id(tag):
    return tag.has_attr("class") and tag.has_attr("id")

results=soup.find_all(has_class_but_not_id)
print(results)