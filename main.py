from bs4 import BeautifulSoup
import  requests

reponse_1 = requests.get("https://5etme.com/doaa/4")
site=reponse_1.text
reponse_2= requests.get("https://5etme.com/azkar/2")
site_2=reponse_2.text
reponse_3=requests.get("https://5etme.com/azkar/1")
site_3=reponse_3.text
reponse_4=requests.get("https://5etme.com/azkar/3")
site_4=reponse_4.text
soup_2=BeautifulSoup(site_2,"html.parser")
soup_3=BeautifulSoup(site_3,"html.parser")
soup_4=BeautifulSoup(site_4,"html.parser")
soup=BeautifulSoup(site, "html.parser")
li=soup.find_all(name="div",class_="zeker-txt")
li_2=soup_2.find_all(name="div",class_="zeker-txt")
li_3=soup_3.find_all(name="div",class_="zeker-txt")
li_4=soup_4.find_all(name="div",class_="zeker-txt")
text=[]
for rep in li:
    temp=rep.getText()
    text.append(temp)
for rep in li_2:
    temp=rep.getText()
    text.append(temp)
for rep in li_3:
    temp=rep.getText()
    text.append(temp)
for rep in li_4:
    temp=rep.getText()
    text.append(temp)

with open("ad3ia.txt",mode="w", encoding="utf-8")as file :
    for a in text:
        file.write(f"{a}\n")
