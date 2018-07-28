from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
driver =webdriver.Firefox()
driver.get('https://nagiosadmin:nagiosadmin@172.17.31.18/nagios/cgi-bin/status.cgi?navbarsearch=1&host=172.17.22.102')
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")


filename=open("D:/files/tableout.html","w+")
tabulka=soup.find("table",{"class":'status'})
print(tabulka)
#for row in tabulka.findAll('tr'):
 #   col = row.findAll('td')
  #  print(col)
filename.write(str(tabulka))
driver.close()
#element.send_keys("192.168.10.1")