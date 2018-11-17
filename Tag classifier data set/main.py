from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






# =====================================================================================================

driver_path='./chromedriver.exe'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') 

driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)


link='https://www.beyondblue.org.au/who-does-it-affect/personal-stories?category=7c245435-a559-465b-bdcb-8b993cb47c6e'

driver.get(link) 

print(driver.title)

d=driver
# =====================================================================================================


dr='./dataset/depression/'


def getpage(i):
    driver.get(link) 
    r=d.find_element_by_id('ctl00_MainContentPlaceholder_C006_rlvList_pager')
    r=r.find_elements_by_tag_name('a')
    script=r[i].get_attribute('href')
    d.execute_script(script)





r=d.find_element_by_id('ctl00_MainContentPlaceholder_C006_rlvList_pager')
r=r.find_elements_by_tag_name('a')
count=len(r)
ll=[]
for i in range(count):
    
    
    getpage(i)    
    p=d.find_elements_by_class_name('read-more')
    co=len(p)
    for j in p:
        ll.append(j.get_attribute('href'))
    
print(ll)



count=1
for i in ll:
    count+=1
    d.get(i)
    es=d.find_element_by_id('MainContentPlaceholder_TEE6B523B001_Col00').text
    txt=es
    with open(dr+'story_'+str(count)+'.txt', 'a') as the_file:
        the_file.write(txt.encode('utf-8','ignore'))
 