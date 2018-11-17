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
driver.get('http://theinkblot.com/') 

print(driver.title)

d=driver
d.find_element_by_class_name('gbutton').click()

# =====================================================================================================

x=[]


for i in range(9):

    ques=[]
    a=d.find_element_by_class_name('ttable').find_elements_by_tag_name('tr')
    for n in a:
        fix=n.text.encode('utf-8','ignore')
        print(fix)
        ques.append(fix)


    print(a)
    print('..........................................................')
    l=d.find_elements_by_name('sel')
    l[0].click()
    d.find_element_by_class_name('gbutton').click()
    img=d.find_element_by_class_name('plate').get_attribute('src')
    
    x.append({"step":i,"ink":img,"content":ques})



import json
js=json.dumps(x)

print(js)

# for chkbox in l:
#     chkbox.click()
# d.get("http://theinkblot.com/")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#         print(hii)
#     )
# finally:
#     d.quit()