import time

from bs4 import BeautifulSoup
import requests
import lxml
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"

}

request=requests.get(url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D",headers=headers)
request.raise_for_status()
data=request.text


soup=BeautifulSoup(data,"lxml")


addr=soup.find_all(class_="list-card-addr")
address=[i.getText().replace(',',"")   for i in addr]


link=soup.find_all(class_="list-card-img")



links=[]
final_links=[]
for i in link:
    # trial=i['href']
    trial=i.get('href')
    links.append(trial)

for i in range(8):
    if "http" not in links[i]:
        final_links.append(f"https://www.zillow.com{links[i]}")
    else:
        final_links.append(links[i])




prices=soup.find_all(class_="list-card-price")
prices_final=[i.getText()    for i in prices]


print(address)
print(final_links)
print(prices_final)




driver.get("https://forms.gle/p9Xay7gmKeD3Mjfs6")
time.sleep(2)

for i in range(len(address)-1):
    time.sleep(2)

    address_1=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_1.send_keys(address[i])

    Price_1=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Price_1.send_keys(prices_final[i])

    Link_1=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Link_1.send_keys(final_links[i])

    submit=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    time.sleep(2)
    reform=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    reform.click()


hehehe