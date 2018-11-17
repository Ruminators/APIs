from flask import Flask,request,abort
app = Flask(__name__)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json





# =====================================================================================================


driver_path='./bin/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') 
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
d=driver

def initialize():
    d.get('http://theinkblot.com/') 
    print(driver.title)
    d.find_element_by_class_name('gbutton').click()




# =====================================================================================================



def getQues():
    initialize()
    x=[]
    for i in range(9):

        ques=[]
        a=d.find_element_by_class_name('ttable').find_elements_by_tag_name('tr')
        for n in a:
            fix=n.text.encode('utf-8','ignore')
            ques.append(fix)


        print(a)
        print('..........................................................')
        l=d.find_elements_by_name('sel')
        l[0].click()
        d.find_element_by_class_name('gbutton').click()
        img=d.find_element_by_class_name('plate').get_attribute('src')
        
        x.append({"step":i,"ink":img,"content":ques})
    return json.dumps(x)











# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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







def getRes(ans):
    initialize()
    for i in ans:
        ques=[]
        a=d.find_element_by_class_name('ttable').find_elements_by_tag_name('input')
        a[i].click()
        print(d.title)
        print('..........................................................')
        
        d.find_element_by_class_name('gbutton').click()
    
    print('..........................................................')
    print(d.current_url)

    WebDriverWait(d,15).until(EC.text_to_be_present_in_element((By.TAG_NAME,"table"),"Test Results"))
    return d.find_element_by_tag_name('table').text
 
 






# -------------------------------Routing------------------------------------
@app.route('/',methods=['GET'])
def ques_handle():
    return getQues()
 
@app.route('/ans',methods=['POST'])
def ans_handle():
    ans=request.get_json()
    return getRes(ans)
 
if __name__ == "__main__":
    app.run(host="localhost", port=103)

# -------------------------------Routing------------------------------------


getQues()